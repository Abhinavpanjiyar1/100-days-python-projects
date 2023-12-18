# student_heights=input().split()
# for n in range(0,len(student_heights)):
#     student_heights[n]=int(student_heights[n])
    
# total_height=0
# for height in student_heights:
#     total_height +=height
# print(f"the total height={total_height}") 
    
# total_student=0
# for student in student_heights:
#     total_student +=1
# print(f"the total student ={total_student}")  
     
# average_height = round(total_height/total_student)
# print(f"the average height is {average_height}")
  
  
  
  
# student_scores =input().split()
# for n in range(0, len(student_scores)):
#     student_scores[n]= int(student_scores[n])
    
# highest_score=0
# for score in student_scores:
#     if score>highest_score:
#         highest_score = score
# print(f"the highest score is {highest_score}")



# target = int(input())
# even_sum =0
# for target in range(2, target, 2):
#     even_sum+= target
# print(even_sum)    

#fizz buzz game
# for i in range(1,101):
#     if i % 3==0 and i % 5 == 0:
#         print("fizzbuzz")
#     elif i %3 == 0:
#         print("fizz")
#     elif i % 5 == 0:
#         print("buzz")
#     else:
#         print(i)               

import random
number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']  
letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                     'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 
                     'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                     'Z']
 
symbols = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', 
           '*', '(', ')', '<']

print("welcome to password generator")
n_letter =int(input("number of letter\n"))
n_number =int(input("number of numbers\n"))
n_symbol=int(input("number of symbol\n"))


#easy password


# password = ""
# for char in range(1, n_letter+1):
#     password+=random.choice(letter)
    
# for char in range(1, n_symbol+1):
#     password+=random.choice(symbols)
    
# for char in range(1, n_number+1):
#     password+=random.choice(number)
   
# print(password)
           
           



password_list =[]
for char in range(1, n_letter+1):
    password_list.append(random.choice(letter))
    
for char in range(1, n_symbol+1):
    password_list+=random.choice(symbols)
    
for char in range(1, n_number+1):
    password_list+=random.choice(number)
   
print(password_list)
random.shuffle(password_list)



password = ""
for char in password_list:
    password+= char
    
print(f"your password is {password}")    
    
    
    

        
    



           


    
    
      