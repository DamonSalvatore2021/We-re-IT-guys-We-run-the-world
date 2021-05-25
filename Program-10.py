#Code starts complete the code
s=0
import random

for i in range(1,50):
    num1=random.randint(10,20)
    num2=random.randint(10,20)
    dn=num1-num2
    print("Please guess difference between two random numbers,to end the game guess 100")
    gn=int(input())
    diff = dn - gn
    if(-2<diff<2 and diff!=0 and i==1):
        print("Excellent")
        print("Game Quit after",i,"attempts")
        break
    elif(diff==0):
        print("Congratulations! You have guessed right")
        print("Game Quit after",i,"attempts")
        break
    elif(diff>=2 or diff<-2and gn!=100):
        print("You've guessed too high! Try again")
    elif(gn==100):
        print("Game Quit after",i,"attempts")
        break
    if(i>10):
        print("alert")
#Code Ends here