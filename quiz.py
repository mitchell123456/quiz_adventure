# Our quiz!

def quiz():
    name = input("Name: ")
    score = 0

    print("Hello", name, "which english footballer is nominated for the 2016 Ballon d'or")
    answer = input("Answer: ")

    if answer.lower() in "jamie vardy":
        print("Correct!")

    print("Next question", name, "who is sunderland afc's all time top goal scorer")
    answer = input("Answer: ")

    if answer.lower() in "kevin phillips":
        print("Correct!")

    print("Lets continue", name, "in what year did sunderland afc win the FA cup")
    answer = input("Answer: ")

    if answer.lower() in "1973":
        print("Correct!")

    print("Next question", name, "how much did sunderland afc buy jermain defoe for")
    answer = input("Answer: ")

    if answer.lower() in "£14 million":
        print("Correct!")

    print("Final question", name, "what is sunderlands highest finish in the premier league")
    answer = input("Answer: ")

    if answer.lower() in "7":
        print("Correct")
        
    






# Leave this at the bottom - it makes quiz run automatically when you
# run your code.
if __name__ == "__main__":
    quiz()
