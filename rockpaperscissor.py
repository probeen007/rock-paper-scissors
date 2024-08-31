import random

def gamebrain():
    lst = ['r', 'p', 's']
    chance = 10
    no_of_chance = 0
    computer_point = 0
    human_point = 0

    while no_of_chance < chance:
        print("************************************************************************************************")
        finput = input("             PLEASE CHOOSE ONE AMONG (R/P/S): ")
        print("************************************************************************************************")
        _input = finput.lower()
        _random = random.choice(lst)

        if _input == _random:
            print(f"you guess {_input} and computer guess {_random} so there is:\n")
            print("TIE: you and computer both gave the same answer. BOTH GOT 0 POINTS\n")
        elif _input == "r" and _random == "p":
            computer_point += 1
            print(f"you guess {_input} and computer guess {_random} so\n")
            print("computer wins 1 point\n")
        elif _input == "p" and _random == "r":
            human_point += 1
            print(f"you guess {_input} and computer guess {_random} so\n")
            print("YOU win 1 point\n")
        elif _input == "p" and _random == "s":
            computer_point += 1
            print(f"your guess {_input} and computer guess {_random} so\n")
            print("computer wins 1 point\n")
        elif _input == "s" and _random == "p":
            human_point += 1
            print(f"your guess {_input} and computer guess {_random} so\n")
            print("YOU win 1 point\n")
        elif _input == "r" and _random == "s":
            human_point += 1
            print(f"your guess {_input} and computer guess {_random} so\n")
            print("YOU win 1 point\n")
        elif _input == "s" and _random == "r":
            computer_point += 1
            print(f"your guess {_input} and computer guess {_random} so\n")
            print("computer wins 1 point\n")
        else:
            print("Invalid input. Please enter R, P, or S only.")

        # Score update after each chance
        print("--------------------------------------------------------------------------------------------")
        print(f"Current Score: You: {human_point} | Computer: {computer_point}")
        print(f"Chances remaining: {chance - no_of_chance - 1}")
        print("--------------------------------------------------------------------------------------------")

        no_of_chance += 1

    print("================================================================================================")
    print("                                !GAME FINISHED!")
    print(                                 " FINAL RESULT IS HERE:")
    print(f"     YOUR FINAL SCORE IS {human_point} AND YOUR COMPUTER FINAL SCORE IS {computer_point} SO,")
    user_name = uname 
    score = int(human_point)
    user_score = int(score)

    f = open("score.txt", 'r')
    content = f.readlines()
    a = 0
    for line in content:
        for i in line:
            if i.isdecimal():
                current_highscore = int(i)
    f.close()

    if int(user_score) > (int(current_highscore)):
        f = open("score.txt", "w")
        f.write(f"current high scorer is {user_name} \n")
        integer = user_score
        f.write(f"And his Score is {str(integer)}") 
        f.close()
        print("Congratulations, you broke the high score of this game :)")
    else:
        f = open("score.txt", "r")
        print(f.read())   
        f.close()    
    
    if computer_point == human_point:
        print("             YOUR AND COMPUTER POINT ARE EQUAL SO THERE IS A TIE ==:)")
    elif computer_point > human_point:
        print("                 HA..HA..HA    your Computer wins and you lose :(")
    else:
        print(" OWO.....   you win and computer loses. Hmm! You are more intelligent than your computer ;)")
    print("================================================================================================")

print("                        HELLO CURIOUS HUMANS WELCOME TO ROCK/PAPER/SCISSOR GAME ")
print("_______________________________________________________________________________________________")
print("###############################################################################################")
uname = input("                       To Start Game First  Enter Your Name: ")
print("###############################################################################################")

def starting_game():
    print("Nice name")
    print("Ok " + uname + ",\n  \t BEFORE PLAYING GAME REMEMBER THIS!")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(uname + ",  YOU GET 10 CHANCES TO DEFEAT THE COMPUTER \n \t1 ENTER R FOR ROCK \n \t2 ENTER P FOR PAPER \n \t3 ENTER S FOR SCISSOR \n \t4 And RESULT IS GIVEN AFTER GAME FINISHED ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    inpgame()

# Input section to confirm if the player is ready to play or not
def inpgame():
    rinput = input(uname + ", IF YOU ARE READY TO CHALLENGE YOUR COMPUTER PRESS (YES): ")
    lrinput = rinput.lower()
    if 'yes' in lrinput:
        print("OK, Let's have fun!")
        gamebrain()
    else:
        inpgame()

# Username input validation
if len(uname) <= 2:
    print(uname + " name must be at least 2 characters")
    while len(uname) <= 2:
        uname = input(uname + " Enter Your Name (Greater than 2 Characters): ")   
        if len(uname) >= 2 and len(uname) <= 14:
            starting_game()
elif len(uname) >= 20:
    print(uname + " Name Must Be Less Than 20 Characters")
    while len(uname) >= 20:
        uname = input(uname + " Enter Your Name (Less Than 20 characters): ")
        if len(uname) >= 2 and len(uname) <= 20:
            starting_game()
else:
    starting_game()

def again():
    print("?????????????????????????????????????????????????????????????????????????????????????????????????")
    finput = input("If you want to play more, type YES, else type exit: ")
    print("?????????????????????????????????????????????????????????????????????????????????????????????????")
    sinput = finput.lower()
    if "yes" in sinput:
        gamebrain()
        again()
    else:
        print("! NOTICE !" * 8)
        print("IF YOU FIND ANY PROBLEM, MISTAKES, OR BUGS IN THIS PROGRAM CONTACT PRO = PRABIN BHATTARAI TO MAKE \n GAME EXPERIENCE BETTER :)")
        print(uname + ", HAVE A HAPPY PRO GAMES DAY;)")
        exit()

again()
