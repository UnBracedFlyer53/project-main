import random
import string  # import statement
# import time

print("\nthis program is created by Aditya Goyal,Aviral Maheshwari and Prakhar Saxena.\n")


def rock_paper_scissors():
    print("Rock-Paper-Scissors is a game played to settle disputes between two people. Thought to be a game of chance "
          "that depends on random luck similar to flipping coins or drawing straws, the game is often taught to "
          "children to help them settle arguments between themselves on their own without adult intervention. "
          "However, the game actually can be a game that has an element of skill that requires quick thinking and "
          "perceptive reasoning.\n")
    user_score, comp_score = 0, 0
    a, b, c = "rock", "paper", "scissors"
    name = input("Enter your name: ")
    # time.sleep(1)
    while True:
        user_input = input("\nChoose :Rock,Paper,Scissor\nYour Choice:")
        comp_input = random.choice([a, b, c])

        if user_input.lower() == a:
            if comp_input == b:
                comp_score += 1
                print("\nYou Lose!")
            elif comp_input == c:
                user_score += 1
                print("\nYou Win!")
            elif comp_input == a:
                comp_score += 1
                user_score += 1
                print("\nIt's a Draw!")

        elif user_input.lower() == b:
            if comp_input == a:
                user_score += 1
                print("\nYou Win!")
            elif comp_input == c:
                comp_score += 1
                print("\nYou Lose!")
            elif comp_input == b:
                comp_score += 1
                user_score += 1
                print("\nIt's a Draw!")


        elif user_input.lower() == c:
            if comp_input == a:
                comp_score += 1
                print("\nYou Lose!")
            elif comp_input == b:
                user_score += 1
                print("\nYou Win!")
            elif comp_input == c:
                comp_score += 1
                user_score += 1
                print("\nIt's a Draw!")

        print(f"\nYour Score : {user_score} ")
        print(f"Computer Score: {comp_score}")
        # time.sleep(1)
        x = int(input("\nPress 1 to Play Again\nPress 2 to Exit :"))
        # time.sleep(1)
        if x == 1:
            continue
        elif x == 2:
            break


def password_generator():
    print(
        "The key aspects of a strong password are length (the longer the better); a mix of letters (upper and lower "
        "case), numbers, and symbols, no ties to your personal information, and no dictionary words.")
    print("\nDon't worry, Today I'll build a Strong Password For You.")
    length = int(input("\nHow Long Do you want the Password to be? :"))
    password = ""
    while len(password) < length:
        alphabets = random.choice(string.ascii_letters)
        digits = random.choice(string.digits)
        symbols = random.choice(string.punctuation)
        d = random.choice([alphabets, digits, symbols])
        password = password + str(d)
    # time.sleep(2)
    print(f"The Password Generated for You is:  {password}\n")


def flames():
    print(
        "FLAMES is a popular game named after the acronym: Friends, Lovers, Affectionate, Marriage, Enemies, "
        "Sibling. This game does not accurately predict whether or not an individual is right for you, but it can be "
        "fun to play this with your friends.\n")
    # time.sleep(1.5)
    name1 = input("Enter Name1: ")
    name2 = input("Enter Name2: ")
    for i in name1:
        if i in name2:
            name1.replace(i, "")
            name2.replace(i, "")
    count = len(name1) + len(name2)
    flames = ["Friends", "Lovers", "Affectionate", "Marriage", "Enemies", "Sibling"]
    while len(flames)!=1:
        a = count % len(flames)
        flames.remove(flames[a-1])
    # time.sleep(1.5)
    for i in flames:
        print(f"\n{name1} and {name2} will be {i}")

    print("\nThank You!\nAll The Best!\n")


def rollthedice():
    print(
        "This program allows you to guess a number, and then rolls a virtual dice.\n If your guess is correct, then you get 1 points, and if it is wrong, then you lose.")
    guess = int(input("Your Guess: "))
    num = random.randint(1, 6)
    if guess == num:
        print("Congratulations, you win!")
    else:
        print(f"Number on the dice: {num} \n")


