
# # 문제가 발생할 수 있는 코드를 묶어서 예외를 잡아주기 위한 구역
# try:
#     operand_A = int(input('a :'))
#     operand_B = int(input('b :'))

#     print(f'몫 : {operand_A//operan_B}, 나머지 : {operand_A % operand_B}')

# # 실제로 문제가 발생했을 때 어떻게 처리할지 정하는 구역
# except ZeroDivisionError:
#     print('0으로 나누는건 허용되지 않습니다.')
# except ValueError:
#     print('정수를 입력하세요')
# except BaseException as exception:
#     print(exception)



a = 100 / 0
print(a)
