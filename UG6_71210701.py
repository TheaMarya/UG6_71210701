class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def addElementHead(self, data):
        nNode = Node(data)
        if self.head is None:
            self.head = nNode
            self.tail = nNode
        else:
            nNode.next = self.head
            self.head.prev = nNode
            self.head = nNode
    
    def addElementTail(self, data):
        nNode = Node(data)
        if self.tail is None:
            self.tail = nNode
            self.head = nNode
        else:
            nNode.prev = self.tail
            self.tail.next = nNode
            self.tail = nNode
    
    def maju(self, n):
        c = self.head
        for i in range(n):
            if c is None:
                break
            c = c.next
        if c is not None:
            print(c.data)
            self.head = c
    
    def mundur(self, n):
        c = self.head
        for i in range(n):
            if c is None:
                break
            c = c.prev
        if c is not None:
            print(c.data)
            self.head = c





# Contoh input & output program:
linkedlist = LinkedList()
linkedlist.addElementHead("Jogja")
linkedlist.addElementHead("Jakarta")
linkedlist.addElementTail("Bali")
linkedlist.addElementTail("Bandung")

linkedlist.maju(2) #output: Bali
linkedlist.mundur(1) #output: Jogja
linkedlist.maju(5) #output: Bali
linkedlist.mundur(3) #output: Bandung