#  Doubly Linked List Implementation



class Node:
    def __init__(self,val):
        self.data = val
        self.next = None
        self.prev = None

class DoublyLinkedList:


    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        #self.travIter = None

    
    def insert(self,key,item):
        if self.isEmpty():
            return "List is Empty"
        new_node = Node(item)
        if self.head.data == key:
            self.insertAtBeg(item)
        elif self.tail.data == key:
            self.append(item)
        else:
            trav = self.head
            while trav.next or trav.next != key:
                trav =  trav.next
            if trav.next == key:
                new_node.next = trav.next.next
                new_node.prev = trav.next
     
    def clear(self):
        trav = self.head
        while trav:
            next = trav.next
            trav.data = trav.prev = trav.next = None
            trav = next

        self.head = None
        self.tail = None
        trav = None
        self.size = 0



    def __len__(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def delete(self):
        pass

    def append(self,item):
        new_node = Node(item)
        if self.isEmpty():
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def insertAtBeg(self,item):
        if self.isEmpty():
            self.head = self.tail = Node(item)

        else:
            new_node = Node(item)
            new_node.next = self.head
            self.head.prev = new_node
            self.head = self.head.prev
        self.size += 1

    def insertAt(self,index,item):
        
        if index < 0 :
            return "List index out of range"
        
        elif index > self.size :
            return "List index out of range"
        
        new_node = Node(item)
        
        if index == 1:
            self.insertAtBeg(item)
        
        else:
            trav = self.head
            for i in range(1,index-1):
                trav = trav.next

            new_node.prev = trav.prev
            new_node.next = trav.next
            trav.next = new_node

        self.size += 1



    def peek(self):
        return self.head.data

    def peekLast(self):
        return self.tail.data


    def indexOf(self,item):
        index = 0 
        trav = self.head

        if item is None:
            while trav:
                if trav.data is None:
                    return index
                trav = trav.next
                index += 1

        else:
            while trav:
                if trav.data == item:
                    return index
                trav = trav.next
                index += 1

        return -1

    def removeFirst(self):
        if self.isEmpty():
            return -1

        else:
            data = self.head.data
            self.head = self.head.next
            self.size -= 1

        if self.isEmpty():
            self.tail = None

        # Memory Cleanup
        else:
            self.head.prev = None

        return data

    def __remove__(self,node):
        if node.prev == None:
            return self.removeFirst()

    def removeLast(self):
        if self.isEmpty():
            return "List is Empty"
        else:
            data = self.tail.data
            self.tail = self.tail.prev
            # Memory Cleanup
            self.tail.next = None
            self.size -= 1
        return data

    def removeAt(self,index):
        if index <= 0 or index > self.size:
            return "List Index out of range"

        # Search from begining
        if index < self.size // 2:
            i = 0
            trav = self.head
            while i != index :
                i += 1
                trav =  trav.next

        # Search from End
        else:
            i = self.size-1
            trav = self.tail
            while i != index:
                i -= 1
                trav = trav.prev

        self.size -= 1

    def remove(self,item):
        trav = self.head

        if item is None:
            while trav:
                if trav.data is None:
                    self.__remove__(trav)
                    return True

                trav = trav.next

        else:
            while trav:
                if trav.data == item:
                    self.__remove__(trav)
                    return True

                trav =  trav.next
            self.size -= 1 

        return False
    
    def traverse(self):
        if self.head == None:
            return "List is Empty"
        trav = self.head
        while trav :
            print(trav.data,end=" -> ")
            trav = trav.next
        print("\n")
        


# Driver Code

DB = DoublyLinkedList()

DB.traverse()
DB.append(1)
DB.append(2)
DB.append(9)
DB.append(8)
DB.append(7)
DB.traverse()
print(DB.removeLast())
DB.traverse()
print(DB.removeLast())
DB.insertAt(2,888)
DB.traverse()
DB.removeFirst()
DB.traverse()
DB.insertAtBeg(777)
DB.traverse()
print(DB.peek())
print(DB.peekLast())
print(DB.removeLast())
DB.traverse()
DB.insert(2,3)
DB.traverse()
DB.remove(2)
DB.traverse()
