class Graph:

    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges
        self.matrix = []

    def adjacencyMatrix(self):
        for i in range(self.vertices):
            self.matrix.append([])
            for j in range(self.vertices):
                self.matrix[i].append(0)
        for i in range(self.edges):
            print("Введите номера смежных вершин")
            u = int(input())
            v = int(input())
            u = u - 1
            v = v - 1
            self.matrix[u][v] = self.matrix[v][u] = 1
        print("Матрица смежности:")
        return self.matrix

    def adjacencyList(self):
        adjacencyList = {}
        for i in range(self.vertices):
            adjacencyList.setdefault(i, [])
            for j in range(self.vertices):
                if self.matrix[i][j] == 1:
                    adjacencyList.get(i).append(j)
        return adjacencyList

    def addNote(self):
        for i in range(self.vertices):
            self.matrix[i].append(0)
        self.vertices = self.vertices + 1
        newNote = []
        for i in range(self.vertices):
            newNote.append(0)
        self.matrix.append(newNote)
        return self.matrix

    def deleteNote(self):
        self.vertices = self.vertices - 1
        v = int(input("Введите номер вершины")) - 1
        self.matrix.pop(v)
        for i in range(self.vertices):
            self.matrix[i].pop(v)
        return self.matrix

    def addArc(self):
        self.edges = self.edges + 1
        u = int(input("Введите номер вершины")) - 1
        v = int(input("Введите номер вершины")) - 1
        self.matrix[u][v] = self.matrix[v][u] = 1
        return self.matrix

    def deleteArc(self):
        self.edges = self.edges - 1
        u = int(input("Введите номер вершины")) - 1
        v = int(input("Введите номер вершины")) - 1
        self.matrix[u][v] = 0
        self.matrix[v][u] = 0
        return self.matrix

    def printGraph(self, matrix):
        for i in range(self.vertices):
            print(matrix[i])


def main():
    vertices = int(input("Введите количество вершин"))
    edges = int(input("Введите количество ребер"))
    graph = Graph(vertices, edges)
    graph.printGraph(graph.adjacencyMatrix())

    graph.printGraph(graph.adjacencyList())
    print(graph.addNote())
    print(graph.deleteNote())
    print(graph.addArc())
    print(graph.deleteArc())

if __name__ == "__main__":
    main()