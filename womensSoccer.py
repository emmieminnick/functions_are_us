# Emmie Minnick
# This program will ask for the home team's name and the number of games, 
# generate random scores for each game, and store the results in a dictionary. 
# It will then display the scores, the final season record, and a final message 
# based on the team's performance.

import random

# STEP 4: Plays the game and updates the team record
def playGame (home_team, away_team, wins, losses) :
    while True :
        home_score = random.randint(1,5)
        away_score = random.randint(1,5)
        if home_score != away_score :
            break
        
    # Determine result and update win/loss count
    result = determine_result(home_score, away_score)
    if home_score > away_score:
        result = 'W'
    else:
        result = 'L'
    return result, wins, losses

# STEP 5: calculates and displays final record
def display_final_record(home_team, wins, losses):
    print(f"\nFinal Season Record for {home_team}: {wins} - {losses}")
    win_percentage = wins / (wins + losses)
    if win_percentage >= 0.75:
        print("Qualified for the NCAA Women's Soccer Tournament")
    elif 0.50 <= win_percentage <= 0.74:
        print("You had a good season")
    else:
        print("Your team needs to practice!")

def choose_team(games):
    print({info['Home Team']})
    for game, info in games.items():
        print({info['Away Team']})

    while True:
        sChoice = int(input("Choose a team"))
        selected_team = games.pop(sChoice-1)  
        return selected_team

# Function to generate a random number
def generate_score() :
    return random.randrange(0, 10)

def menu() :
    print("Main Menu\n\n1. Choose your home team\n2. Play opponent team\n3. Show final record\n4. Quit\n")

    userChoice = int(input("Enter an option (1-4): "))

    while (userChoice < 0) or (userChoice > 4) :
        userChoice = int(input("\nPlease enter a valid option (1-4): "))

    return userChoice

# Function to determine the result of the game
def determine_result(home_score, away_score) :
    if home_score > away_score :
        return 'W'
    else :
        return 'L'

def introduction() :
    print("Welcome to the game! You will be prompted to enter your name. Then, you will choose a home team and opponent using a menu and generate random scores to display the team's final record.")
def get_name() :
    user_name = input("Please enter your name: ").capitalize()
    return user_name

# This is the main function
def main() :

# Dictionary to store game information
    games = {}
    wins = 0
    losses = 0

    introduction()
    user_name = get_name()
    print(f"Hello, {user_name}! Welcome to the game.")

    # Get the home team name and number of games
    home_team = input("Enter the name of your team: ").upper()
    num_games = int(input("Enter the number of teams that " + home_team + " will play: "))

    # Loop through game
    for iCount in range(1, num_games + 1) :
        away_team = input("Enter the name of the away team for game " + str(iCount)  + ": ").upper()

        result, home_score, away_score = playGame(home_team, away_team, wins, losses)

        # Store game information in dictionary
        games[f"Game {iCount}"]= {
            "Home Team": home_team,
            "Home Score": home_score,
            "Away Team": away_team,
            "Away Score": away_score,
            "Result": result
        }

        if result == 'W':
            wins += 1
        else:
            losses += 1

    # Print game information
    for game, info in games.items() :
        print(f"{game}: {info['Home Team']} {info['Home Score']} - {info['Away Team']} {info['Away Score']} ({info['Result']})")
        
    # Print season record
    print(f"Final season record: {home_team} {str(wins) + "-" + str(losses)}")

# Run the main function
if __name__ == "__main__":
    main()