# An adventure game
health = 1
isaac_matthews_health = 10


    




def room1():
    global health

    print("Its election day")
    print("Youre in the booth looking at the candidates")
    print("Donald Trump     Hilary Clinton")
    print("But you dont see thoose names... you see")
    print("A. Isaac Matthews   Mr Herbane")
    print("B. Isaac Matthews  Scarce")
    print("C. Isaac Matthews   Keemstar")
    answer = input("Answer: ")

    if answer.lower() == "a":
        print("Do you even know who they are")
        room2()

    if answer.lower() == "b":
        print("You just picked this because of scarce didnt you")
        room2()

    if answer.lower() == "c":
        print("You are beyond help now")
        room2()

    print("Ok its time to cast your vote")
    print("But wait, whats that?")
    print("Its Isaac Matthews!!!")
    print("A. Walk up to him and take a selfie")
    print("B. Ignore him. And ask him why he is here")
    print("C. Charge at him, tackle him through a table and ask who is your real dad")
    answer = input("Answer: ")

    if answer.lower() == "a":
        print("You just want to brag and myspace")
        room2()

    if answer.lower() == "b":
        print("You secritly want to punch him in his massive ears")
        room2()

    if answer.lower() == "c":
        print("Firstly good choice and secondly we all know his real dad is Glen")
        room2()


def room2():

    print("Isaac is annoyed because he heard someone talking about him having pictures of someone on his duck USB stick")
    print("He starts to attack everyone in sight")
    print("He is staring right at you")
    print("A. Be a man and fight him")
    print("B. Be an Isaac and hide under a table")
    answer = input("Answer: ")

    if answer.lower() == "a":
        print("Enter arena. Round 1 Fight!!")
        room3()

    if answer.lower() == "b":
        print("Coward, you are going to fight him anyway. Round 1 Fight!!")
        room3()


def room3():

    print("Attack or talk about his dads")
    if answer.lower() == "attack":
        print("You deal 2 damage")

    if answer.lower() == "talk about his dads":
        print("CRITICAL HIT, 5 damage")

    print("Attack or talk about his dads")
    if answer.lower() == "attack":
        print("CRITICAL HIT, 5 damage")

    if answer.lower() == "talk about his dads":
        print("You deal 2 damage")

    print("He is weak")
    print("Attack or talk about his dads")
    if answer.lower() == "attack":
        print("Well done he is dead. You should be proud!")
        room4()

    if answer.lower() == "talk about his dads":
        print("Well done he is dead. You should be proud!")
        room4()


def room4():

    print("You have finally killed Isaac Matthews.")
    print("The world is saved")
    print("BOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOM")
    print("Oh no")
    print("Its Donald Trump")
    print("And hes not happy")
    print("He says he wants to nuke cincinnati")
    print("                                   ")
    print("                                   ")
    print("He nuke cincinnati and kills everyone including a gorilla called harambe")
    print("Conspiricy theorists go nuts")
    print("Game over")
    
        
    
        
          
    
    
    
    








# Leave this at the bottom - it makes room1 run automatically when you
# run your code.
if __name__ == "__main__":
    room1()
