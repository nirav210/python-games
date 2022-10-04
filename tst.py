
# list = [ int(input())**2 for x in range(0,4)]
# print(list, end='')

# -------------------------------------------------------------

# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)

# n = int(input("Enter any number:"))
# print(f'Factorial of {n} is {factorial(n)}.')

# -------------------------------------------------------------

# list = [1,4,5,2,7,3,8]

# def check_even_list(list):

#     print([ num for num in list if num % 2 == 0])

# print(check_even_list(list))

# -------------------------------------------------------------

# list = [1,5,7,3]

# def check_even_list(list):
    
#     for num in list:
#         if num % 2 == 0:
#             return True
    
# print(check_even_list(list))

# -------------------------------------------------------------

# work_hours = [('abc',200), ('def',500), ('ghi',900)]

# def max_hour_employee(work_hours):
    
#     current_max = 0
#     employee_name = ''

#     for employee,hour in work_hours:
#         if hour > current_max:
#             current_max = hour
#             employee_name = employee
#         else:
#             pass

#     return(employee_name,current_max)

# print(max_hour_employee(work_hours))

# -------------------------------------------------------------

# from random import shuffle
# def shuffle_list(list):
#     shuffle(list)
#     return list

# def player_guess():

#     guess=''
#     while guess not in ['0' ,'1' ,'2']:
#         guess = input("Pick a number : 0, 1, 2: ")

#     return int(guess)

# def result(list, guess):

#     if list[guess] == 'O':
#         print("winner")
#     else:
#         print("losser")
#     print(list)


# list = ['', '', 'O']
# a=shuffle_list(list)
# b=player_guess()
# result(a,b)

# -------------------------------------------------------------

# def only_even(*args):
    
#     return [i for i in args if i%2 == 0]

# print(only_even(2,4,6,3,5,2,1,5,8))


# -------------------------------------------------------------

# def myfunc(str):
#     mix=[]
#     for i in range(len(str)):
#         if i%2 == 0:
#             mix.append(str[i].lower())
#         else:
#             mix.append(str[i].upper())

#     return ''.join(mix)

# print(myfunc('Anthropomorphism'))

# -------------------------------------------------------------
a = ' '

def abc():
    return a == ' '

print(abc())

if not abc():
    print('abc')