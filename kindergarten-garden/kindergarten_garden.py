class Garden:
    def __init__(self, diagram, students=None):
        self.diagram = diagram.split('\n')
        self.groups_plants()
        if students is None:
            self.groups_students()
        else:
            students.sort()
            self.students = students

    def plants(self, student):
        result = []
        position = self.students.index(student) * 2
        for seccion in self.diagram:
            for letter in seccion[position:position + 2]:
                result.append(self.array_plants[letter])
        return result

    def groups_plants(self):
        self.array_plants = {
                'G': 'Grass',
                'C': 'Clover',
                'R': 'Radishes',
                'V': 'Violets'
        }

    def groups_students(self):
        self.students = [
            'Alice', 'Bob', 'Charlie', 'David',
            'Eve', 'Fred', 'Ginny', 'Harriet',
            'Ileana', 'Joseph', 'Kincaid', 'Larry'
        ]
