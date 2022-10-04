#1  LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers *if* both numbers are even,
#  but returns the greater if one or both numbers are odd
# lesser_of_two_evens(2,4) --> 2
# lesser_of_two_evens(2,5) --> 5

# def lesser_of_two_evens(a,b):

#     if a%2==0 and b%2==0:
#         print(min(a,b))
#     else:
#         print(max(a,b))

# lesser_of_two_evens(2,4)
# lesser_of_two_evens(2,5)



#2 MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False
# makes_twenty(20,10) --> True
# makes_twenty(12,8) --> True
# makes_twenty(2,3) --> False

# def makes_twenty(n1,n2):
#     sum = n1+n2
#     return sum == 20 or n1 == 20 or n2 ==20

# print(makes_twenty(12,8))
# print(makes_twenty(20,10))
# print(makes_twenty(2,3))



#3 OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name  
# old_macdonald('macdonald') --> MacDonald    
# Note: `'macdonald'.capitalize()` returns `'Macdonald'`

# def old_macdonald(name):
    
#     letter = [letter for letter in name]
#     capital0=letter[0].capitalize()
#     capital3=letter[3].capitalize()
#     letter[0]=capital0
#     letter[3]=capital3

#     return "".join(letter)

# def old_macdonald(name):
#     if len(name) > 3:
#         return name[:3].capitalize() + name[3:].capitalize()
#     else:
#         return 'Name is too short!'


# print(old_macdonald('macdonald'))



#4 MASTER YODA: Given a sentence, return a sentence with the words reversed
# master_yoda('I am home') --> 'home am I'
# master_yoda('We are ready') --> 'ready are We'

# def master_yoda(name):
    
#     letter = list(name.split(" "))
#     letter.reverse()
    
#     return " ".join(letter)

# print(master_yoda('I am home'))
# print(master_yoda('We are ready'))



#5 FIND 33: 
# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
#     has_33([1, 3, 3]) → True
#     has_33([1, 3, 1, 3]) → False
#     has_33([3, 1, 3]) → False

# def has_33(list):
#     for i in range(0, len(list)-1):
#         if list[i:i+2] == [3,3]:
#             return True
#     return False

# print(has_33([1, 3, 3]))
# print(has_33([1, 3, 1, 3]))
# print(has_33([3, 1, 3]))


#6 PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
# paper_doll('Hello') --> 'HHHeeellllllooo'
# paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'

# def paper_doll(name):

#     new_list=[]
#     for letter in name:
#         for i in range(3):
#             new_list.append(letter)
    
#     return "".join(new_list)

# def paper_doll(text):
#     result = ''
#     for char in text:
#         result += char * 3
#     return result

# print(paper_doll('Hello'))
# print(paper_doll('Mississippi'))



#7 SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.
# summer_69([1, 3, 5]) --> 9
# summer_69([4, 5, 6, 7, 8, 9]) --> 9
# summer_69([2, 1, 6, 9, 11]) --> 14

# def summer_69(list):
#     sum = 0
#     for i in range(len(list)):
#         if 6 in list:
#             if i in range((list.index(6)), (list.index(9))+1):
#                 continue
#         sum = sum+list[i]
#     return sum

# def summer_69(arr):
#     total = 0
#     add = True
#     for num in arr:
#         while add:
#             if num != 6:
#                 total += num
#                 break
#             else:
#                 add = False
#         while not add:
#             if num != 9:
#                 break
#             else:
#                 add = True
#                 break
#     return total

# def spy_game(nums):

#     code = [0,0,7,'x']
    
#     for num in nums:
#         if num == code[0]:
#             code.pop(0)   # code.remove(num) also works
       
#     return len(code) == 1

# print(summer_69([1, 3, 5]))
# print(summer_69([4, 5, 6, 7, 8, 9]))
# print(summer_69([2, 1, 6, 9, 11]))



#8 SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
# spy_game([1,2,4,0,0,7,5]) --> True
# spy_game([1,0,2,4,0,5,7]) --> True
# spy_game([1,7,2,0,4,5,0]) --> False

# def spy_game(list):

#     length=len(list)
#     if 7 in list[2:]:            
#         for i in range(2,length):
#                 if list[i] == 7:
#                     if list[i-1] == 0 and list[i-1] == list[i-2]:
#                         print(True)
#                     else:
#                         print(False)
#     else:
#         print(False)

# spy_game([1,2,4,0,0,7,5])
# spy_game([1,0,2,4,0,5,7])
# spy_game([1,7,2,0,4,5,0])
