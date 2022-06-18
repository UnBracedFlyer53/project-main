import time

print("FLAMES is a popular game named after the acronym: Friends, Lovers, Affectionate, Marriage, Enemies, "
        "Sibling. This game does not accurately predict whether or not an individual is right for you, but it can be "
        "fun to play this with your friends.\n")
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

for i in flames:
    print(f"\n{name1} and {name2} will be {i}")

print("\nThank You!\nAll The Best!\n")