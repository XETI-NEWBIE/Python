
# my_list[4]->['hello','world','!!!']
# my_list[4][-1]->'!!!'

my_list = [ 1, 2, 3, 'Python', ['hello', 'world', '!!!']]
           
print(len(my_list)) #5
print(my_list[4][-1]) #!!!
print(my_list[-1][1][0]) #w

my_list = [1, 2, 3, 4, 5]
my_list[1] = 'two'
print(my_list) #[1, 'two', 3, 4, 5]

my_list = [1, 2, 3, 4, 5]
my_list[2:4] = ['three', 'four']
print(my_list) #[1, 2, 'three', 'four', 5]