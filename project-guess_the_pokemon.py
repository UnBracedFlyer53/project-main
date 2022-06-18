import random

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
    print("\nGuess the Pokemon\n")
    print("1) Start\n2) Exit")
    w = int(input("Choose One! : "))
    if w==1:
        guess_the_pokemon()
    if w == 2:
        break