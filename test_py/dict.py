my_dict_1 = {}
my_dict_2 = {'key': 'value'}
my_dict_3 = {'apple':12, 'list':[1,2,3]}

print(my_dict_1) #{}
print(my_dict_2) #{'key': 'value'}
print(my_dict_3) #{'apple': 12, 'list': [1, 2, 3]}

my_dict = {'apple':12, 'list':[1,2,3]}

#추가
my_dict['banana'] = 50
print(my_dict) #{'apple': 12, 'list': [1, 2, 3], 'banana': 50}

#변경
my_dict['apple'] = 100
print(my_dict) #{'apple': 100, 'list': [1, 2, 3], 'banana': 50}  

print(my_dict)

# students = {
#     '김철수' : {
#         'age' : 30
#         'address' : {
#             ' '
#         }
#     },
#     '이영희' : {
#         'age' : 25
#         'address' : {
#             'city' : 'Seoul'
#             'zip' : '123-456'
#         }
#     }
# }