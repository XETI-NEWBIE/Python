
# # list 자료형 : 0개 이상의 데이터를 저장할 때 사용

# alex = ['Alex', 'Rod', 'NYY']
# menus = ['Chicken', 'Pizza', 'Beer']
# print(menus)
# print(menus[0])  # Chicken
# print(menus[:2])
# print(menus[2:])
# print(menus[::-1])

# # mutable : 변경 가능한 자료형
# menus[1] = 'Pepperoni Pizza'
# print(menus)  # ['Chicken', 'Pepperoni Pizza', 'Beer']

# # 중첩 가능 : list 안에 list 를 넣을 수 있다
# # 알고리즘 문제 풀 때, 중첩 list는 진짜 쥰내 잘 쓸 수 있어야 한다 ㅋㅋ
# beers = ['Stella', 'Hoe', 'Cass', 'Terra']
# menus[2] = beers
# print(menus) 

# menus = ['Chicken', 'Pizza', ['Stella', 'Hoe', 'Cass', 'Terra', 0]]
# print(menus[2][1][0])  
# print(menus[2][-1][0])

# tuple 자료형 : list 와 거의 동일, 단 변경 불가능 (immutable)
# tuple은 대괄호 대신 소괄호 ()을 사용함
jeeho = ('Jeeho', 'Park', 0)
# immutable : 변경 불가능
# jeeho[0] = 'Jiho'  # 오류 발생

# tuple unpacking
first_name, last_name, age = jeeho

## python의 가장 큰 장점 중 하나 : swap이 매우 간단함
# swap
a=2
b=3
# 아래에서 b,a는 튜플임 (괄호가 생략된)
a,b=b,a

## 다른 불쌍한 언어들의 경우 .. 유유유유 (개귀찮띄)
a=2
b=3
temp=a
a=b
b=temp
print(a,b)

# warning
result = 100, # 끝에 쉼표가 한 개의 데이터를 가진 tuple을 만드는 행위 ㅋ
print(type(result))
print(result+1) # 오류 발생

# Django 를 할 때 특히 ...
# return render(),  # <- 요런 식으로 많이 사용함 (튜플 만들어져서 진짜 바로 에러남 ㅋㅋ)


# range 자료형 : 일정 규칙 가진 애들을 계속 뽑아내기 위힘
print(range(10))
print(range(5, 10))
print(list(range(5, 0, -1)))

