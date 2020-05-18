def hangman():
    word = "youtube"
    word_guess_state = ["_", "_", "_", "_", "_", "_", "_"]
    incorrect_letters = []
    incorrect_guess_value = 5
    print("Welcome to Hangman!\n Guess the word! You get five incorrect guesses.")
    print("The word has six letters and is a type of animal!")
    print("".join(word_guess_state))
    while incorrect_guess_value > 0:
        guess = (input("Guess a letter: "))
        if len(guess) > 1:
            print("Too many letters! Try again...")
            continue
        elif len(guess) == 0:
            print("You have to type something!")
            continue
        else:
            if guess[0] in word:
                current_char = guess[0]
                current_letter_value = word.count(current_char)
                print("You got a letter!")
                print("There are " + str(current_letter_value) + " " + str.upper(current_char) + "s in the word!")
                for x, y in enumerate(word):
                    if y is current_char:
                        word_guess_state[x] = current_char
                print("".join(word_guess_state) + "\n")
                if "_" not in word_guess_state:
                    print("You won!")
                    print("The word was: " + word)
                    break
                else:
                    continue
            else:
                incorrect_guess_value -= 1
                print("That was incorrect... sorry! You have " + str(incorrect_guess_value) + " more guesses.")
                incorrect_letters.append(guess[0])
                print("Incorrect letters: " + ",".join(incorrect_letters))
                print("".join(word_guess_state) + "\n")
                continue
    else:
        print("You lost! The word was: " + word)


hangman()






