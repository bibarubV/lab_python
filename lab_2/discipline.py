#!/usr/bin/env python3

class Discipline:
    __id = 0

    def __init__(self, name, term):
        self.id = Discipline.__id
        Discipline.__id += 1

        self.name = name
        self.term = term

    def __repr__(self):
        return f"Дисциплина '{self.name}', {self.term} семестр"
