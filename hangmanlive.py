# ====================================================================================================================
# -------------------------------------------- Project Assignment-2---------------------------------------------------
# ====================================================================================================================

import random

word_list = ["attitude", "attorney", "attract", "attractive", "attribute", "audience", "author", "authority", "auto",
             "available",
             "average", "avoid", "award", "aware", "awareness", "away", "awful", "cholesterol", "choose", "Christian",
             "Christmas",
             "church", "cigarette", "circle", "circumstance", "cite", "citizen", "city", "civil""civilian", "claim",
             "classic"]


def getRandom():
    word = random.choice(word_list)
    return word.upper()


def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letter = ['a', 'e']
    guessed_word = []
    tries = 6

    print("Lets Play Hangman!")
    print(displayHangman(tries))
    print(word_completion)
    print("\n")

    while not guessed and tries > 0:
        guess = input("Enter your guess:").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letter:
                print(f"You already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letter.append(guess)
            else:
                print("Good job,", guess, "is in the word!")
                guessed_letter.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True

        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_letter:
                print(f"You already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letter.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess")
        print(displayHangman(tries))
        print(word_completion)
        print("\n")

    if guessed:
        print("Congrats,you guessed the word! You win!")
    else:
        print("You ran out of tries.The word was" + word + "Maybe next time!")


def displayHangman(tries):
    stages = [  # 6 final state:head,torso,both arms and both legs
        """
                    --------
                    |     |
                    |     O
                    |    \\|/
                    |     |
                    |    / \\
                    -
        """,
        # 5 head,torso,both arms and one leg
        """
                    --------
                    |     |
                    |     O
                    |    \\|/
                    |     |
                    |    / 
                    -
        """,

        # 4 head,torso and both arms
        """
                    --------
                    |     |
                    |     O
                    |    \\|/
                    |     |
                    |    
                    -
        """,

        # 3 head ,torso and one arm
        """
                    --------
                    |     |
                    |     O
                    |    \\|
                    |     |
                    |   
                    -
        """,

        # 2 head torso
        """
                    --------
                    |     |
                    |     O
                    |     |
                    |     |
                    |    
                    -
        """,

        # 1 head
        """
                    --------
                    |     |
                    |     O
                    |    
                    |     
                    |    
                    -
        """,

        # 0 Initial Empty State
        """
                    --------
                    |     |
                    |   
                    |    
                    |     
                    |    
                    -
        """
    ]
    return stages[tries]


def main():
    word = getRandom()
    print(word)
    play(word)

    while input("Do you want to play again(Y/N):").upper() == "Y":
        word = getRandom()
        play(word)


main()
