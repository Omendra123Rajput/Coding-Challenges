class Node():
    def __init__(self,value=None):
        self.value=value
        self.next=None

class SingleLL():
    def __init__(self):
        self.head=None
        self.tail=None
    def __iter__(self):
        node=self.head
        while node is not None :
            yield node
            node = node.next
    def insertSLL(self,value,loaction):
        newNode = Node(value)
        if self.head is None :
            self.head = newNode
            self.tail = newNode
        else:
            if loaction == 0 :
                newNode.next = self.head
                self.head = newNode
            elif loaction == 1 :
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < loaction - 1 :
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                newNode.next = nextNode
                tempNode.next = newNode
    def traversing(self):
        node = self.head
        if node is None:
            print('List is empty')
        else:
            
            while node is not None:
                print(node.value)
                node = node.next
                
    def deleteNode(self,location):

        if self.head == None:
            print('SLL is empty')
        else:
            if location == 0:
                if self.head == self.tail :
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            elif location == 1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = None
                    self.tail = node
            else:

                tempNode = self.head

                index = 0

                while index < location - 1:
                    tempNode = tempNode.next
                    index +=1
                nextNode = tempNode.next
                tempNode.next = nextNode.next
                
                    

                
                  
                  
                          


singlylinkedlist = SingleLL()
singlylinkedlist.insertSLL(1,0)
singlylinkedlist.insertSLL(2,1)
singlylinkedlist.insertSLL(2,1)
singlylinkedlist.insertSLL('hi',1)
singlylinkedlist.insertSLL('hello',2)

print([node.value for node in singlylinkedlist])

singlylinkedlist.deleteNode(1)
#singlylinkedlist.deleteNode(0)

print([node.value for node in singlylinkedlist])








