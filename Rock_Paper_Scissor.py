import random

r= "Computer Choose Rock"
p= "Computer Choose Paper"
s= "Computer Choose Scissor"
d= "Match Draw"
w= "You Wins"
c= "Computer Wins"

def isRock():
    cv = random.randint(0,2)
    if cv == 0:
        print(r)
        print(d)
    elif cv == 1:
        print(p)
        print(w)
    else:
        print(s)
        print(w)
    

def isPaper():
    cv = random.randint(0,2)
    if cv == 1:
        print(p)
        print(d)
    elif cv == 2:
        print(s)
        print(c)
    else:
        print(r)
        print(w)

def isScissor():
    cv = random.randint(0, 2)
    if cv == 2:
        print(s)
        print(d)
    elif cv == 0:
        print(r)
        print(c)
    else:
        print(p)
        print(w)
    


if __name__ == "__main__":
    print("Press: 0 For Rock, 1 For Paper, 2 For Scissor")
    num = int(input("How many times you want to play? "))
    for i in range(num):
        n = int(input("Enter Your Choice: "))
        if n>2:
            print("Incorrect Chocie, Try again")
        if n == 0:
            isRock()
        if n == 1:
            isPaper()
        if n == 2:
            isScissor()