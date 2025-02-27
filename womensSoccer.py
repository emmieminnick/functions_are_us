# Emmie Minnick
# This program will ask for the home team's name and the number of games, 
# generate random scores for each game, and store the results in a dictionary. 
# It will then display the scores, the final season record, and a final message 
# based on the team's performance.

import random

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

# Function to determine the result of the game
def determine_result(home_score, away_score) :
    if home_score > away_score :
        return 'W'
    else :
        return 'L'
    
# This is the main function
def main() :
    # Get the home team name and number of games
    home_team = input("Enter the name of your team: ").upper()
    num_games = int(input("Enter the number of teams that " + home_team + " will play: "))

    # Dictionary to store game information
    games = {}
    wins = 0
    losses = 0

    # Loop through game
    for iCount in range(1, num_games + 1) :
        away_team = input("Enter the name of the away team for game " + str(iCount)  + ": ").upper()

        # Generate scores and ensure no ties
        while True :
            home_score = generate_score()
            away_score = generate_score()
            if home_score != away_score :
                break
        
        # Determine result and update win/loss count
        result = determine_result(home_score, away_score)
        if result == 'W' :
            wins += 1
        else :
            losses += 1

        # Store game information in dictionary
        games[f"Game {iCount}"]= {
            "Home Team": home_team,
            "Home Score": home_score,
            "Away Team": away_team,
            "Away Score": away_score,
            "Result": result
        }

    # Print game information
    for game, info in games.items() :
        print(f"{game}: {info['Home Team']} {info['Home Score']} - {info['Away Team']} {info['Away Score']} ({info['Result']})")
        
    # Print season record
    print(f"Final season record: {home_team} {str(wins) + "-" + str(losses)}")

    # Print final message
    total_games = wins + losses
    win_percentage = wins/total_games

    if win_percentage >= 0.75 :
        print("Qualified for the NCAA Women's Soccer Tournament")
    elif win_percentage >= 0.50 :
        print("You had a good season")
    else :
        print("Your team needs to practice!")

# Run the main function
if __name__ == "__main__":
    main()