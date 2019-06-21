class Matrix(object):
    def __init__(self, matrix_string):
        ms = matrix_string.split("\n")

        list_of_lists = []
        for x in ms:
            list_of_lists.append([int(i) for i in x.split(" ")])

        self.matrix = list_of_lists

    def row(self, index):
        return self.matrix[index-1]

    def column(self, index):
        column_list = []
        for item in self.matrix:
            column_list.append(item[index-1])

        return column_list