def hangman():
    l1 = ["3 Idiots", "Special 26", "Raid", ]
    l2 = ["The Prestige", "Intersteller"]

    def guessbolly():
        movie_og = random.choice(l1)

        # function to change letters to dashes, and provide vowels
        def give_word(movie_name: str):
            new_str = ""
            for i in movie_name:
                if i in list("aieouAEIOU"):
                    new_str += i.lower()
                elif i == " ":
                    new_str += " "
                else:
                    new_str += "_"
            return new_str

        # function to swap dashes with existing letters
        def swap_letters(original: str, guessed: str, guess: str):
            if guess in guessed.lower():
                return "exists"
            if guess in original.lower():
                guess_indexes = []
                for letter in range(0, len(movie_og.lower())):
                    if guess.lower() == movie_og.lower()[letter]:
                        guess_indexes.append(letter)
                for guess_index in guess_indexes:
                    guessed = guessed[:guess_index] + guess.lower() + guessed[guess_index + 1:]
                return guessed
            else:
                print("Does not exist.")

        coded = give_word(movie_og)
        print("The Movie to be Guessed is", coded)
        counter = 5
        success = False
        while counter:
            print(f"You have {counter} lives.")
            guess = input("Enter letter to be guessed: ")
            check = swap_letters(movie_og, coded, guess)
            if check != "exists" and check is not None:
                coded = check
                print(f"Bingo, {guess} was in the word!\nCurrent word: {coded}")

                if coded.lower() == movie_og.lower():
                    success = True
                    break
            elif check == "exists":
                print("Your guess already exists in the word, please enter another guess.")
            else:
                counter -= 1
                print(f"{guess} was not in the word. You lose one life!")

        if success == True:
            print(f"You have guessed the movie! It was {movie_og}")
        else:
            print(f"You have failed to guess the movie! It was {movie_og}")

    def guessholly():
        movie_og = random.choice(l2)

        # function to change letters to dashes, and provide vowels
        def give_word(movie_name: str):
            new_str = ""
            for i in movie_name:
                if i in list("aieouAEIOU"):
                    new_str += i.lower()
                elif i == " ":
                    new_str += " "
                else:
                    new_str += "_"
            return new_str

        # function to swap dashes with existing letters
        def swap_letters(original: str, guessed: str, guess: str):
            if guess in guessed.lower():
                return "exists"
            if guess in original.lower():
                guess_indexes = []
                for letter in range(0, len(movie_og.lower())):
                    if guess.lower() == movie_og.lower()[letter]:
                        guess_indexes.append(letter)
                for guess_index in guess_indexes:
                    guessed = guessed[:guess_index] + guess.lower() + guessed[guess_index + 1:]
                return guessed
            else:
                print("")

        coded = give_word(movie_og)
        print("The Movie to be Guessed is", coded)
        counter = 5
        success = False
        while counter:
            print(f"You have {counter} lives.")
            guess = input("Enter letter to be guessed: ")
            check = swap_letters(movie_og, coded, guess)
            if check != "exists" and check is not None:
                coded = check
                print(f"Bingo, {guess} was in the word!\nCurrent word: {coded}")

                if coded.lower() == movie_og.lower():
                    success = True
                    break
            elif check == "exists":
                print("Your guess already exists in the word, please enter another guess.")
            else:
                counter -= 1
                print(f"{guess} was not in the word. You lose one life!")

        if success == True:
            print(f"You have guessed the movie! It was {movie_og}")
        else:
            print(f"You have failed to guess the movie! It was {movie_og}")

    while True:
        print("\nHANGMAN!\n")
        print("1) Bollywood\n2) Hollywood\n3) Exit")
        k = int(input("Choose One! : "))
        if k == 1:
            guessbolly()
        if k == 2:
            guessholly()
        if k == 3:
            break


