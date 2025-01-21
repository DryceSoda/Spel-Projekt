# Hangman
import os
import json
import random
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
player_history_file = os.path.join(script_dir, "player_stats.json")

    
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

# funktion för att "återställa" terminal vajre gång den printar ut uppdaterade versionen av hangedman listan (alltså gubben)
def clear_screen():
    if os.name == 'nt':
        os.system('cls')
                                        
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

# initierar att max_wrong = längden av listan, som används senare i koden (användingen är för sjävla stickgubben)
max_wrong = len(hangedman) - 1


# blanding av olika ord jag kom upp med
words = ["Legendary", "Gros Michel", "Chair", "Fireflies", "Blueprint", "Brainstorm", "Avenged Sevenfold", "Metallica", "Ice Nine Kills", "Monarch", 
        "Aerosmith", "McQueen", "Balatro", "Snivy", "Water", "Schecter Synyster Gates Signature Standard", "Steve Vai", "Brains", "Photoshop",
        "Quixotic", "Embourgeoisement", "Metronome", "Surprise", "Book", "Skylanders", "Clock", "Bottle", "Cookie", "Beer", "Microphone", "Slay the Spire",
        "Microsoft", "Bracelet", "Computer", "Python", "Audiophile", "Technology", "Heretic", "Gunslinger", "Shower Scene", "Nintendo", "Acoustic",
        "Projector", "Door", "Headphones", "Ibanez", "Paarthurnax",]

play_again = "no"
player_stats = load_player_stats()

# frågar efter spelarens namn
player_name = input("Your name: ")
print(f"Hi {player_name}! Welcome to Hangman! Try to guess the correct word, or you'll get hanged! Good luck!")
print("Type 'hint' if you need help, you can only ask for one hint!")

# lägger in spelaren i player_stats.json om namnet inte redan finns, och skriver ut att spelaren lagts till i json filen
if player_name not in player_stats:
    player_stats[player_name] = {'wins': 0, 'losses': 0}
    print("\nNew player added")

# lista för olika meddelanden som skrivs ut när spelaren förlorat
game_over_rep = [f"Game over, it's okay, {player_name} we've all been there", "Hanged.", "That was a quick loss, must've been a hard word.", 
			    "Aw man, I believed in you.", "Aaaand you lost, oops.", "It's just a game, probably.", f"Nice try {player_name}, but you failed.", 
			    "Must've been a tough word, you tried at least."]

# lista för olika meddelanden som skrivs ut när spelaren vinner 
correct_rep = [f"Good job, {player_name} you won!", "CORRECT!!", f"You actually got it, {player_name}!", f"You guessed it! Nicely done, {player_name}",
		        f"Well that was easy for you, {player_name}, dictonaries should look out for you!", f"Nice {player_name}, you survived!",
                f"Wooooo! Congrats {player_name}, you got it!"]


# visar stats från display_stats funktionen
display_stats(player_name, player_stats)

