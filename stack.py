class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.arr = []

    def push2(self, number):
        if self.size > self.capacity:
            raise IndexError('out of range')

        self.arr.append(number)
        self.size += 1
        return self.arr
    
    def isEmpty2(self):
        return True if self.size == 0 else False
    
    def pop2(self):
        if self.size < 0:
            raise IndexError('out of range')
        
        del self.arr[len(self.arr)-1]
        self.size -= 1
        return self.arr
    
    def remove2(self, number):
        if self.size < 0:
            raise IndexError('out of range')
        
        index = self.arr.index(number)
        del self.arr[index]
        self.size -= 1
        return self.arr

    def __str__(self):
        return f"{self.arr}"



stack = Stack(10)
stack.push2(5)
stack.pop2()
for i in range(10):
    stack.push2(i)

print(stack)

stack.remove2(5)
print(stack)
print(stack.isEmpty2())