def oddeven():
    player1 = input("Enter the name of first player: ")
    player2 = "Computer"
    while True:
        best_of = int(input("best of ? :"))
        player_score, comp_score = 0, 0
        while best_of != 0:
            choice = input("Choice of player odd/even: ").lower()
            player_num = int(input("Number chosen by first player: "))
            comp_num = random.randint(1, 10)
            check_num = player_num + comp_num
            print(check_num)
            if check_num % 2 == 0:
                if choice == "even":
                    player_score += 1
                    print(f"Congratulations!, {player1} won.")
                    print(f"Number chosen by comp {comp_num}.")
                if choice == "odd":
                    comp_score += 1
                    print(f"Sorry!, {player1} lost.")
                    print(f"Number chosen by comp {comp_num}.")
            if check_num % 2 != 0:
                if choice == "even":
                    comp_score += 1
                    print(f"Sorry!,{player1} lost.")
                    print(f"Number chosen by comp {comp_num}.")
                if choice == "odd":
                    player_score += 1
                    print(f"Congratulations!, {player1} won")
                    print(f"Number chosen by comp {comp_num}.")
            print(f"Scores-->\n{player1}'s Score: {player_score}\n{player2}'s Score: {comp_score}")
            best_of -= 1
        print(f"Final Scores-->\n{player1}'s Score: {player_score}\n{player2}'s Score: {comp_score}")
        x = int(input("Press 1 to play again\nPress 2 to Exit: "))
        if x == 2:
            break


def handcricket():
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

    def cricket():
        user_score, comp_score = 0, 0
        innings = oddeven()
        print("Starting Game...\n")
        while True:
            if innings == "bat":
                user_num = int(input("Your Num: "))
                comp_num = random.randint(1, 10)
                print(f"Number chosen by computer: {comp_num}")
                if user_num == comp_num:
                    print("You are out! ")
                    print(f"Runs Scored by you: {user_score}")
                    print("\nSeconds innings starting now --->\n"
                          "It's your chance to bowl now .")
                    while True:
                        user_num = int(input("Your Num: "))
                        comp_num = random.randint(1, 10)
                        if comp_num == user_num:
                            print("Comp is out!")
                            print(f"Runs scored by comp: {comp_score}")
                            break


                        else:
                            comp_score += comp_num
                            print(f"Number chose by comp: {comp_num}")
                            print(f"Comp Runs : {comp_score}")

                    break
                else:
                    user_score += user_num
                    print(f"Your Runs: {user_score}")
            if innings == "bowl":
                user_num = int(input("Your Num: "))
                comp_num = random.randint(1, 10)
                print(f"Number chosen by computer: {comp_num}")
                if user_num == comp_num:
                    print(f"Comp is out! \n"
                          f"Runs scored by Comp: {comp_score}")
                    print("\nSeconds innings starting now --->\n"
                          "It's your chance to bat now .")
                    while True:
                        user_num = int(input("Your Num: "))
                        comp_num = random.randint(1, 10)
                        if comp_num == user_num:
                            print(f"{user_name} is out!")
                            print(f"Runs scored by {user_name}: {user_score}")
                            break

                        else:
                            user_score += user_num
                            print(f"Number chosen by computer: {comp_num}")
                            print(f"User Runs : {user_score}")

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

    cricket()


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
                if user_num == (comp_num - 1) or user_num == (comp_num + 1):
                    print("You are out! ")
                    print(f"Runs Scored by you: {user_score}")
                    print("\nSeconds innings starting now --->\n"
                          "It's your chance to bowl now .")
                    while True:
                        user_num = int(input("Your Num: "))
                        comp_num = random.randint(1, 10)
                        if comp_num == (user_num - 1) or comp_num == (user_num + 1):
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
                    if user_num == comp_num:
                        user_score += (user_num * comp_num)
                        print(f"Your Runs: {user_score}")
                    else:
                        user_score += user_num
                        print(f"Your Runs: {user_score}")
            if innings == "bowl":
                user_num = int(input("Your Num: "))
                comp_num = random.randint(1, 10)
                print(f"Number chosen by computer: {comp_num}")
                if (user_num - 1) == comp_num or (user_num + 1) == comp_num:
                    print(f"Comp is out! \n"
                          f"Runs scored by Comp: {comp_score}")
                    print("\nSeconds innings starting now --->\n"
                          "It's your chance to bat now .")
                    while True:
                        user_num = int(input("Your Num: "))
                        comp_num = random.randint(1, 10)
                        if (comp_num + 1) == user_num or (comp_num - 1) == user_num:
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


