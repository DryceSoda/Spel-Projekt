# Hangman
import random
import os

player_history_file = "player_history.txt"

# funktion för att ladda spelar historik
def load_player_history():
    if os.path.exists(player_history_file):
        with open(player_history_file, "r") as file:
            return set(line.strip() for line in file.readlines())
    return set()

def save_player_history(player_history):
    with open(player_history_file, "w") as file:
        for name in player_history:
            file.write(name + "\n")


# laddar existerande spelar historik (om det redan finns)
all_players = load_player_history()
session_players = set()

# frågar efter spelar namn
player_name = input("Gib name: ")
print(f"Hi {player_name}! Welcome to hangman, good luck")

if player_name not in all_players:
    all_players.add(player_name)
    print("\nNew player added to history")
session_players.add(player_name)

# visa session spelare
print("\nSession players: ")
print(", ".join(session_players))

print("\nAll-time players: ")
print(", ".join(all_players))

save_player_history(all_players)



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

# statistik för highscore
games_won = 0
games_lost = 0
total_wrong_guesses = 0
lowest_wrong_guesses = float('inf')

while True:
    word = random.choice(words).lower()

    so_far = "".join(["-" if char != " " else " " for char in word])
    wrong = 0
    used = []
    hint_used = False
    guess = ""
    

    
    print("Type 'hint' if you need help, you can only ask for one hint!")

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
            wrong += 1
            #print("debug: wrong counter is:", wrong)
            print("\nSkill issue.", guess, "Isn't in the word, did you even try?")
            print(hangedman[wrong])
    # hur många spel som vunnits/förlorats
    if so_far == word:
        games_won += 1
        total_wrong_guesses += wrong
        print("\nCongrats!", word, "is correct!")
    else:
        games_lost += 1
        total_wrong_guesses += wrong
        print(hangedman[wrong])
        print("You got hanged, skill issue")
        print("The correct word was:", word)
    
    # skriver ut statistik
    print("\nGame Statistics:")
    print("Games Won: ", games_won)
    print("Games Lost: ", games_lost)
    if games_won > 0:
        print("Lowest wrongs: ", lowest_wrong_guesses)
        print("Total wrongs: ", total_wrong_guesses)

        # använde det här innan, lämnar även om det inte används längre
        #if wrong == max_wrong:
            #print(hangedman[wrong])
            #print("You got hanged, skill issue")
            #print("The correct word was:", word)
    
        #else:
            #print("\nCongrats!", word," ", "is correct!")

    # ger ett val om spelaren vill köra igen eller inte
    play_again = input("\nPlay again? (yes/no): ").lower()
    if play_again != "yes":
        print("Really? I thought we had a connection.. that's okay, goodbye... :C")
        break


    



    

