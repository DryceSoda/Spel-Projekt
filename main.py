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

# funktion för att spara stats i json filen "player_stats.json"
def save_player_stats(player_stats):
    with open(player_history_file, "w") as file:
        json.dump(player_stats, file, indent=4)

# funktion för hangman listan 
def display_hangman(wrong):
    print(hangedman[wrong])

# funktion för att samla alla stats
def display_stats(player_name, player_stats):
    print(f"\n{player_name}'s stats")
    print(f"wins: {player_stats[player_name]['wins']}, losses: {player_stats[player_name]['losses']}")

# funktion som checkar om ordet är rätt eller fel
def process_guess(guess, word, so_far, used):
    
    if guess in used:
        return so_far, f"You've already guessed {guess}, try something different."
    
    used.append(guess)

    if guess in word:
        
        new_so_far = "".join([guess if word[i] == guess else so_far[i] for i in range(len(word))])
        return new_so_far, f"The letter '{guess}' is in the word!"
    
    else:
        return so_far, f"Wrong guess, {guess} is not in the word. Try again."

# get hint funktion som kallas senare i koden för att låta spelaren få en ledtråd
def get_hint(word, so_far):
    for i in range(len(word)):
            if so_far[i] == "-":
                return f"Hint: One of the letters is '{word[i]}!"
    return "No hints available"
            

                                
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

# initierar att max_wrong är = längden av listan, som används varje gång svaret blir fel
max_wrong = len(hangedman) - 1

# blanding av olika ord jag kom upp med
words = ["Legendary", "Gros Michel", "BONK", "Fireflies", "Blueprint", "Brainstorm", "Avenged Sevenfold", "Metallica", "Ice Nine Kills", "Monarch", 
        "Aerosmith", "McQueen", "Balatro", "Snivy", "Water", "Schecter Synyster Gates Signature Standard", "Steve Vai", "Brains", "Photoshop",
        "Quixotic", "Embourgeoisement", "Metronome", "Surprise", "Book", "Skylanders", "Clock", "Bottle", "Cookie", "Beer", "Microphone", "Slay the Spire",
        "Microsoft", "Bracelet", "Computer", "Python", "Audiophile", "Technology", "Heretic", "Gunslinger", "Shower Scene", "Nintendo", "Acoustic"]

player_stats = load_player_stats()

# frågar efter spelarens namn
player_name = input("Your name: ")
print(f"Hi {player_name}! Welcome to hangman")
print("Type 'hint' if you need help, you can only ask for one hint!")
# lägger in spelaren i player_stats.json om namnet inte redan finns
if player_name not in player_stats:
    player_stats[player_name] = {'wins': 0, 'losses': 0}
    print("\nNew player added")

# visar stats från display_stats funktionen
display_stats(player_name, player_stats)

# startar spelet
while True:

    print("\nMain Menu")
    print("1. Play Hangman")
    print("2. Stats")
    print("3. Exit")
    choice = input("Choose an option (1, 2 or 3): ").strip()


    # om valet är 1, så körs spelet
    if choice == "1":
        word = random.choice(words).lower()

        so_far = "".join(["-" if char != " " else " " for char in word])
        wrong = 0
        used = []
        hint_used = False
    
    

        print("\nGame starting! Type 'hint' for a clue (only once!)")
    

        # går igenom om ett svar är rätt/fel baserat på om spelaren angivit rätt ord eller en bokstav som finns i ordet, samt tar bort en linje om det är varken eller
        while wrong < max_wrong and so_far != word:
            print("\n" + "-" * 30)
            display_hangman(wrong)
            print(f"\nUsed letters: {','.join(used) if used else 'None'}")
            print(f"\nWord: {so_far}")
            guess = input("Enter your guess: ").lower()
        
            if guess == "hint":
                if hint_used:
                    print("You've already used your hint!")
                else:
                    hint_used = True
                    print(get_hint(word, so_far))
                continue

            # låter spelare gissa genom att skriva ett helt ord
            if len(guess) > 1:
                if guess == word:
                    so_far = word
                    break
                else:
                    print(hangedman[wrong])
                    print(f"You really think {word} is it? Delusional, try again")
                    wrong += 1
                    continue
            so_far, message = process_guess(guess, word, so_far, used)
            print(message) 

            if message.startswith("Wrong"):
                wrong += 1           
        # skriver ut i en ny linje så det ser bättre ut                 
        print("\n" + "-" * 30)    
        if so_far == word:
            print(f"\nCongrats, {player_name}! {word} is correct")
            player_stats[player_name]['wins'] += 1
        
        else:
            display_hangman(wrong)
            print(f"You got hanged.. The correct word was {word}")        
            player_stats[player_name]['losses'] += 1
        
    # val 2 är att visa stats, alltså visar den upp hur många vinster/förluster kopplade till alla spelar namn
    elif choice == "2":
        display_stats(player_name, player_stats)   
        play_again = input("\nPlay again? (yes/no): ").strip().lower()
    # om valet är 3 så stängs spelet
    elif choice == "3":   
        if play_again != "yes":
            print("Really? I thought we had a connection.. that's okay, goodbye... :C")
            break
# sparar spelarens stats i player_stats.json och sparar tills nästa gång!
save_player_stats(player_stats)



    



    

