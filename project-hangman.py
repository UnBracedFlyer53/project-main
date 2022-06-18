import random

def hangman():
    l1 = ["3 Idiots", "Special 26", "Raid" ]
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
