# import random

# random=random.randint(0,1)
# if random==0:
#     print("head")
# else:
#     print("tail")

# names=names_string.split(",")

# import random
# num_list=len(names)
# random_choice=random.randint(0,num_list -1)
# p=names[random_choice]
# print(p)

# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

# dirty_dozen = [fruits, vegetables]

# print(dirty_dozen[1][1])
# print(dirty_dozen)
# print(dirty_dozen[0])
# print(dirty_dozen[1])

# print(dirty_dozen[1][2])
# print(dirty_dozen[1][3])



import random
option=["rock", "paper","scissor"]

user_choice=input("choose rock, paper or scissor")
comp_choice=random.choice(option)

print(f"you choose,{user_choice}")
print(f"computer choose,{comp_choice}")

if user_choice==comp_choice:
    print("its a tie")
elif user_choice=="rock" and comp_choice=="scissor":
    print("you won")
elif user_choice=="scissor" and comp_choice=="paper":
    print("you won")    
elif user_choice=="paper" and comp_choice=="rock":
    print("you won")
else:
    print("computer won")
    






    