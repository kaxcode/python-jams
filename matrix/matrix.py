class Matrix(object):
    def __init__(self, matrix_string):
        self.matrix = matrix_string.split("\n")

    def row(self, index):
        return[int(i) for i in self.matrix[index-1].split(" ")]

    def column(self, index):
        return self.matrix
