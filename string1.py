## 문자열 더하기

head = "Python"
tail = "is fun"

print(f"{head} {tail}")
print(head + tail)

## 문자열 곱하기

a = "python"

print(a*3)
# print(a**3) => 문자열은 제곱은 안된다

##############################

## 문자열 길이 구하기

c = 'life is too short'
print(len(c))

## 문자열 인덱싱과 슬라이싱

b = "Life is too short, You need Python"

print(b[3]) 
# print(b[시작인덱스:마지막인덱스-1:범위])


## 문자열 포맷팅
print("I eat %d apples" %3) #숫자 대입
print("I eat %s" % "apple") #문자 대입
print(f"I eat {3} apples") 

###############################################

##### 문자열 관련 함수들

## 1. 문자 개수 세기 (count)

a = "hobby" 
print(a.count('b')) # 해당 문자열에 개수가 몇개 있는지 확인


## 2. 위치 알려주기 (find)
a = "hobby"
print(a.find('b')) # 해당 문자열에 첫번째 문자열의 위치를 알려준다 없다면 -1을 반환한다

## 3. 위치 알려주기 (index)

a = "hobby"
print(a.index('b')) #없다면 오류를 반환한다

## 4. 문자열 삽입 (join)

a = ['a','b','c','d']
print(''.join(a)) # 리스트에서 해당 문자열을 삽입할 수 있다

## 5. 문자열 소문자를 대문자로 (upper)

a = "s"
print(a.isupper())  # 문자열이 대문자가 맞는지 확인
print(a.upper()) # 문자열을 대문자로 변경 

## 6. 문자열 대문자를 소문자로 (lower)

a = "S"
print(a.islower())
print(a.lower()) 

## 7. 왼쪽 공백 지우기 (lstrip)
## 7. 오른쪽 공백 지우기 (rstrip)
## 7. 양쪽 공백 지우기(strip)
a = " S string "

print(a.strip())

## 8. 문자열 바꾸기 (replace)
a = 'Life is too short'
print(a.replace('too', 'not')) # 해당 문자열로 치환한다

## 9. 문자열 나누기 - split 

a = 'life is fun'
print(a.split()) ## 아무값도 넣지 않았을 시에는 공백은 기준으로 나눈다
print(a.split('i')) ## 문자열 값을 넣었을 때 해당 문자열을 기준으로 나눈다

# %% 
b = 'lifeisgood'
print(list(b)) ## javscript의 split처럼 하나씩 잘라서 list화 시키고 싶다면 list()로 사용
# %% 



