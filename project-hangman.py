import random
import time

print("----this program is developed by aditya goyal----")
#time.sleep(3)
print("\nHangman is a guessing game for two or more players. One player thinks of a word, phrase or sentence and the other tries to user_guess it by suggesting letters within a certain number of guesses. ")
#time.sleep(5)
print("\nIn this edition of hangman, the player will be dealing with movies. The player will be given 5 guesses.\n\n")
print("Starting the game in 3 seconds...\n\n")
#time.sleep(3)

def hollywood_hangman():
    guesslist = []
    answer_list = []
    used_letters = []
    vowels = "aeiouAEIOU"
    word = ""
    hollywood=["The Prestige"]
    answer = random.choice(hollywood).upper()
    for i in answer:
        answer_list.append(i)
    for i in answer_list:
        if i in vowels:
            word += i
        if i == " ":
            word += " "
        if i not in vowels and i != " ":
            word += "_"
    print("Your Word is: ", word)
    for i in word:
        guesslist.append(i)
    guesses = 5
    while guesses != 0:
        new_word = ""
        print("Guesses left: ", guesses)
        user_guess = input("Enter your user_guess: ").upper()
        if user_guess in vowels:
            print("Your Guess is Already There!   Please check before Guessing!")
        elif user_guess in used_letters:
            print("You have already used that letter! ")
            print("Letters used till now: ", used_letters)
        else:
            if user_guess in answer_list:
                count = answer_list.count(user_guess)
                used_letters.append(user_guess)
                if count == 1:
                    index = answer_list.index(user_guess)
                    guesslist[index] = answer_list[index]
                    for i in guesslist:
                        new_word += i
                    print(new_word)
                if count > 1:
                    if answer_list.count(user_guess) > 1:
                        for m in range(count):
                            b=answer_list.index(user_guess,m,len(answer_list))
                            c=answer_list.index(user_guess,b+m,len(answer_list))
                            guesslist[b]=guesslist[c]=answer_list[b]
                        for i in guesslist:
                            new_word+=i
                        print(new_word)
            else:
                print("Wrong Guess! ")
                guesses -= 1
        if new_word==answer:
            print("Congratulations, you guessed the word! ")
            print("The word was: ",answer)
            time.sleep(3)
            break


def bollywood_hangman():
    guesslist = []
    answer_list = []
    used_letters = []
    vowels = "aeiouAEIOU"
    word = ""
    bollywood = ["Airlift", "Baby", "The Kashmir Files", "Special 26", "Uri"]
    answer = random.choice(bollywood).upper()
    for i in answer:
        answer_list.append(i)
    for i in answer_list:
        if i in vowels:
            word += i
        if i == " ":
            word += " "
        if i not in vowels and i != " ":
            word += "_"
    print("Your Word is: ", word)
    for i in word:
        guesslist.append(i)
    guesses = 5
    while guesses != 0:
        new_word = ""
        print("Guesses left: ", guesses)
        user_guess = input("Enter your user_guess: ").upper()
        if user_guess in vowels:
            print("Your Guess is Already There!   Please check before Guessing!")
        elif user_guess in used_letters:
            print("You have already used that letter! ")
            print("Letters used till now: ", used_letters)
        else:
            if user_guess in answer_list:
                count = answer_list.count(user_guess)
                used_letters.append(user_guess)
                if count == 1:
                    index = answer_list.index(user_guess)
                    guesslist[index] = answer_list[index]
                    for i in guesslist:
                        new_word += i
                    print(new_word)
                if count > 1:
                    if answer_list.count(user_guess) > 1:
                        for m in range(count):
                            b=answer_list.index(user_guess,m,len(answer_list))
                            c=answer_list.index(user_guess,b+m,len(answer_list))
                            guesslist[b]=guesslist[c]=answer_list[b]
                        for i in guesslist:
                            new_word+=i
                        print(new_word)
            else:
                print("Wrong Guess! ")
                guesses -= 1
        if new_word==answer:
            print("Congratulations, you guessed the word! ")
            print("The word was: ",answer)
            time.sleep(3)
            break

'''
def hangman():
    guesses = 5
    while guesses != 0:
        new_word = ""
        print("Guesses left: ", guesses)
        user_guess = input("Enter your user_guess: ").upper()
        if user_guess in vowels:
            print("Your Guess is Already There!   Please check before Guessing!")
        elif user_guess in used_letters:
            print("You have already used that letter! ")
            print("Letters used till now: ", used_letters)
        else:
            if user_guess in answer_list:
                count = answer_list.count(user_guess)
                used_letters.append(user_guess)
                if count == 1:
                    index = answer_list.index(user_guess)
                    guesslist[index] = answer_list[index]
                    for i in guesslist:
                        new_word += i
                    print(new_word)
                if count > 1:
                    if answer_list.count(user_guess) > 1:
                        for m in range(count):
                            b=answer_list.index(user_guess)
                            c=answer_list.index(user_guess,b+m+1,len(answer_list))
                            guesslist[b]=guesslist[c]=answer_list[b]
                        for i in guesslist:
                            new_word+=i
                        print(new_word)
            else:
                print("Wrong Guess! ")
                guesses -= 1
        if new_word==answer:
            print("Congratulations, you guessed the word! ")
            print("The word was: ",answer)
            break
'''

while True:
    print("\nThere are 2 options-\n"
          "Hollywood Movies(1)\n"
          "Bollywood Movies(2)\n"
          "Exit the Menu(3)")
    x=int(input("\nYour Choice: "))

    if x==1:
        hollywood_hangman()
    if x==2:
        bollywood_hangman()
    if x==3:
        exit()