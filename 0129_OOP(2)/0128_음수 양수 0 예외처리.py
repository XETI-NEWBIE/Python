
def check_number():
    try:
        # 아래 초기 코드는 result를 정의해주는 구문이 없어서 에러가 떴다. 
        # int(input()) 부분은 result에 따로 저장해주고, finally는 현재는 굳이 쓸 필요가 없다.
        # 그리고 매 print마다 input을 쓸 필요가 전혀 없다. result에서 미리 저장해뒀기 때문.......
        result = int(input('숫자를 입력해주세요 :'))
        if result > 0:
            print('양수입니다.')
        elif result == 0:
            print('0입니다.')
        else:
            print('음수입니다')
    except ValueError:
        print('잘못된 입력입니다.')
check_number()




# # 아래 함수를 수정하시오.
# def check_number():
#     try: 
#         # num = int(input('숫자를 입력해주세요 :'))
#         if result > 0:
#             print(input('양수입니다.'))
#         elif result == 0:
#             print(input('0입니다'))
#     except ValueError:
#         print('잘못된 입력입니다')
#     finally:
#         print(f'숫자를 입력하세요: {result}')
# check_number()

# # try-except
# try: 
#     result = 10 / 0
# except ZeroDivisionError:
#     print('0으로 나눌 수 없습니다')

# try:
#     num = int(input('숫자를 입력해주세요 :'))
# except ValueError:
#     print('그건 숫자가 아니에요..')