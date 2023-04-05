class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SLL:
    def __init__(self):
        self.head = None

    def AtEnd(self, newdata):
        NewNode = Node(newdata)
        if self.head is None:
            self.head = NewNode
            return

        tail = self.head

        while tail.next:
            tail = tail.next
        tail.next = NewNode

    def AtStart(self, newdata):
        NewNode = Node(newdata)
        NewNode.next = self.head
        self.head = NewNode

    def Inbetween(self, middle_node, newdata):
        if middle_node is None:
            print('The Mentioned Node Does Not Exist')
            return

        NewNode = Node(newdata)
        NewNode.next = middle_node.next
        middle_node.next = NewNode

    def DeleteNode(self, RemoveData):
        HeadValue = self.head
        if HeadValue is not None:
            if HeadValue.data == RemoveData:
                self.head = HeadValue.next
                HeadValue = None
                return
            while HeadValue is not None:
                if HeadValue.data == RemoveData:
                    break
                prev = HeadValue
                HeadValue = HeadValue.next
            if HeadValue == None:
                return
            prev.next = HeadValue.next
            HeadValue = None

    def getCount(self):
        tmp = self.head
        count = 0

        while tmp:
            count += 1
            tmp = tmp.next
        return count

    def listprint(self):
        output = self.head
        while output is not None:
            print(output.data)
            output = output.next


list1 = SLL()
list1.head = Node('Mon')
e2 = Node('Tues')
e3 = Node('Wed')

list1.head.next = e2
e2.next = e3

list1.AtEnd('Thurs')
list1.AtEnd('Fri')
list1.AtStart('Sat')
list1.Inbetween(list1.head, 'Sun')
# list1.DeleteNode('Mon')

print('Count =', list1.getCount())
list1.listprint()
