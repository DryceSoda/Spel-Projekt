# Hangman
import random

hangedman = (
    """
 ------
 |    |
 |
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |   -+-
 | 
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-
 |   
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |   
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |    |
 |   | 
 |   | 
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |    |
 |   | |
 |   | |
 |  
----------
""")

max_wrong = len(hangedman) - 1


words = ["Legendary", "Gros Michel", "BONK", "Fireflies", "Blueprint", "Brainstorm", "Avenged Sevenfold", "Metallica", "Ice Nine Kills", "Monarch", 
        "Aerosmith", "McQueen", "Balatro", "Snivy", "Water", "Schecter Synyster Gates Signature Standard", "Steve Vai", "Brains", "Photoshop",
        "Quixotic", "Embourgeoisement", "Metronome", "Surprise", "Book", "Gigabyte AORUS Elite B450-A"]

word = random.choice(words)

so_far = "-" * len(word)

wrong = 0

used = []

guess 

player = input("Gib name: ")

print("Hi", player + "!", "Welcome to Hangman, good luck")



while wrong < max_wrong and so_far != word:
    print(hangedman[wrong])
    print("\nYou've used the following letters:\n", guess)
    print("\nSo far, you have guessed:\t", so_far)
    
    guess = input("Enter your guess: ")
    
    while guess is used:
        print("You've already guessed the letter:\t", guess)
        guess = input("Guess again:\t")
        
    used.append(guess)
    
    if guess in word:
        print("The letter", guess, "is in the word")
        
        new = ""
        
    for i in range(len(word)):
        if guess == word [i]:
            new += guess
        else:
            new += so_far [i]
        so_far = new
        
else:
    print("\nSkill issue.", guess, "Isn't in the word, did you even try?")
    wrong += 1
    
if wrong == max_wrong:
    print(hangedman[wrong])
    print("You got hanged, skill issue")
    
else:
    print("\nThe word was", word)

input = ("\nPress [Enter] to exit")


    

