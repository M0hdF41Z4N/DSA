# Implementation of Circular Linked List
# Using Singly Linked List

class Node:
  def __init__(self,val):
    self.data = val
    self.next = none
    
    
    
class CircularLinkedList:
  def __init__(self):
    self.tail = None
    
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
                trav = self.tail.next
                new_node = Node(key)
                while trav :
                    if trav.data == data:
                        break
                    elif trav.data == self.tail.next:
                        return "Item not found"
                    trav = trav.next
                new_node.next = trav.next
                trav.next = new_node
            
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
    
