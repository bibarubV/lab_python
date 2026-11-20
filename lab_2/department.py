#!/usr/bin/env python3

from exceptions import DisciplineNotFoundError

class Department:
    __id = 0

    def __init__(self, name):
        self.id = Department.__id
        Department.__id += 1

        self.name = name
        self.courses = {}

    def add_course(self, discipline, specialty):
        self.courses[(discipline.id, specialty)] = discipline

    def remove_course(self, discipline, specialty):
        del self.courses[(discipline.id, specialty)]

    def teaches_course(self, discipline, specialty):
        return (discipline.id, specialty) in self.courses

    def get_discipline(self, discipline_id):
        for (discipline_id_, _), discipline in self.courses.items():
            if discipline_id_ == discipline_id:
                return discipline
        raise DisciplineNotFoundError("дисциплина '"+str(discipline_id)+"' не найдена")

    def __repr__(self):
        return f"Кафедра {self.name} ({self.id}), курсы: {self.courses}"

