class Node:

    def __init__(self, data):
        self.rChild = None
        self.lChild = None
        self.data = data

    def insert(self, value):
        if value < self.data:
            if self.lChild is None:
                self.lChild = Node(value)
            else:
                self.lChild.insert(value)
        elif value > self.data:
            if self.rChild is None:
                self.rChild = Node(value)
            else:
                self.rChild.insert(value)

    # Обратный обход
    def print_tree(self):
        if self.lChild:
            self.lChild.print_tree()
        print(self.data),
        if self.rChild:
            self.rChild.print_tree()

    # Прямой обход
    def pre_order(self):
        print(self.data)
        if self.lChild:
            self.lChild.pre_order()
        if self.rChild:
            self.rChild.pre_order()

    # Центрированный обход
    def post_order(self):
        if self.lChild:
            self.lChild.post_order()
        if self.rChild:
            self.rChild.pre_order()
        print(self.data)

def main():
    root = Node(12)
    root.insert(6)
    root.insert(14)
    root.insert(3)
    root.insert(8)
    # root.print_tree()
    # root.pre_order()
    root.post_order()



if __name__ == "__main__":
    main()
