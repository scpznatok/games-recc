import sqlite3
import random


conn = sqlite3.connect("games.db")

cursor = conn.cursor()

cursor.execute("SELECT * FROM games")
games = cursor.fetchall()

def get_random_game(games):
    if not games:
        return "У базі даних немає ігор."

    random_game = random.choice(games)
    game_name = random_game[1]
    genre = random_game[2]
    year = random_game[3]
    studio = random_game[4]

    recommendation = f"Спробуйте гру '{game_name}' в жанрі '{genre}', випущену у {year} році від студії '{studio}'."
    return recommendation


recommendation = get_random_game(games)
print(recommendation)


conn.commit()
