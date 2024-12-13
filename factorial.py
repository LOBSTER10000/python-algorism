import time

## factorial 

def factorial1(number):
    if number <= 1:
        return 1
    
    return number * factorial1(number-1)

start = time.time()
print(factorial1(30))
endtime = time.time()
print(endtime- start)
## 가장 비효율적인 재귀 형식


def factorial2(number):
    if number <= 1:
        return 1
    memo = {1 : 1}
    def realFacto(number):
        if number in memo:
            return memo[number]
        
        memo[number] = number * realFacto(number-1)
        return memo[number]
    
    return realFacto(number)


start = time.time()
print(factorial2(30))
endtime = time.time()
print(endtime- start)

## 기본적인 메모이제이션을 활용한 재귀 형식


def factorial3(number):
    a = 1
    for i in range(2, number+1):
        a = a*i
    
    return a

start = time.time()
print(factorial3(30))
endtime = time.time()
print(endtime- start)
