
#문자열 : 문자들의 나열
hello_world = 'hello world!'
hello_world = "hello world!"

#중첩 따옴표
quotations_1 = '따옴표 문자열 내부에 "큰따옴표"를 넣을 때'
quotations_2 = "쌍따옴표 문자열 내부에 '따옴표'를 넣을 때"

#escape sequence : 특수문자 표현
escape_seq = 'Hello, my name \tis \nJeeho Park.'
print(escape_seq)
escape_seq = '따옴표 내부의 따옴표는 \'탈출\'시켜라'
print(escape_seq)

#String Interpolation : f-string
name = 'Jeeho Park'
greeting = f'hello, {name}!!!'
print(greeting)

a = 2
b = 3
result = f'{a} + {b} = { a + b }'
print(result)

#indexing / slicing (인덱스를 바탕으로 _ 잘라서 새로운 문자열을 만든다)

#indexing : 문자열의 특정 위치에 접근
print(name[4]) # o
print(name[8]) # r

# slicing : 문자열의 특정 구간을 잘라서 새로운 문자열 생성
# [start : end : step ] 이라는 것을 기억해야
print(name[5:])
print(name[:5])
print(name[5:7])
print('result: ' + name[5:7:-1])
print('result: ' + name[7:5:-1])
