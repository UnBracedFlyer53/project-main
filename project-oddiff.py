import random
def oddeven():

    player1=input("Enter the name of first player: ")
    player2="Computer"
    while True:
        best_of=int(input("best of ? :"))
        player_score, comp_score = 0, 0
        while best_of!=0:
            choice=input("Choice of player odd/even: ").lower()
            player_num=int(input("Number chosen by first player: "))
            comp_num = random.randint(1, 10)
            check_num=player_num+comp_num
            print(check_num)
            if check_num%2==0:
                if choice=="even":
                    player_score+=1
                    print(f"Congratulations!, {player1} won.")
                    print(f"Number chosen by comp {comp_num}.")
                if choice=="odd":
                    comp_score+=1
                    print(f"Sorry!, {player1} lost.")
                    print(f"Number chosen by comp {comp_num}.")
            if check_num%2!=0:
                if choice=="even":
                    comp_score+=1
                    print(f"Sorry!,{player1} lost.")
                    print(f"Number chosen by comp {comp_num}.")
                if choice=="odd":
                    player_score+=1
                    print(f"Congratulations!, {player1} won")
                    print(f"Number chosen by comp {comp_num}.")
            print(f"Scores-->\n{player1}'s Score: {player_score}\n{player2}'s Score: {comp_score}")
            best_of-=1
        print(f"Final Scores-->\n{player1}'s Score: {player_score}\n{player2}'s Score: {comp_score}")
        x=int(input("Press 1 to play again\nPress 2 to Exit: "))
        if x==2:
            break

oddeven()