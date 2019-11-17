class Graph:

    def __init__(self, size):
        self.size = size
        self.matrix = []

    def adjacencyMatrix(self):
        for i in range(self.size):
            self.matrix.append([])
            for j in range(self.size):
                value = int(input())
                if value == 0 or value == 1:
                    self.matrix[i].append(value)
        print("Матрица смежности:")
        return self.matrix

    def adjacencyList(self):
        adjacencyList = {}
        for i in range(self.size):
            adjacencyList.setdefault(i, [])
            for j in range(self.size):
                if self.matrix[i][j] == 1:
                    adjacencyList.get(i).append(j)
        return adjacencyList

    def incidenceMatrix(self):

        return

    def listOfArcs(self):

        return



def main():
    size = int(input("Введите размер матрицы:"))
    graph = Graph(size)
    print(graph.adjacencyMatrix())
    print(graph.adjacencyList())


if __name__ == "__main__":
    main()
