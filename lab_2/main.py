#!/usr/bin/env python3

from faculty import Faculty
from department import Department
from student import Student
from discipline import Discipline
from exceptions import FacultyError

def init_raf():
    raf = Faculty("РФиКТ")
    kkb = Department("кибербезопасности")
    kfiz = Department("физики")
    kmat = Department("математики")
    ksi = Department("системного анализа")
    raf.add_department(kkb)
    raf.add_department(kfiz)
    raf.add_department(kmat)
    raf.add_department(ksi)

    pi = "прикладная информатика"
    kb = "кибербезопасность"

    mechanics = Discipline("Механика", 1)
    electricity = Discipline("Электричество", 2)
    optics = Discipline("Оптика", 3)
    angeo = Discipline("АГиЛА", 1)
    linal = Discipline("АГиЛА", 2)
    db = Discipline("Базы данных", 3)

    kfiz.add_course(mechanics, pi)
    kfiz.add_course(electricity, pi)
    kfiz.add_course(optics, pi)
    kfiz.add_course(optics, kb)
    kmat.add_course(angeo, pi)
    kmat.add_course(linal, pi)
    kmat.add_course(angeo, kb)
    kmat.add_course(linal, kb)
    ksi.add_course(db, kb)

    myself = Student("Харитич", "Елисей", "Алексеевич", "прикладная информатика", 2, None)
    vadim = Student("Барановский", "Вадим", None, "кибербезопасность", 3, None)

    raf.add_student(myself)
    raf.add_student(vadim)

    raf.enroll_in_discipline(myself.id, linal.id)
    raf.enroll_in_discipline(myself.id, electricity.id)

    raf.enroll_in_discipline(vadim.id, optics.id)
    raf.enroll_in_discipline(vadim.id, db.id)

    raf.set_grade(myself.id, linal.id, 7)
    raf.set_grade(myself.id, electricity.id, 3)

    raf.set_grade(vadim.id, optics.id, 9)
    raf.set_grade(vadim.id, db.id, 10)

    return raf

def main():
    faculty = init_raf()
    while True:
        print()
        print("1. Зачислить студента на специальность")
        print("2. Отчислить студента")
        print("3. Записать студента на дисциплину")
        print("4. Удалить студента с дисциплины")
        print("5. Выставить оценку")
        print("6. Перевести студента в следующий семестр")
        print("7. Ведомость по студенту (в файл)")
        print("8. Ведомость по дисциплине (в файл)")
        print("9. Ведомость по студенту (в терминал)")
        print("10. Ведомость по дисциплине (в терминал)")
        print("11. Показать всех студентов")
        print("12. Показать все дисциплины и кафедры")
        print("13. Зачислить нового студента")
        print("14. Ввести новую кафедру")
        print("15. Ввести новую дисциплину")
        print("16. Ввести курс на кафедру")
        print("0. Выход")
        choice = input("Выберите действие: ").strip()

        try:
            if choice == "0":
                print("До свидания!")
                break

            elif choice == "1":
                sid = int(input("ID студента: "))
                spec = input("Специальность (например, 'прикладная информатика'): ").strip()
                faculty.enroll_student(sid, spec)

            elif choice == "2":
                sid = int(input("ID студента: "))
                faculty.expel_student(sid)

            elif choice == "3":
                sid = int(input("ID студента: "))
                did = int(input("ID дисциплины: "))
                faculty.enroll_in_discipline(sid, did)

            elif choice == "4":
                sid = int(input("ID студента: "))
                did = int(input("ID дисциплины: "))
                faculty.drop_discipline(sid, did)

            elif choice == "5":
                sid = int(input("ID студента: "))
                did = int(input("ID дисциплины: "))
                grade = int(input("Оценка (1-10): "))
                faculty.set_grade(sid, did, grade)

            elif choice == "6":
                sid = int(input("ID студента: "))
                faculty.promote_student(sid)

            elif choice == "7":
                sid = int(input("ID студента: "))
                fname = input("Имя файла (Enter - по умолчанию): ").strip() or f"report_student_{sid}.txt"
                faculty.report_for_student(sid, fname)

            elif choice == "8":
                did = int(input("ID дисциплины: "))
                fname = input("Имя файла (Enter - по умолчанию): ").strip() or f"report_discipline_{did}.txt"
                faculty.report_for_discipline(did, fname)

            elif choice == "9":
                sid = int(input("ID студента: "))
                faculty.report_for_student(sid)

            elif choice == "10":
                did = int(input("ID дисциплины: "))
                faculty.report_for_discipline(did)

            elif choice == "11":
                print("\nСтуденты:")
                for k, v in faculty.students.items():
                    print(f"{k}. {v}")

            elif choice == "12":
                print("\nДисциплины:")
                for d in set(faculty.disciplines):
                    print(f"  {d.name}, {d.term} семестр")
                print("\nКафедры и читаемые курсы:")
                for department in faculty.departments.values():
                    print(f"  {department.id}. {department.name}:")
                    for (_, specialty), discipline in department.courses.items():
                        print(f"    {discipline.id}. {discipline.name} ({discipline.term} семестр) для '{specialty}'")

            elif choice == "13":
                last_name = input("Фамилия: ").strip()
                first_name = input("Имя: ").strip()
                patronymic = input("Отчество: ").strip() or None
                specialty = input("Специальность: ").strip() or None
                term = int(input("Семестр: "))
                faculty.add_student(Student(last_name, first_name, patronymic, specialty, term))

            elif choice == "14":
                name = input("Название кафедры: ").strip()
                faculty.add_department(Department(name))

            elif choice == "15":
                name = input("Название дисциплины: ").strip()
                term = input("Семестр: ").strip()
                did = int(input("ID читающей кафедры: "))
                specialty = input("Специальность: ").strip()
                faculty.get_department(did).add_course(Discipline(name, term), specialty)

            elif choice == "16":
                diid = int(input("ID дисциплины: "))
                deid = int(input("ID кафедры: "))
                specialty = input("Специальность: ").strip()
                faculty.get_department(deid).add_course(faculty.get_discipline(diid), specialty)

            else:
                print("Неверный пункт меню.")

        except FacultyError as e:
            print(f"Ошибка: {e}")

        except ValueError:
            print("Ошибка ввода!")

if __name__ == "__main__":
    main()
