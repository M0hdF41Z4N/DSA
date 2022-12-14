# Implementation of Circular Linked List
# Using Singly Linked List

class Node:
    def __init__(self,val):
        self.data = val
        self.next = None
    
    
    
class CircularLinkedList:
    def __init__(self):
        self.tail = None

    # Function to check if List is empty
    def isEmpty(self):
        return self.tail == None
    
    # Function to add element in front of List    
    def addFront(self,key):
        new_node = Node(key)
        if self.isEmpty() :
            self.tail = new_node
            new_node.next = self.tail
            
        else:
            new_node.next = self.tail.next
            self.tail.next = new_node
            
            
    # Function to add element at end of List
    def append(self,key):
        new_node = Node(key)
        if self.isEmpty() :
            self.tail = new_node
            new_node.next = self.tail
        else:
            new_node.next = self.tail.next
            self.tail.next = new_node
            self.tail = new_node
    
    # Function to search element
    def search(self,item):
        if self.isEmpty():
            return False
        trav = self.tail.next
        while trav :
            if trav.data == item:
                return trav
            trav = trav.next
            if trav == self.tail.next:
                break
        return False
        
    # Function to add element after a node of List
    def addAfter(self,data,key):
        if self.isEmpty():
            return "List is Empty"
        else:
            if self.tail.data == data:
                self.append(key)
            elif self.tail.next == data:
                self.addFront(key)
            else:
                if self.search(data):
                    prev = self.search(data)
                    new_node = Node(key)
                    new_node.next = prev.next
                    prev.next = new_node
                else:
                    return "Item not found"
    
    # Function to traverse through list
    def traverse(self):
        if self.isEmpty():
            return "List is Empty"
        trav = self.tail.next
        while trav :
            print(trav.data,end = " -> ")
            trav = trav.next
            if trav == self.tail.next:
                break
        print("\n")

    # Function to delete the front of list
    def deleteFront(self):
        front = self.tail.next
        data = front.data
        self.tail.next = front.next
        return data

    # Function to delete node
    def deleteNode(self,key):
        if self.tail.next.data == key:
            return self.deleteFront()
        else:
            curr = self.tail.next
            prev = curr
            while curr.next:
                prev = curr
                curr = curr.next
                if curr.data == key:
                    break
                elif curr.next == self.tail.next:
                    return "Node % not found" % key
            prev.next = curr.next
            data = curr.data
            return data



        



# Driver Code

l = CircularLinkedList()
for i in range(5):
    l.addFront(i)
l.append(5)
l.traverse()
print(l.addAfter(55,10))
l.traverse()
l.addAfter(2,10)
l.addAfter(4,11)
l.addAfter(5,12)
l.traverse()



