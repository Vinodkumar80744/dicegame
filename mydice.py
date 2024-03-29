#program to play with the dice.the one who reaches 1st 20 is the winner and this game is maximum playable by any number of players.
#importing random(for random values on dice) and time modules
from random import randint
from time import sleep
#function
def dice():
    #this function generates a number and returns the sum of last score and present score.
    def diceresult(s,p1=0):
                n1=randint(1,6)
                print(n1)
                if n1==6:
                    if p1!=1:
                        input("another chance :enter a key")
                        s=diceresult(s)
                    else:
                        print('Another chance for me')
                        p=1
                        s=diceresult(s,p)
                s=s+n1
                return s
    #reads no of players from the user
    a=int(input('select no of players : '))
    if a==0:
        printf('invalid entry')
    #if there are is only one guy.
    if a==1:
        s1=0
        s2=0
        print("no competition its better to go with the computer or find a friend")
        choice=input("want to play with computer : 'y' or 'n'").upper()
        if choice=='Y':
            print("******YOUR GAME STARTED******")
            while s1<20 and s2<20:
                user=input("press a key to roll the dice :")
                s1=diceresult(s1)
                sleep(1)
                print("**your score is : ",s1)
                if s1>=20:
                    print("*******YOU WON THE GAME********")
                    break
                print("---------------------------------------------------------")
                print("computers turn.......")
                p=1
                s2=diceresult(s2,p)
                sleep(1)
                print("**computer score is : ",s2)
                if s2>=20:
                    print("****** COMPUTER WON********")
                print("---------------------------------------------------------")
    #if there are multiplule players
    if ( a > 1):
        def cal(a):
            #stores the scores of the players
            scores=[]
            for i in range(0,a):
                scores.append(0)
            execution=True
            while execution:
                for i in range(0,a):
                    user=input(f'{i+1}st player,press a key to roll the dice :')
                    s1=scores[i]
                    scores[i]=diceresult(s1)
                    sleep(0.5)
                    print("**your score is : ",scores[i])
                    print("---------------------------------------------------------")
                    for j in range(0,a):
                        if scores[j]>=20:
                            execution=False
                    if scores[i]>=20:
                        print(f"*******PLAYER {i+1} WON********")
        #calling the function
        cal(a)
                
dice()
#asks the users want to continue the game again.
while True:
    print("..hoping you enjoyed the game......")
    again=input("Do You Want to Play Again : 'y' or 'n' :").upper()
    if again=="Y":
        dice()
    else:
        break
input("enter a key to exit")

