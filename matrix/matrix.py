class Matrix:
    def __init__(self, matrix_string):
        self.matrix = []
        cont = 0
        for i in matrix_string.split('\n'):
            self.matrix.append([])
            for j in i.split(' '):
                self.matrix[cont].append(int(j))
            cont += 1

    def row(self, index):
        return self.matrix[index - 1]

    def column(self, index):
        resp = []
        for i in self.matrix:
            resp.append(i[index - 1])
        return resp
