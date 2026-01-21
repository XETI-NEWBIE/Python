#dictionary
#사전과 같은 자료형
my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}
alex = {
    'first_name':'Alex',
    'last_name':'Rod',
    'born_at':1970,
    'age':55,
    'skills':['SS']
}

print(alex['first_name'])
print(alex['last_name'])


#set 
#집합과 같은 자료형. 중복 허용 안 함묘!!
primes = {2, 3, 5, 7, 11}
names = {'alex', 'brad' , 'chad' , 'alex', 'alex'}
print(names) #중복된 alex는 하나만 남음