
import time


def fibonachi1(number):
    array = {1 : 1, 2: 1}
    
    def realFIbo(number):
        if number in array:
            return array[number]
        
        array[number] = realFIbo(number-1) + realFIbo(number-2)
        return array[number]
    
    return realFIbo(number)

startTime = time.time()
print(fibonachi1(5));        
endTime = time.time()
print(endTime-startTime)        
    
# fibonachi 1번 메모이제이션 방법


def fibonachi2(number):
    if number <= 2:
        return 1
    memo = {1: 1, 2:1}
    for i in range(3, number+1):
        memo[i] = memo[i-1] + memo[i-2]
    
    return memo[number]

startTime = time.time()
print(fibonachi2(5))
endTime = time.time()
print(endTime-startTime)    


##  fibonachi 2번 반복문 메모이제이션 방법



def fibonachi3(number):
    if number <= 2:
        return 1
    
    a,b= 1, 1
    for i in range(3, number+1):
        sum = a + b
        a = b
        b = sum
    
    return b

startTime = time.time()
print(fibonachi3(5))
endTime = time.time()
print(endTime-startTime)    


## fibonachi 3번 반복문


# def fibonachi2(number):
#     if number <= 2:
#         return 1
    
#     return fibonachi2(number-1) + fibonachi2(number+2)


# print(fibonachi2(5))

## 해당 방법은 maximum stack exceed로 오류가 생김 이것은 자바스크립트랑 다른 점
