class stack: 
    def __init__(self):
        self.arr = []
        self.size = 0
        
    def push(self, number):
        if(len(self.arr) > 10):
         raise MemoryError('stack exceed memory')

        self.arr.append(number)
        self.size += 1
        return self.arr
    
    def pop2(self):
        if len(self.arr) == 0:
         raise IndexError('Stack is empty, cannot pop')

        del self.arr[-1]
        self.size -= 1
        return self.arr
    
    def get_size(self):
        return self.size

    def isEmpty(self):
        if(self.size > 0):
            return False
        else:
            return True
        
    def __str__(self):
        return f"stack({self.arr})"


s2 = stack()

for i in range(10):
    i += 1
    s2.push(i)

print(s2)

s2.pop2()

print(s2)

del s2.arr[0:8:2]
s2.pop2()
print(s2)    
