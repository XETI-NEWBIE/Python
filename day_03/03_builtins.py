
numbers = [1,2,3,4,5]
print(numbers)
print(len(numbers))
print(max(numbers))
print(min(numbers))
print(sum(numbers))

print(max(1,2,3))
print(min(44,24,10))

#map
raw_input = input()
num_list = map(int, raw_input.split())
print(sum(num_list))

num_list = map(to_int_and_double_up(''), raw_input.split())
print(sum(num_list))