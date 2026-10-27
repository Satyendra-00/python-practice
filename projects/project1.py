#snake water gun game 
import random
dict={1:"snake",2:"water",3:"gun"}
user=int(input("enter you choice 1,2, 3 : "))
computer=random.choice([1,2,3])
print(f"you choose {dict[user]}\ncomputer choose {dict[computer]}")
if computer==user:
    print("its a draw")
else:
    if computer==1 and user == 2:
        print("you loose")
    elif computer==1 and user==3:
        print("you winn")
    elif computer==2 and user==1:
        print("you win ")
    elif computer==2 and user == 3:
        print("you loose")
    elif computer==3 and user==1:
            print("you loose")
    elif computer==3 and user==2:
            print("you win ")
    else:
         print("something wrong")