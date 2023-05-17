Oliver Smith's Music guessing game!

This program is a guess the song game where the user needs to guess the name of a song based on hints provided. The program keeps track of the user's score and displays a scoreboard of the top five scores at the end of the game. The user's login information is stored in a file, and the highest score achieved by each user is recorded in another file.

Features:
- User login: The program prompts the user for a username and password. If the login information is correct, the game starts. Otherwise, a new login is created.
- The Game: The program randomly selects a song from a list and provides a hint in the format "Artist - First letter of the song". The user has two chances to guess the song name. If the user guesses correctly on the first try, they receive 3 points. If they guess correctly on the second try, they receive 1 point. The user has 3 lives, and if they run out of lives, the game ends.
- Scoreboard: After the game ends, the user's score is recorded in a scoreboard file. The program displays the top five scores from the scoreboard.

Files:
- `logins.txt`: Stores the user login information in the format "username,password".
- `songs.txt`: Contains the list of songs and their corresponding artists in the format "songname,artistname".
- `scores.txt`: Keeps track of the user's highest scores in the format "username,score".

Usage:
1. Run the program.
2. If you have an existing account, enter your username and password to create an account
3. If you don't have an account or your login information is incorrect, a new account will be created.
4. The game starts, and you will be provided with a hint for a song. Guess the song name based on the hint.
5. You have two chances to guess the song. If you guess correctly on the first try, you receive 3 points. If not, you have one more chance to guess and receive 1 point if correct.
6. The game continues with new songs until you run out of lives or all songs are guessed.
7. At the end of the game, your score is recorded in the scoreboard, and the top five scores are displayed.

Please make sure to have the necessary files (`logins.txt`, `songs.txt`, and `scores.txt`) in the same directory as the program script.
