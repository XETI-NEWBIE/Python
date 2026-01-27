

def add_item_to_dict(dict, key, value):
    # 실습에서 요구하는 부분이 아래 두 줄이다
    # 핵심적인 function body 고려하기
    new_dict = dict.copy()
    new_dict.update({key:value})
    return new_dict

my_dict = {'name':'Alice', 'age' : 25 }

result = add_item_to_dict(my_dict, 'country', 'USA')

print(result)
