


# # 아래 클래스를 수정하시오.
# class StringRepeater:
    


# repeater1 = StringRepeater()
# repeater1.repeat_string(3, "Hello")


# class StringRepeater: 
#     def repeat_string(self, text):
#         if times < 4:
#             return ""
#         return self.text *times
#     repeater1 = StringRepeater()
# print(repeater1.repeat_string(3, "Hello"))




class StringRepeater:
    def repeat_string(int, text):
        if times < 4:
            return repeater1
repeater1 = StringRepeater()
print(repeater1.repeat_string(3, "Hello"))




# print(repeat_string('Hello'))

# class StringRepeater:
#     def __init__(self, text):
#         """반복할 문자열을 초기화합니다."""
#         self.text = str(text)

#     def repeat(self, times):
#         """문자열을 지정된 횟수만큼 반복하여 반환합니다."""
#         if times < 0:
#             return ""
#         return self.text * times

#     def repeat_with_separator(self, times, separator=" "):
#         """구분자를 포함하여 문자열을 반복합니다."""
#         if times <= 0:
#             return ""
#         # 리스트 컴프리헨션과 join을 사용하여 효율적으로 연결
#         return separator.join([self.text] * times)

# # --- 사용 예시 ---
# # 1. 객체 생성 
# repeater = StringRepeater("Python")

# # 2. 기본 반복 (* 연산자 활용)
# print(repeater.repeat(3))  # 출력: PythonPythonPython

# # 3. 구분자를 넣어 반복
# print(repeater.repeat_with_separator(3, separator="-"))  # 출력: Python-Python-Python

# # 4. 다른 문자열로 재사용
# hi = StringRepeater("Hi")
# print(hi.repeat(5))  # 출력: HiHiHiHiHi