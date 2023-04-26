import random
import time
import os

# function to clear the terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# function to read the logins.txt file
def read_logins():
    logins = {}
    with open('logins.txt') as f:
        for line in f:
            username, password = line.strip().split(',')
            logins[username] = password
    return logins

# function to read the songs.txt file
def read_songs():
    songs = []
    with open('songs.txt') as f:
        for line in f:
            song, artist = line.strip().split(',')
            songs.append((song, artist))
    return songs

# function to read the scores.txt file
def read_scores():
    scores = {}
    with open('scores.txt') as f:
        for line in f:
            username, high_score = line.strip().split(',')
            scores[username] = int(high_score)
    return scores

# function to write a new high score to the scores.txt file
def write_score(username, high_score):
    scores = read_scores()
    scores[username] = high_score
    with open('scores.txt', 'w') as f:
        for username, high_score in sorted(scores.items(), key=lambda x: x[1], reverse=True)[:5]:
            f.write(f"{username},{high_score}\n")

# function to play the game
def play_game(songs):
    score = 0
    lives = 3
    for i in range(1, 11):
        clear()
        print(f"Question {i}/10")
        song, artist = random.choice(songs)
        print(f"Artist: {artist}")
        print(f"Song: {song[0].upper() + '-'*(len(song)-1)}")
        for j in range(2):
            guess = input("Your guess: ")
            if guess.lower() == song.lower():
                print("Correct!")
                if j == 0:
                    score += 3
                else:
                    score += 1
                break
            else:
                print("Incorrect.")
                lives -= 1
                if lives == 0:
                    print("Game over.")
                    return score
                elif j == 0:
                    print(f"You have {lives} lives left. Here's another hint:")
                    print(f"Song: {song[0].upper() + '-'*(len(song)-1)}")
                    time.sleep(2)
    return score

# main program
logins = read_logins()
username = input("Username: ")
password = input("Password: ")
if username in logins and logins[username] == password:
    clear()
    print(f"Welcome, {username}!")
    input("Press Enter to start the game...")
    clear()
    print("Loading...")
    time.sleep(7)
    songs = read_songs()
    score = play_game(songs)
    print(f"Total score: {score}")
    write_score(username, score)
    print("Top 5 Scores:")
    for i, (username, high_score) in enumerate(sorted(read_scores().items(), key=lambda x: x[1], reverse=True)[:5]):
        print(f"{i+1}. {username}: {high_score}")
else:
    print("Incorrect username or password.")
