# Hangman
import os
import json
import random

player_history_file = "player_stats.json"

# funktion för att ladda spelar historik
def load_player_stats():
    if os.path.exists(player_history_file):
        with open(player_history_file, "r") as file:
            return json.load(file)
    return{}

def save_player_stats(player_stats):
    with open(player_history_file, "w") as file:
        json.dump(player_stats, file, indent=4)


# laddar existerande spelar historik (om det redan finns)
player_stats = load_player_stats()





# hanged man "lista" så det ser ut som en stick gubbe
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

# tar bort en linje när spelaren får fel
max_wrong = len(hangedman) - 1

# blanding av olika ord jag kom upp med
words = ["Legendary", "Gros Michel", "BONK", "Fireflies", "Blueprint", "Brainstorm", "Avenged Sevenfold", "Metallica", "Ice Nine Kills", "Monarch", 
        "Aerosmith", "McQueen", "Balatro", "Snivy", "Water", "Schecter Synyster Gates Signature Standard", "Steve Vai", "Brains", "Photoshop",
        "Quixotic", "Embourgeoisement", "Metronome", "Surprise", "Book", "Gigabyte AORUS Elite B450-A", "Eric Clapton", "Bottle", "Cookie", "Beer", "Microphone"]

# frågar efter spelar namn
player_name = input("Gib name: ")
print(f"Hi {player_name}! Welcome to hangmansdn")
print("Type 'hint' if you need help, you can only ask for one hint!")

if player_name not in player_stats:
    player_stats[player_name] = {'wins': 0, 'losses': 0}
    print("\nNew player added")

print(f"\n{player_name}'s stats")
print(f"wins: {player_stats[player_name]['wins']}, losses: {player_stats[player_name]['losses']}")



while True:
    word = random.choice(words).lower()

    so_far = "".join(["-" if char != " " else " " for char in word])
    wrong = 0
    used = []
    hint_used = False
    #guess = ""
    

    
    

    # går igenom om ett svar är rätt/fel baserat på om spelaren angivit rätt ord eller en bokstav som finns i ordet, samt tar bort en linje om det är varken eller
    while wrong < max_wrong and so_far != word:
        print(hangedman[wrong])

        print("\nYou've used the following letters:\n", " ".join(used))
        print("\nSo far, you have guessed:\t", so_far)
    
        guess = input("Enter your guess: ").lower()


        if guess == "hint":
            if hint_used:
                print("You've already used one hint!")
            else:
                hint_used = True
                revealed_letter = None

                for i in range(len(word)):
                    if so_far[i] == "-":
                        revealed_letter = word[i]
                        break
                if revealed_letter:
                    print("\nHere's your hint! One of the letters is:", revealed_letter)
                else:
                    print("\nNo hint available, you've already used it")
            continue

        # låter spelare gissa genom att skriva ett helt ord
        if len(guess) > 1:
            if guess == word:
                so_far = word
                break
            else:
                print(hangedman[wrong])
                print("You really think that's the word? Delusional, try again")
                wrong += 1
                continue
            
            # tillåter inte bokstäver eller ord användas om
        while guess in used:
            print("You've already guessed the letter:\t", guess)
            guess = input("Guess again:\t").lower()
        
        used.append(guess)
    
    
        #print("debug: guess is:", guess)
        #print("debug: word is:", word)

        # om bokstäven finns i ordet
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
            print(f"\nSkill issue. {guess} isn't the word, did you even try?")
            wrong += 1
            #print(hangedman[wrong])
    if so_far == word:
        print(f"\nCongrats, {player_name}! {word} is correct")
        player_stats[player_name]['wins'] += 1
        
    else:
        print(hangedman[wrong])
        print("You got hanged..")
        print(f"The correct word was: {word}")
        player_stats[player_name]['losses'] += 1
        
        print(f"\n{player_name}'s stats")
        print(f"wins: {player_stats[player_name]['wins']}, losses: {player_stats[player_name]['losses']}")



    # ger ett val om spelaren vill köra igen eller inte
    play_again = input("\nPlay again? (yes/no): ").strip().lower()
    if play_again != "yes":
        print("Really? I thought we had a connection.. that's okay, goodbye... :C")
        break

save_player_stats(player_stats)
print("History saved, see you next time")


    



    

