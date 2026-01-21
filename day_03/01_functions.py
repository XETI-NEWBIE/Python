
def make_sum(x,y):
    result = x + y
    return result


print(make_sum(1,2))
print()

#재사용가능하게 묶어두는 놈이 함수임

def add_interest(money, rate):
    money += money * (rate / 100)
    return money

print(add_interest(100,4.2))
print(100+(100*(4.2/100)))
print(add_interest(25000, 4.11))
print(25000+(25000*(4.11/100)))

#나중에 가면 갈수록 OOP / 추상화의 개념이 중요해질것 !!!!!!!

print(add_interest(100,4.2))
print(add_interest(25000,4.11))

# 화면에 출력하는 함수 
def print_greeting(name):
    print(f'Hello, {name}!!!')

# 호출한 곳으로 값을 반환하는 함수
def make_greeting(name):
    return f'Hi, {name}!!!'

print(print_greeting('chaewon'))
print(make_greeting('chaewon'))
