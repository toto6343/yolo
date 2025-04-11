# 리스트
numbers = [1, 2, 3, 4, 5] # 정수 리스트
fruits = ["apple", "banana", "cherry"] # 문자열 리스트
mixed = [1, "hello", 3.14, True] # 다양한 자료형을 포함하는 리스트

# 리스트의 인덱싱과 슬라이싱
print(numbers[0]) # 1
print(fruits[-1]) # cherry
print(numbers[1:4]) # [2, 3, 4]

# 리스트 요소 변경
# numbers[0] = 100
# print(numbers)
# [100, 2, 3, 4, 5]

# 리스트 요소 추가
# numbers.append(6)
# print(numbers)
# [1, 2, 3, 4, 5, 6]

# numbers.insert(2, 99)
# print(numbers) 
# [1, 2, 99, 3, 4, 5]

# 리스트 요소 제거
# numbers.remove(5)
# print(numbers)
# [1, 2, 3, 4]

# a = numbers.pop()
# print(a)
# print(numbers)
# [1, 2, 3, 4]

#  리스트 길이 확인
print(len(numbers))
#  5

numbers.reverse()
print(numbers)

numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)

y = reversed(numbers)
print(y)