# startar spelet
while True: # main loop för spelet, avslutar när använder väljer alternativ 3 (exit) i huvudmenyn

    print("\nMain Menu")
    print("1. Play Hangman")
    print("2. Stats")
    print("3. Exit")
    choice = input("Choose an option (1, 2 or 3): ").strip()


    # om valet är 1, så körs spelet
    if choice == "1":
        word = random.choice(words).lower() # slumpar ett ord från listan
        game_over = random.choice(game_over_rep).lower() # slumpar ett game over meddelande ifall spelaren förlorar 
        correct = random.choice(correct_rep).lower() # slumpar ett vinnar meddelanden ifall spelaren vinner
        

        so_far = "".join(["-" if char != " " else " " for char in word]) # skapar en sträng med lika många "-" som det finns bokstäver i order
        wrong = 0 # räknar antal fel gissningar
        used = [] # lägger till använda bokstäver i en lista
        hint_used = False # initierar att hint_used är false (ändras till True när användaren använder en hint)
    
    

        print("\nGame starting! Type 'hint' for a clue (only once!)") # skriver ut att spelet startar
    

        # går igenom om ett svar är rätt/fel baserat på om spelaren angivit rätt ord eller en bokstav som finns i ordet, samt tar bort en linje om det är varken eller
        while wrong < max_wrong and so_far != word:
            
            print("\n" + "-" * 30) # skriver ut en line för att det ska se bättre ut
            display_hangman(wrong) # skriver ut main hangman listan (stick gubben)
            print(f"\nUsed letters: {','.join(used) if used else 'None'}") # skriver ut använda bokstäver
            print(f"\nWord: {so_far}") # skriver ut hur många bokstäver som använts samt vilka
            guess = input("Enter your guess: ").lower() # spelaren gissar på ett ord eller en bokstav
            clear_screen() # rensar terminalen innan nästa gissning för att det ska se mindre rörigt ut
            
            if guess == "hint": # om spelaren skriver "hint" så får de en ledtråd, och ändrar hint = false till hint = true
                if hint_used:
                    print("You've already used your hint!")
                else:
                    hint_used = True # ändrar hint = false till hint = true 
                    print(get_hint(word, so_far)) # skriver ut ledtråden från get hint funktionen
                continue

            # låter spelare gissa genom att skriva ett helt ord
            if len(guess) > 1: # om längden av gissningen är mer än 1
                if guess == word: # om gissningen matchar ordet så skrivs det ut att spelaren vunnit och startar om (alltså tar dig till meny
                    so_far = word # skriver ut hela order
                    break # stoppar loopen så det kan börja om i menyn
                else: # om ordet är fel : 
                    print(hangedman[wrong]) # skriver ut stick gubben
                    wrong_word = [f"I'm sorry but {guess} is not it",  # lista av fel meddelanden 
                                  f"Unfortunately, {guess} is incorrect", 
                                  f"Oooops, {guess} is not it", 
                                  f"I guess {guess} was a confident guess but, nope",
                                  f"Sorry {guess} is not the word",
                                  f"Almost but not quite, {guess} isn't even close.. or is it?",
                                  f"Ouch, {guess} is not the word",]
                    wrong_w = random.choice(wrong_word) # slumpar ett fel meddelande ur wrong_word listan
                    print(wrong_w) # skriver ut fel meddelandet
                        
                    wrong += 1 # lägger +1 fel i wrong variabeln som räknar fel gissningar
                    continue
            # skriver ut so far alltså hur många bokstäver som använts
            so_far, message = process_guess(guess, word, so_far, used) # kollar oom gissningen är rätt / fel
            print(message)  # skriver ut meddelandet från process_guess funktionen
            # om so far message börjar med att använder skrivit in ett fel 
            if message.startswith("Wrong"): # om meddelandet börjar med wrong så skrivs stickgubben ut
                wrong += 1   # lägger till +1 fel i wrong variablen       
        # skriver ut i en ny linje så det ser bättre ut                 
        print("\n" + "-" * 30)    
        # om användaren vinner skriver det ut ett meddelande och lägger till en vinst i player_stats.json 
        if so_far == word: # om alla bokstäver användaren gissat är rätt så skriver det ut ett meddelande från correct_rep listan 
            print(correct)
            player_stats[player_name]['wins'] += 1 # skriver in +1 vinster till player_stats.json filen i rätt player_name rad
        # om användaren förlorar skriver det ut game over meddelande och uppdaterar player_stats.json med en förlust
        else:
            display_hangman(wrong) 
            print(game_over)
            print(f"the word was: {word}")       
            player_stats[player_name]['losses'] += 1 
        
    # val 2 är att visa stats, alltså visar den upp hur många vinster/förluster kopplade till alla spelar namn
    elif choice == "2":
        for player_name in player_stats: # går igenom player_stats.json namn för namn och skriver ut all statistik, dvs hur många vinster eller förluster 
            display_stats(player_name, player_stats) # skriver ut resultat, alltså listan med alla spelar namn (om det nu finns mer än 1 spelare) och respektive stats
        play_again = input("\nBack to main menu? (yes): ").strip().lower() # skriver ut ett "gå tillbaka till menyn?" meddelande, finns bara svar ja
        
    # om valet är 3 så stängs spelet
    elif choice == "3":   
        print("Thanks for playing!") 
        break
    
# sparar spelarens stats i player_stats.json och sparar tills nästa gång
save_player_stats(player_stats)


    



    

