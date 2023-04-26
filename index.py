import random
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

# function to write a new login to the logins.txt file
def write_login(username, password):
    with open('logins.txt', 'a') as f:
        f.write(f"{username},{password}\n")

# function to read the songs.txt file
def read_songs():
    songs = []
    with open('songs.txt') as f:
        for line in f:
            song, artist = line.strip().split(',')
            songs.append((song, artist))
    return songs

# function to play the game
def play_game(songs):
    score = 0
    lives = 3
    for i in range(10):
        clear()
        song, artist = random.choice(songs)
        print(f"Question {i+1}:")
        print(f"Artist: {artist}")
        print(f"Song: {song[0]}{'_'*(len(song)-1)}")
        guess = input("What's the name of the song? ")
        if guess.lower() == song.lower():
            score += 3
            print("Correct! You earned 3 points.")
        else:
            lives -= 1
            print(f"Incorrect. You have {lives} lives left.")
            guess = input("What's the name of the song? ")
            if guess.lower() == song.lower():
                score += 1
                print("Correct! You earned 1 point.")
            else:
                lives -= 1
                print(f"Incorrect. You have {lives} lives left.")
        if lives == 0:
            print("Game over. You lost all your lives.")
            break
    else:
        print("Congratulations! You finished the game.")
    return score

# main program
logins = read_logins()
username = input("Username: ")
password = input("Password: ")
if username in logins and logins[username] == password:
    clear()
    print(f"Welcome, {username}!")
    songs = read_songs()
    score = play_game(songs)
    print(f"Total score: {score}")
else:
    print("Invalid username or password.")
    write_login(username, password)
    print("New login created.")
