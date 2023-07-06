import random
import os
import shutil
import getpass

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
    password = getpass.getpass("Enter your password: ")
    write_line("logins.txt", f"{username},{password}")

# Function to check if a username and password match a stored login
def check_login(username, password):
    logins = read_file("logins.txt")
    if f"{username},{password}" in logins:
        return True
    else:
        return False

# Function to update the scoreboard with a user's score
def update_scoreboard(username, score):
    scores = read_file("scores.txt")
    user_scores = [line.split(",") for line in scores if line.startswith(username)]
    if user_scores:
        highest_score = max(int(user_score[1]) for user_score in user_scores)
        if score > highest_score:
            for user_score in user_scores:
                if int(user_score[1]) < score:
                    user_score[1] = str(score)
    else:
        user_scores = [[username, str(score)]]
    scores = [",".join(user_score) for user_score in user_scores] + [line for line in scores if not line.startswith(username)]
    with open("scores.txt", "w") as f:
        f.write("\n".join(scores))


# Function to display the top five scores in the scoreboard
def display_scoreboard():
    scores = read_file("scores.txt")
    user_scores = [line.split(",") for line in scores]
    user_scores.sort(key=lambda x: (x[1]), reverse=True)
    print("\nTop 5 Scores:")
    print("----------------")
    for i in range(min(len(user_scores), 5)):
        print(f"{user_scores[i][0]} - {user_scores[i][1]}")
    print("\n")

# Function to display the main menu
def display_menu():
    menu = """
    
   ______                        ________    _                  
  / ____/___ _____ ___  ___     /_  __/ /_  (_)___  ____ ___  __
 / / __/ __ `/ __ `__ \/ _ \     / / / __ \/ / __ \/ __ `/ / / /
/ /_/ / /_/ / / / / / /  __/    / / / / / / / / / / /_/ / /_/ / 
\____/\__,_/_/ /_/ /_/\___/    /_/ /_/ /_/_/_/ /_/\__, /\__, /  
                                                 /____//____/   


1. Play Game
2. Create Account
3. Leaderboard
4. Exit"""
    print(menu)

# Function to center align text
def center_align(text):
    columns, _ = shutil.get_terminal_size()
    padding = (columns - len(text)) // 2
    return " " * padding + text

# Function to display the menu in the center of the screen
def display_centered_menu():
    clear_screen()
    menu = """
  
   ______                        ________    _                  
  / ____/___ _____ ___  ___     /_  __/ /_  (_)___  ____ ___  __
 / / __/ __ `/ __ `__ \/ _ \     / / / __ \/ / __ \/ __ `/ / / /
/ /_/ / /_/ / / / / / /  __/    / / / / / / / / / / /_/ / /_/ / 
\____/\__,_/_/ /_/ /_/\___/    /_/ /_/ /_/_/_/ /_/\__, /\__, /  
                                                 /____//____/   


1. Play Game
2. Create Account
3. Leaderboard
4. Exit"""
    print(center_align(menu))

# Function to play the guess the song game
def play_game(username):
    songs = read_file("songs.txt")
    lives = 3
    score = 0
    clear_screen()
    print(f"""Welcome to
   ______                        ________    _                  
  / ____/___ _____ ___  ___     /_  __/ /_  (_)___  ____ ___  __
 / / __/ __ `/ __ `__ \/ _ \     / / / __ \/ / __ \/ __ `/ / / /
/ /_/ / /_/ / / / / / /  __/    / / / / / / / / / / /_/ / /_/ / 
\____/\__,_/_/ /_/ /_/\___/    /_/ /_/ /_/_/_/ /_/\__, /\__, /  
                                                 /____//____/   """)
    while len(songs) > 0 and lives > 0:
        song = random.choice(songs)
        songs.remove(song)
        song_name, artist_name = song.split(",")
        hint = f"{artist_name} - {song_name[0]}"
        print(f"\nHint: {hint}")
        guess = input("What is the name of this song? ")
        if guess.lower() == song_name.lower():
            score += 3
            print("Correct! You earned 3 points.")
        else:
            lives -= 1
            if lives == 0:
                print(f"Incorrect. You have run out of lives. The answer was {song_name}.")
            else:
                print(f"Incorrect. You have {lives} lives.")
    return score

# Main program
def main():
    clear_screen()
    display_centered_menu()
    while True:
        option = input("")
        if option == "1":
            clear_screen()
            username = input("Enter your username: ")
            password = getpass.getpass("Enter your password: ")
            if check_login(username, password):
                score = play_game(username)
                update_scoreboard(username, score)
            else:
                print("Incorrect username or password. Please try again.")
        elif option == "3":
            clear_screen()
            display_scoreboard()
        elif option == "2":
            clear_screen()
            get_login()
            print("Account created successfully!")
        elif option == "4":
            clear_screen()
            print("""Thank you for playing 
   ______                        ________    _                  
  / ____/___ _____ ___  ___     /_  __/ /_  (_)___  ____ ___  __
 / / __/ __ `/ __ `__ \/ _ \     / / / __ \/ / __ \/ __ `/ / / /
/ /_/ / /_/ / / / / / /  __/    / / / / / / / / / / /_/ / /_/ / 
\____/\__,_/_/ /_/ /_/\___/    /_/ /_/ /_/_/_/ /_/\__, /\__, /  
                                                 /____//____/   
""")
            break
        else:
            print("Invalid option. Please try again.")

# Run the main program
if __name__ == "__main__":
    main()
