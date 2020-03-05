class School:
    def __init__(self):
        self.students = {}

    def add_student(self, name, grade):
        if grade in self.students:
            self.students[grade].append(name)
        else:
            self.students[grade] = [name]

    def roster(self):
        result = []
        grades = list(self.students.keys())
        grades.sort()
        for grade_number in grades:
            for student in self.grade(grade_number):
                result.append(student)
        return result

    def grade(self, grade_number):
        result = []
        if grade_number in self.students:
            result = self.students[grade_number]
            result.sort()
        return result
