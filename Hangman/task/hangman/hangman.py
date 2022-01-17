# Write your code here
import random

words = ['python', 'java', 'kotlin', 'javascript']

answer = random.choice(words)
hint = answer[0:3]
guess = list("-" * (len(answer)))

def test(word):
    check = "".join([str(elem) for elem in word])
    if(len(word) == 1):
        if check.islower() and check.isalpha():
            return True
        else:
            print("Please enter a lowercase English letter")
            return False
    else:
        print("You should input a single letter")
        return False


def game():
    tries = 8
    letters = []
    while tries != 0 and list(answer) != guess:
        print("")
        print("".join([str(elem) for elem in guess]))
        word = input("Input a letter: ")
        if test(word) == False:
            continue
        if word in letters:
            print("You've already guessed this letter")
            continue
        letters.append(word)
        if word in answer:
            for i in range(len(answer)):
                if (answer[i] == word):
                    guess[i] = word
                    if list(answer) == guess:
                        print("")
                        print(answer)
                        print("""You guessed the word!
You survived!""")
                        return()
        else:
            print("That letter doesn't appear in the word")
            tries = tries - 1
    else:
        print("You lost!")

def start():
    print("H A N G M A N")
    choice = input('Type "play" to play the game, "exit" to quit: ')

    if choice == "play":
        game()
start()
