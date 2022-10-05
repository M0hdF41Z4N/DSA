#   Implementation of Dyanmic Array using static array

class Dynamic_Array:
    def __init__(self) -> None:
        self.array = []
        self.length = 0
        self.capacity = 0

    def add(self,item):
        if self.length+1 >= self.capacity:
            if self.capacity == 0: # checks if empty
                self.capacity = 1   
            else:   # other wise grow to power 2
                self.capacity *= 2
            self.array += [None] * (self.capacity-self.length) # pads with extra 0/null elements
        self.array[self.length] = item
        self.length += 1
        


    def is_empty(self):
        return self.size() == 0

    def size(self):
        return self.length

    def get(self,index):
        return self.array[index-1]

    def set(self,index,item):
        self.array[index-1] = item
        
    def clear(self):
        for i in range(self.length):
            self.array[i] = None
            self.length = 0

    def removeAt(self,position):
        # Python built-in function array.pop(index)
        new_array = []
        temp = self.length
        index = position-1
        if position < self.length :
            for i in range(temp):
                if i == index:
                    data = self.array[i]
                    self.length -= 1
                    continue
                else:
                    new_array.append(self.array[i]) # exception
            self.array = new_array
            return data
        else:
            return "Index Out of Range"
        


    def remove(self,item):
        # Python built-in function array.remove(item)
        for i in range(self.length):
            if self.array[i] == item:
                return self.removeAt(i+1)
        return -1




    def Display(self):
        if self.is_empty():
            print("Array is Empty")
        else:
            for i in range(self.length):
                print(self.array[i],end=" , ")
            print("\n")



# Driver Code

a = Dynamic_Array()
a.is_empty()
a.add(1)
a.add(2)
a.add(9)
a.add(14)
print(a.size())
a.Display()
print(a.get(3))
a.set(1,897)
a.Display()
print(a.size())
print(a.removeAt(1))
a.Display()
print(a.size())
print(a.remove(9))
a.Display()
a.clear()
a.Display()
