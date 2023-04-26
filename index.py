import random
import os

# Function to read a file and return its contents as a list
def read_file(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
    return [line.strip() for line in lines]

# Function to write a line to a file
def write_line(filename, line):
    with open(filename, "a") as f:
        f.write(line + "\n")

# Function to clear the terminal screen
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

# Function to get a username and password from the user and store it in a file
def get_login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    write_line("logins.txt", f"{username},{password}")

# Function to check if a username and password match a stored login
def check_login(username, password):
    logins = read_file("logins.txt")
    if f"{username},{password}" in logins:
        return True
    else:
        write_line("logins.txt", f"{username},{password}")
        return False

# Function to play the guess the song game
def play_game(username):
    songs = read_file("songs.txt")
    lives = 3
    points = 0
    clear_screen()
    print(f"Welcome to Guess the Song, {username}!")
    while len(songs) > 0 and lives > 0:
        song = random.choice(songs)
        songs.remove(song)
        song_name, artist_name = song.split(",")
        hint = f"{artist_name} - {song_name[0]}"
        print(f"\nHint: {hint}")
        guess = input("What is the name of this song? ")
        if guess.lower() == song_name.lower():
            points += 3
            print("Correct! You earned 3 points.")
        else:
            lives -= 1
            if lives == 0:
                print(f"Incorrect. You have run out of lives. The answer was {song_name}.")
            else:
                print(f"Incorrect. You have {lives} lives remaining. Try again.")
                guess = input("What is the name of this song? ")
                if guess.lower() == song_name.lower():
                    points += 1
                    print("Correct! You earned 1 point.")
                else:
                    lives -= 1
                    if lives == 0:
                        print(f"Incorrect. You have run out of lives. The answer was {song_name}.")
                    else:
                        print(f"Incorrect. You have {lives} lives remaining. The answer was {song_name}.")
    print(f"\nGame over. You earned {points} points.")
    update_scoreboard(username, points)

# Function to update the scoreboard with a user's score
def update_scoreboard(username, score):
    scores = read_file("scores.txt")
    user_scores = [line.split(",") for line in scores if line.startswith(username)]
    if user_scores:
        highest_score = max(int(user_score[1]) for user_score in user_scores)
        if score > highest_score:
            user_scores = [[username, str(score)]] + [user_score for user_score in user_scores if int(user_score[1]) < score]
        else:
            return
    else:
        user_scores = [[username, str(score)]]
    scores = [",".join(user_score) for user_score in user_scores] + [line for line in scores if not line.startswith(username)]
    with open("scores.txt", "w") as f:
        f.write("\n".join(scores))

# Main program
while True:
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if check_login(username, password):
        clear_screen()
        play_game(username)
        break
    else:
        print("Incorrect login. Please try again.")


