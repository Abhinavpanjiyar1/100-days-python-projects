print('''
      =====[Shotgun]
 ,______________________________________
|_________________,----------._ [____]  ""-,__  __....-----=====
               (_(||||||||||||)___________/   ""                |
                  `----------' Krogg98[ ))"-,                   |
                                       ""    `,  _,--....___    |
                                               `/           """"
                                               ''')

print("welcome to Treasure Island. your mission is to find the treasure. ")
choice1=input("left" or"right").lower()
if choice1=="left":
    choice2=input("swim" or "wait").lower()
    if choice2=="wait":
        choice3=input('which door? Type "red" or "blue" or "yellow"')
        if choice3=="yellow":
            print("you won")
        else:
            print("game over")
    else:
        print("game over")                
else:
    print("Game over")
    
    
