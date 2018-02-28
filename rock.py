import random
c= 1
while (c==1): 
    options = ["Rock","Paper","Scissors"]
    r = random.choice(options)
    user = input("Enter Your Choice: ")
    user = user.lower()
    if user == 'rock' or 'paper' or 'scissors':
        print ("The computer has drawn ", r,  " whilst you have drawn " ,user)
    if user == 'rock':
        if r == 'Rock':
            print ('Tie Game')
        elif r == 'Paper':
            print ('r Wins')
        else:
            print ('User Wins')
    if user == 'paper':
        if r == 'Rock':
                print ('User Wins')
        elif r == 'Paper':
            print ('Tie Game')
        else:
            print ('r Wins')
    if user == 'scissors':
        if r == 'Rock':
                print ('r Wins')
        elif r == 'Paper':
            print ('User Wins')
        else:
            print ('Tie Game')
