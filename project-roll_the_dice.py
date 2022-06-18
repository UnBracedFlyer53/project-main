import random
def rollthedice():
    print("This program allows you to roll a virtual dice for your games. The outcomes of the dice are purely random." )
    num=random.randint(1,6)
    print(f"Number on the dice: {num} \n")
rollthedice()