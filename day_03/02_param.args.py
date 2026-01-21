
def make_greeting(name, year):
    """
   사람에게 현재 연도를 바탕으로
   나이를 알려주는 문자열을 변환하는 함수
    
    :param name: 사람
    :param year: 출생연도
    """

    return f'Hello,{name}!!! You are {2026-year+1} years old.'


# positional arguments : 매개변수의 순서에 맞춰서 인자를 전달해버리는 방법 (순서를 맞춰서 데이터 넣어주기 )
print(make_greeting('chaewon','1900'))
print(make_greeting('1900','chaewon'))

#keyword argument: 매개변수의 이름을 바탕으로 인자를 전달하는 방법
print(make_greeting(year=1900, name='chaewon'))

#default parameter : 매개변수에 기본값을 미리 할당하는 방법
def make_greeting(name='Anon',year=2025):
    return f'Hello, {name}!!! You are {2026 - year + 1} years old.'

print(make_greeting())
print(make_greeting(name='alex'))
print(make_greeting('brad'))
print(make_greeting(year=1900))
# print(make_greeting(year=1000,'alex')) # bad_case !!!!!!!!

#  bad case
#=>print(make_greeting(year=1000,'alex'))

def calculate_sum(*args):
    return sum(args)

#bad case
def print_movie_info(*args):
    print(args[0])
    print(args[1])
    print(args[2])

#good case
def movie_info(name,actors,director):
    print(name([0]))
    print(actors([2]))
    print(director([4]))
