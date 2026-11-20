#!/usr/bin/env python3

class FacultyError(Exception):
    pass

class StudentNotFoundError(FacultyError):
    pass

class DisciplineNotFoundError(FacultyError):
    pass

class DepartmentNotFoundError(FacultyError):
    pass

class StudentNotEnrolledError(FacultyError):
    pass

class DisciplineNotAvailableError(FacultyError):
    pass

class InvalidGradeError(FacultyError):
    pass

class NotAllDisciplinesPassedError(FacultyError):
    pass

class SpecialtyNotSupportedError(FacultyError):
    pass
