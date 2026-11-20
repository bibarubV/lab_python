#!/usr/bin/env python3

import functools

from exceptions import *

class Faculty:
    __id = 0

    def __init__(self, name, departments=None, students=None):
        self.id = Faculty.__id
        Faculty.__id += 1

        self.name = name
        self.departments = departments or {}
        self.students = students or {}

    def check_student(func):
        arg_i = func.__code__.co_varnames[:func.__code__.co_argcount].index("student_id")

        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            student_id = args[arg_i-1]
            if student_id not in self.students:
                raise StudentNotFoundError("студент с id "+str(student_id)+" не найден")
            result = func(self, *args, **kwargs)
            return result
        return wrapper

    def check_department(func):
        arg_i = func.__code__.co_varnames[:func.__code__.co_argcount].index("department_id")

        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            department_id = args[arg_i-1]
            if department_id not in self.departments:
                raise DepartmentNotFoundError("кафедра с id "+str(department_id)+" не найдена")
            result = func(self, *args, **kwargs)
            return result
        return wrapper

    def add_department(self, department):
        self.departments[department.id] = department

    def remove_department(self, department):
        del self.departments[department.id]

    def add_student(self, student):
        self.students[student.id] = student

    def remove_student(self, student):
        del self.students[student.id]

    @check_department
    def get_department(self, department_id):
        return self.departments[department_id]

    @check_student
    def get_student(self, student_id):
        return self.students[student_id]

    def enroll_student(self, student_id, specialty):
        student = self.get_student(student_id)
        if student.specialty:
            raise FacultyError("студент уже зачислен на специальность")
        supported_specialties = [specialty for department in self.departments.values() for (specialty, _) in department.courses]
        if specialty not in supported_specialties:
            raise SpecialtyNotSupportedError("специальность '"+str(specialty)+"'не поддерживается факультетом")
        student.specialty = specialty

    @check_student
    def expel_student(self, student_id):
        del self.students[student_id]

    def get_discipline(self, discipline_id):
        for department in self.departments.values():
            try:
                return department.get_discipline(discipline_id)
            except DisciplineNotFoundError:
                pass
        raise DisciplineNotFoundError("дисциплина с id "+str(discipline_id)+" не найдена")

    @property
    def disciplines(self):
        disciplines = []
        for department in self.departments.values():
            for discipline in department.courses.values():
                disciplines.append(discipline)
        return disciplines

    def enroll_in_discipline(self, student_id, discipline_id):
        student = self.get_student(student_id)
        if not student.specialty:
            raise FacultyError("студент не зачислен на специальность")
        if discipline_id in student.grades:
            raise FacultyError("студент уже изучает дисциплину")
        if self.get_discipline(discipline_id).term != student.term:
            raise FacultyError(f"дисциплина недоступна для "+str(student.term)+" курса")

        student.grades[discipline_id] = None

    def drop_discipline(self, student_id, discipline_id):
        student = self.get_student(student_id)
        if discipline_id not in student.grades:
            raise StudentNotEnrolledError("студент не записан на дисциплину")
        del student.grades[discipline_id]

    def set_grade(self, student_id, discipline_id, grade):
        student = self.get_student(student_id)
        if discipline_id not in student.grades or student.grades[discipline_id] is not None:
            raise StudentNotEnrolledError("студент не записан на дисциплину")
        if not isinstance(grade, int) or not 1 <= grade <= 10:
            raise InvalidGradeError("оценка должна быть целым числом от 1 до 10")
        student.grades[discipline_id] = grade

    def promote_student(self, student_id):
        student = self.get_student(student_id)
        if not student.grades:
            raise FacultyError("студент не изучает ни одной дисциплины")
        bad_grades = []
        for discipline_id, grade in student.grades.items():
            discipline = self.get_discipline(discipline_id)
            if discipline.term == student.term and (grade is None or grade < 4):
                bad_grades.append(discipline)
        if bad_grades:
            raise NotAllDisciplinesPassedError("не все дисциплины семестра успешно изучены: "+repr(bad_grades))
        student.term += 1

    def report_for_student(self, student_id, filename=None):
        student = self.get_student(student_id)
        lines = []
        lines.append(f"Ведомость успеваемости студента")
        lines.append(f"ФИО: {student.last_name} {student.first_name} {student.patronymic}")
        lines.append(f"ID: {student.id}")
        lines.append(f"Специальность: {student.specialty}")
        lines.append(f"Семестр: {student.term}")
        lines.append("-"*60)
        lines.append(f"{'Дисциплина':<30}{'Кафедра':<20}{'Оценка':<10}")
        lines.append("-"*60)
        for discipline_id, grade in student.grades.items():
            discipline = self.get_discipline(discipline_id)
            department_name = None
            for department in self.departments.values():
                if department.teaches_course(discipline, student.specialty):
                    department_name = department.name
                    break
            grade_str = str(grade) if grade is not None else "-"
            lines.append(f"{discipline.name:<30}{department_name:<20}{grade_str:<10}")
        lines.append("-"*60)
        lines.append(f"Средний балл: {student.average_grade:.2f}")
        lines.append("")
        if filename:
            with open(filename, "w", encoding="utf-8-sig") as f:
                f.write("\n".join(lines))
            print(f"Ведомость сохранена в файл '{filename}'")
        else:
            print(*lines, sep="\n")

    def report_for_discipline(self, discipline_id, filename=None):
        discipline = self.get_discipline(discipline_id)
        department_name = None
        for department in self.departments.values():
            for (discipline_id_, _) in department.courses:
                if discipline.id == discipline_id_:
                    department_name = department.name
                    break
            if department_name is not None:
                break
        rows = []
        average = 0
        count = 0
        for student in self.students.values():
            if discipline.id in student.grades:
                grade = student.grades[discipline.id]
                grade_str = str(grade) if grade is not None else "-"
                rows.append((student.full_name, student.specialty, grade_str))
                if grade is not None:
                    average += grade
                    count += 1
        average = average/count if count else 0.
        lines = []
        lines.append(f"Ведомость по дисциплине: {discipline.name}")
        lines.append(f"Читающая кафедра: {department_name}")
        lines.append(f"Средний балл: {average:.2f}")
        lines.append("-"*85)
        lines.append(f"{'Студент':<50}{'Специальность':<25}{'Оценка':<10}")
        lines.append("-"*85)
        for name, specialty, grade in rows:
            lines.append(f"{name:<50}{specialty:<25}{grade:<10}")
        lines.append("")
        if filename:
            with open(filename, "w", encoding="utf-8-sig") as f:
                f.write("\n".join(lines))
            print(f"Ведомость сохранена в файл '{filename}'")
        else:
            print(*lines, sep="\n")
