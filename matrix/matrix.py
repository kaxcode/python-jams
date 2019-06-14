class Matrix(object):
    def __init__(self, matrix_string):
        self.matrix = int(matrix_string.split("\n"))

    def row(self, index):
        return self.matrix[index-1].split(" ")

    def column(self, index):
        empty_list = []

        for string in self.matrix:
            list_of_lists = []
            list_of_lists.append(string.split(" "))
            for item in list_of_lists:
                empty_list.append(item[index-1])

        return empty_list