def guess_the_pokemon():

    pokemon = ["pikachu","charizard"]
    all_hints=[["pikachu",[["type","electric"],["region","kanto"]]],["charizard",[["type","fire"],["region","kanto"]]]]
    z=0
    pokemon_og = random.choice(pokemon)
    for i in all_hints:
        if i[0]==pokemon_og:
            hints=i[1]
    # function to change letters to dashes, and provide vowels
    def give_word(pokemon_name: str):
        new_str = ""
        for i in pokemon_name:
            if i in list("aieouAEIOU"):
                new_str += i.lower()
            elif i == " ":
                new_str += " "
            else:
                new_str += "_"
        return new_str

    # function to swap dashes with existing letters
    def swap_letters(original: str, guessed: str, guess: str):
        if guess in guessed.lower():
            return "exists"
        if guess in original.lower():
            guess_indexes = []
            for letter in range(0, len(pokemon_og.lower())):
                if guess.lower() == pokemon_og.lower()[letter]:
                    guess_indexes.append(letter)
            for guess_index in guess_indexes:
                guessed = guessed[:guess_index] + guess.lower() + guessed[guess_index + 1:]
            return guessed
        else:
            print("")

    coded = give_word(pokemon_og)
    print("The Pokemon to be Guessed is", coded)
    counter = 5
    success = False
    while counter:
        print(f"You have {counter} lives.")
        print(f"You have {2-z} hints left.")
        guess = input("\nEnter letter to be guessed: ").lower()
        check = swap_letters(pokemon_og, coded, guess)
        if check != "exists" and check is not None:
            coded = check
            print(f"Bingo, {guess} was in the word!\nCurrent word: {coded}\n")

            if coded.lower() == pokemon_og.lower():
                success = True
                break
        elif check == "exists":
            print("Your guess already exists in the word, please enter another guess.")
        else:
            counter -= 1
            print(f"{guess} was not in the word. You lose one life!")
            a=int(input("Press 1 to get a hint\nPress 2 to continue: "))

            if a==1:
                if len(hints)<=z:
                    print("No more hints !")
                else:
                    print(f"Hint({z+1}):The Pokemon's {hints[z][0]} is {hints[z][1]}. \n")
                    z=z+1

    if success == True:
        print(f"You have guessed the pokemon! It was {pokemon_og}")
    else:
        print(f"You have failed to guess the pokemon! It was {pokemon_og}")


while True:
    print("---Menu---\n"
          "Please enter the number corresponding to the option you want to choose.\n"
          "The Following Options are Available-\n"
          "(1)Rock Paper Scissors\n"
          "(2)Password Generator\n"
          "(3)FLAMES\n"
          "(4)Roll the Dice\n"
          "(5)Hangman\n"
          "(6)OddEven\n"
          "(7)Hand Cricket(Virtual Cricket)\n"
          "(8)Crazy Cricket\n"
          "(9)Guess The Pokemon\n"
          "(10)Exit the Menu")
    x = int(input("\nYour Choice: "))

    if x == 1:
        rock_paper_scissors()
    if x == 2:
        password_generator()
    if x == 3:
        flames()
    if x == 4:
        rollthedice()
    if x == 5:
        hangman()
    if x == 6:
        oddeven()
    if x == 7:
        handcricket()
    if x == 8:
        crazycricket()
    if x == 9:
        while True:
            print("\nGuess the Pokemon\n")
            print("1) Start\n2) Exit")
            w = int(input("Choose One! : "))
            print("")
            if w == 1:
                guess_the_pokemon()
            if w == 2:
                break
    if x == 10:
        exit()
