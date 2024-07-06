#!/usr/bin/env python3
# Author ID: Harsahir Singh (hs100)

class Student:
    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.courses = {}

    def displayStudent(self):
        print('Student Name: ' + self.name)
        print('Student Number: ' + self.number)

    def addGrade(self, course, grade):
        self.courses[course] = grade

    def displayGPA(self):
        if len(self.courses) == 0:
            print('No courses added yet. GPA cannot be calculated.')
            return
        gpa = sum(self.courses.values()) / len(self.courses)
        print('GPA of student ' + self.name + ' is ' + str(gpa))

# Example usage:
if __name__ == '__main__':
    student1 = Student('John', '013454900')
    student1.addGrade('uli101', 4.0)
    student1.addGrade('ops245', 3.5)
    student1.addGrade('ops445', 3.0)

    student1.displayStudent()
    student1.displayGPA()
