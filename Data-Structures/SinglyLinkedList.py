# Implementation of Singly Linked List



class Node:
    # Constructor
    def __init__(self,data_val):
        self.data =  data_val
        self.next = None

class Linked_List:
    # Constructor
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def isEmpty(self):
        return self.head == None

    # Function to insert a Node after given node
    def insertAfter(self,key,data_val):
        new_node = Node(data_val)
        node = self.search(key)
        if node:
            new_node.next = node.next
            node.next = new_node
            self.length += 1
            return str(data_val)+" Inserted Successfully"
        else:
            return "Node %d not found" % key
        

    # Function to remove a node in list
    def remove(self,data_val):
        if self.head:
            if self.head.data == data_val:
                self.head = self.head.next

            elif self.tail.data == data_val:
                self.removeLast()

            else:
                current = self.head
                previous = current
                while current :
                    if current.data == data_val :
                        previous.next = current.next
                    previous = current
                    current = current.next
            self.length -= 1
        else:
            return "List is Empty Or Key not Found" 

    # Function to Search a Node in list
    def search(self,node):
        current = self.head
        while current :
            if current.data == node:
                return current
            current = current.next
        return False

    # Function to append a Node in list
    def append(self,data_val):
        new_node = Node(data_val)
        if self.isEmpty() :
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    # Function insert an element
    def insertAtBegining(self,data_val):
        new_node = Node(data_val)
        if self.isEmpty() :
            self.tail = self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    # Function to traverse the a node in list
    def traverse(self):
        copy = self.head
        while copy:
            print(copy.data,end=" -> ")
            copy = copy.next
        print("\n")
        

    # Function to an element
    def deleteAtGivenPosition(self,position):
        if position > self.size():
            return "List index out of range"
        elif position == 1:
            return self.removeFirst()
        elif position == self.size():
           return self.removeLast()
        else:
            i = 0
            curr = self.head
            prev = curr
            while i != position-1:
                i+=1
                prev = curr
                curr = curr.next
            data = curr.data
            prev.next = curr.next
            return data


    def peekFirst(self):
        return self.head.data

    def peekLast(self):
        return self.tail.data

    def size(self):
        return self.length

    def clear(self):
        pass

    def removeFirst(self):
        if self.isEmpty():
            return "List is Empty"
        else:
            data = self.head
            self.head = self.head.next
        return data

    # Find the 
    def removeLast(self):
        if self.isEmpty() :
            return "List is Empty"
        else:
            last = self.head
            prev = last
            while last.next:
                prev = last
                last = last.next
            data = last.data
            prev.next = last.next
            self.tail = prev
        return data

    # Find the index of particular value in the linked list
    def indexOF(self,key):
        i = 0
        trav = self.head
        while trav:
            i += 1
            if trav.data == key:
                return i
            trav = trav.next
        return -1


# Driver Code

l = Linked_List()
for i in range(50,60):
    l.insertAtBegining(i)
l.append(5)
l.append(3)
l.append(4)
l.append(1)
l.traverse()
print(l.insertAfter(33,7))
print(l.insertAfter(3,7))
l.traverse()
l.insertAtBegining(99)
l.traverse()
print(l.deleteAtGivenPosition(5))
l.traverse()
l.removeLast()
l.removeLast()
l.removeLast()
l.traverse()
