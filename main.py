#Auhor: Colin Stokes
#Date: 6/24/2025

import random

def print_menu():

    print("----------Welcome to Riracina's Game Picker and Tracker!----------\n\nWhat would you like to do?\n1. Select a subset of games\n2. Finish a game\n\nType \"exit\" to exit the program.")
            

if __name__ == '__main__':

    #variable definitions
    unlocked_games = list() #list of all unlocked games

    game_name : str #name of the game extracted from the total_games file
    locked_status : str #status of the game extracted from the total_games file

    exit_trigger : bool = False #trigger boolean to end the program

    #open the file and read all lines
    with open("Total_Games_List.txt") as total_games:

        all_lines = total_games.readlines() #read all the lines into a list 

    for full_line in all_lines:

        splitLine = full_line.split(", ") #splits the line into name of game and locked or unlocked status

        game_name = splitLine[0]
        locked_status = splitLine[1]

        locked_status = locked_status.strip("\n") #get rid of trailing newline character

        if(locked_status == "unlocked"):
            unlocked_games.append(game_name)
        
    #print(unlocked_games)

    while(not exit_trigger):

        print_menu() #print the program menu

        choice = input("\n>> ")

        choice = choice.lower() #convert string to lowercase to reduce keying errors

        if(choice == "1" or choice == "select"):
            print("\nyou chose select!\n")
            random.seed() #set seed to current system time or whatever your os feels like is best

            selected_games = random.sample(unlocked_games, 20) #generate 20 random games from the list of unlocked games

            for game in selected_games:
                print(game)

        elif(choice == "2" or choice == "finish"):
            print("\nyou chose finish!\n")
        elif(choice == "exit"):
            print("\nyou chose to exit!\n")
            exit_trigger = True
        else:
            print("Invalid input. See the Usage section in the readme for more details")

        #TODO: write Usage section in the readme
        #      Code logic that unlocks the games when the finish option is selected
        #      Make a GUI???? Maybe
        #      Code select logic to return a specified amount of games
        #      Make the program epic and professional and not with debug stuff everywhere