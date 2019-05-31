class Matrix(object):
    def __init__(self, matrix_string):
        self.matrix = matrix_string.split("\n")
        print(self.matrix)

    def row(self, index):
        return[int(i) for i in self.matrix[index-1].split(" ")]

    def column(self, index):
        empty_list = []

        for string in self.matrix:
            list_of_lists = []
            list_of_lists.append(string.split(" "))
            for item in list_of_lists:
                empty_list.append(item[index-1])

        return[int(i) for i in empty_list]
