import os
import json

player_history_file = "player_stats.json"

def load_player_stats():
    if os.path.exists(player_history_file):
        with open(player_history_file, "r") as file:
            return json.load(file)
    return{}

def save_player_stats(player_stats):
    with open(player_history_file, "w") as file:
        json.dump(player_stats, file, indent=4)

player_stats = load_player_stats()

player_name = input("Gib name: ")
print(f"Hi {player_name}! Welcome to hangmansdn")

if player_name not in player_stats:
    player_stats[player_name] = {"wins": 0, "losses": 0}
    print("\nNew player added")


print(f"\n{player_name}'s stats")
print(f"wins: {player_stats[player_name]['wins']}, losses: {player_stats[player_name]["losses"]}")


game_result = input("\nWin or lose=: ").lower()
if game_result == "win":
    player_stats[player_name]["wins"] += 1
    print(f"Congrats {player_name}, you won")
elif game_result == "lose":
    player_stats[player_name]["losses"] += 1
    print(f"lol skill issue")

save_player_stats(player_stats)

