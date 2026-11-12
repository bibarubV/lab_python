#!/usr/bin/env python3

class Student:
    __id = 0

    def __init__(self, last_name, first_name, patronymic=None):
        self.last_name = last_name
        self.first_name = first_name
        self.patronymic = patronymic
        self.id = self.__id

        self.__id += 1
