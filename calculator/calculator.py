from .helpers import *


def calculator():

    while True :
        print("1 .Add\n 2. Subtract \n 3. Mul \n 4. Div \n 0. Quit")
        choice = int(input("Enter a choice"))
        if choice == 0:
            break
        elif choice==1:
            x,y= map(int,input("Enter numbers : "))
            print(add(x,y))
        elif choice==2:
            x,y= map(int,input("Enter numbers : "))
            print(sub(x,y))
        elif choice==3:
            x,y= map(int,input("Enter numbers : "))
            print(mul(x,y))
        elif choice==4:
            x,y= map(int,input("Enter numbers : "))
            print(div(x,y))
        else:
            pass


    return
