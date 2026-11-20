#!/usr/bin/env python3

class Student:
    __id = 0

    def __init__(self, last_name, first_name, patronymic=None, specialty=None, term=1, grades=None):
        self.id = Student.__id
        Student.__id += 1

        self.last_name = last_name
        self.first_name = first_name
        self.patronymic = patronymic
        self.specialty = specialty
        self.term = term

        self.grades = grades or {}

    @property
    def full_name(self):
        return f"{self.last_name} {self.first_name}{(" "+self.patronymic) if self.patronymic else ""}"

    @property
    def average_grade(self):
        total = 0
        count = 0
        for _, grade in self.grades.items():
            if grade is not None:
                total += grade
                count += 1
        return total/count if count else 0.

    def __repr__(self):
        return f"{self.full_name}, {self.specialty} {(self.term+1)//2} курс, средний балл {self.average_grade}"
