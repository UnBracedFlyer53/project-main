import random

def crazycricket():
    user_name = input("Your Name: ")
    user_score, comp_score = 0, 0

    def oddeven():
        print("Going in for a toss...\n")
        choice_list = ["bat", "bowl"]
        user_c = input("What do you want to choose(odd/even):").lower()
        user_n = int(input("Num : "))
        comp_num = random.randint(1, 9)
        if (user_n + comp_num) % 2 == 0:
            if user_c == "odd":
                print("You lose! ")
                comp_choice = random.choice(choice_list)
                print(f"The computer has chose to {comp_choice}")
                return comp_choice
            if user_c == "even":
                user_choice = input("The Choice is yours. What do you choose(bat/bowl)? :").lower()
                return user_choice
        if (user_n + comp_num) % 2 != 0:
            if user_c == "even":
                print("You lose! ")
                comp_choice = random.choice(choice_list)
                print(f"The computer has chosen to {comp_choice}")
                return comp_choice
            if user_c == "odd":
                user_choice = input("The Choice is yours. What do you choose(bat/bowl)? :").lower()
                return user_choice

    def ccricket():
        user_score, comp_score = 0, 0
        innings = oddeven()
        print("Starting Game...\n")
        while True:
            if innings == "bat":
                user_num = int(input("Your Num: "))
                comp_num = random.randint(1, 10)
                print(f"Number chosen by computer: {comp_num}")
                if user_num == (comp_num-1) or user_num == (comp_num+1):
                    print("You are out! ")
                    print(f"Runs Scored by you: {user_score}")
                    print("\nSeconds innings starting now --->\n"
                          "It's your chance to bowl now .")
                    while True:
                        user_num = int(input("Your Num: "))
                        comp_num = random.randint(1, 10)
                        if comp_num == (user_num-1) or comp_num == (user_num+1):
                            print(f"No chosen by comp: {comp_num}")
                            print("Comp is out!")
                            print(f"Runs scored by comp: {comp_score}")
                            break
                        else:
                            if user_num == comp_num:
                                comp_score += (user_num * comp_num)
                                print(f"Comp Runs: {comp_score}")
                                print(f"Number chose by comp: {comp_num}")
                            else:
                                comp_score += comp_num
                                print(f"Comp Runs: {comp_score}")
                                print(f"Number chose by comp: {comp_num}")

                    break
                else:
                    if user_num==comp_num:
                        user_score+=(user_num*comp_num)
                        print(f"Your Runs: {user_score}")
                    else:
                        user_score += user_num
                        print(f"Your Runs: {user_score}")
            if innings == "bowl":
                user_num = int(input("Your Num: "))
                comp_num = random.randint(1, 10)
                print(f"Number chosen by computer: {comp_num}")
                if (user_num-1) == comp_num or (user_num+1) == comp_num:
                    print(f"Comp is out! \n"
                          f"Runs scored by Comp: {comp_score}")
                    print("\nSeconds innings starting now --->\n"
                          "It's your chance to bat now .")
                    while True:
                        user_num = int(input("Your Num: "))
                        comp_num = random.randint(1, 10)
                        if (comp_num+1) == user_num or (comp_num-1) == user_num:
                            print(f"{user_name} is out!")
                            print(f"Runs scored by {user_name}: {user_score}")
                            break

                        else:
                            if user_num == comp_num:
                                user_score += (user_num * comp_num)
                                print(f"No shown by comp: {comp_num}")
                                print(f"Your Runs: {user_score}")
                            else:
                                user_score += user_num
                                print(f"No shown by comp: {comp_num}")
                                print(f"Your Runs: {user_score}")

                    break
                else:
                    comp_score += comp_num
                    print(f"Comp Runs: {comp_score}")
        winner = max(user_score, comp_score)
        if winner == user_score:
            print(f"\nCongratulations {user_name}, you won the game !\n"
                  f"Final Scores-->\n"
                  f"{user_name} : {user_score} runs\n"
                  f"Computer : {comp_score} runs\n")
        if winner == comp_score:
            print(f"\nSorry {user_name}, you lost the game !\n"
                  f"Final Scores-->\n"
                  f"{user_name} : {user_score} runs\n"
                  f"Computer : {comp_score} runs\n")
        if user_score == comp_score:
            print(f"\nCongratulations {user_name}, It's a draw !\n"
                  f"Final Scores-->\n"
                  f"{user_name} : {user_score} runs\n"
                  f"Computer : {comp_score} runs\n")

    ccricket()


crazycricket()
