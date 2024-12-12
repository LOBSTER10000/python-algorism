odd = [1,3,5,7,9]

# 리스트명 = [요소1, 요소2]

## 리스트의 요소를 삭제할 때 (del)

del odd[0]
print(odd)


## 리스트 요소 추가하기 (append)

odd.append(2)
print(odd)

## 리스트에 요소 추가하기 (insert)

odd.insert(0, 5) 
print(odd)

## 리스트 정렬하기 (sort)

odd.sort() ## 오름차순으로 정렬하기
print(odd)

sorted(odd, reverse=True) ## 내림차순으로 정렬하기
print(odd)

## 리스트 뒤집기 (reverse)

odd.reverse()
print(odd)

## index 반환 (index)

print(odd.index(5)) ## 해당 내역이 있는 인덱스를 반환한다, 없을시 오류 반환

## 리스트 요소 제거 (remove)

odd.remove(5) ## 리스트에서 첫번째로 나오는 X를 삭제하는 함수
print(odd)

## 리스트 요소 끄집어 내기 (pop)
odd.pop()
print(odd)

## 리스트 요소 확장하기 (extend)
odd.extend([4,10])
print(odd)

sorted(odd, reverse=True) ## 원본리스트는 변함 없음
odd.sort(reverse=True) ## 원본 리스트 변함
print(odd)



