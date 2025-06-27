#Auhor: Colin Stokes
#Date: 6/24/2025

import random

SPREADSHEET_LINK = "https://docs.google.com/spreadsheets/d/1FhdPQ60erFwbJ1hVjo_Y96p_AgVF0qJo5LXag9CQHOY"

#function that prints the main menu of the program
def print_menu():

    print("----------Welcome to Riracina's Game Picker and Tracker!----------\n\nWhat would you like to do?\n1. Select a subset of games\n2. Finish a game\n\nType \"exit\" to exit the program.")

#function that prints the game selection
def print_selected_games(selected_games : list):
    print(f"\nYour {len(selected_games)} selected games:\n-------------------------")

    for game in selected_games:
        print(game)
    
    print("-------------------------\n")
            

if __name__ == '__main__':

    #variable definitions
    unlocked_games = list() #list of all unlocked games
    total_games_list = list() #list of all games total
    prereq_games = list() #list of all prereq games
    newly_unlocked_games = list() #list of all newly unlocked games
    prereq_list = list() #list of all prereqs
    prereq_list_index = list()
    AND_flag_list = list()
    other_prereq_list = list()

    game_name : str #name of the game extracted from any games file
    locked_status : str #status of the game extracted from the total_games file
    prereq_game : str #name of prereq game
    finished_game : str #name of finished game

    exit_trigger : bool = False #trigger boolean to end the program
    valid_integer : bool = False #trigger boolean to end the selection number loop
    valid_game : bool = False #trigger boolean to end the game selection loop
    AND_flag : bool = False #boolean to say that there was an AND prereq
    found_line : bool = False #boolean to trigger end of while loop for finding the correct line to modify
    is_prereq : bool = False #boolean that denotes whether finished game is a prereq or not

    counter : int #counter variable

    while(not exit_trigger):

        unlocked_games.clear()
        total_games_list.clear()

        #open the file and read all lines
        with open("Total_Games_List.txt", "r", encoding="utf-8") as total_games_file:

            total_games_all_lines = total_games_file.readlines() #read all the lines into a list 
            total_games_file.close()

        for full_line in total_games_all_lines:

            splitLine = full_line.split(", ") #splits the line into name of game and locked or unlocked status

            game_name = splitLine[0]
            locked_status = splitLine[1]

            total_games_list.append(game_name)

            locked_status = locked_status.strip("\n") #get rid of trailing newline character

            if(locked_status == "unlocked"):
                unlocked_games.append(game_name)

        print_menu() #print the program menu

        choice = input("\n>> ")

        choice = choice.lower() #convert string to lowercase to reduce keying errors

        if(choice == "1" or choice == "select"):
            print("\nyou chose select!\n")
            random.seed() #set seed to current system time or whatever your os feels like is best

            valid_integer = False

            #loop to keep prompting until a valid integer is inputted
            while(not valid_integer):
                try:

                    select_num = int(input("How many games would you like to select?\n>> ")) #throws an error if a non-integer is passed
                    valid_integer = True

                except: #catches the error
                    print("\n!!---Invalid input. Please pass an integer value to the program---!!\n")

            selected_games = random.sample(unlocked_games, select_num) #generate an amount of random games from the list of unlocked games

            print_selected_games(selected_games)

        elif(choice == "2" or choice == "finish"):

            prereq_list.clear()

            #read all lines into a list
            with open("Locked_Games_List.txt", "r", encoding="utf-8") as locked_file:
                locked_games_all_lines = locked_file.readlines()
                locked_file.close()
            
            #build the locked games dictionary
            for full_line in locked_games_all_lines:

                splitLine = full_line.split(", ")

                game_name = splitLine[0]
                prereq_game_line = splitLine[1]

                prereq_game_line = prereq_game_line.strip("\n")

                prereq_list.append(prereq_game_line)
                
            valid_game = False

            while(not valid_game):

                finished_game = input("What game did you finish? >> ")

                if finished_game in total_games_list:
                    print("\nGame Found! Adding game to Finished_Games_List.txt...\n")
                    print(f"Congrats on completing {finished_game}!\n")
                    valid_game = True

                    with open("Finished_Games_List.txt", "a", encoding="utf-8") as finished_file:
                        finished_file.write(finished_game + "\n")
                        finished_file.close()

                    prereq_list_index.clear()
                    other_prereq_list.clear()
                    AND_flag_list.clear()
                    counter = 0
                    is_prereq = False
                    while(counter < len(prereq_list)):
                        split2 = prereq_list[counter].split("++")
                        if(finished_game in split2):
                            prereq_list_index.append(counter)
                            is_prereq = True
                            if len(split2) > 1:
                                AND_flag_list.append(True)
                                if finished_game == split2[0]:
                                    other_prereq_list.append(split2[1])
                                else:
                                    other_prereq_list.append(split2[0])
                            else:
                                print("testing")
                                print(len(prereq_list_index))
                                AND_flag_list.append(False)
                        else:
                            split2 = prereq_list[counter].split("|")
                            if(finished_game in split2):
                                prereq_list_index.append(counter)
                                is_prereq = True
                                AND_flag_list.append(False)
                    
                        counter += 1
                    
                    if is_prereq:

                        for i in range(len(prereq_list_index)):

                            game_name = locked_games_all_lines[prereq_list_index[i]].split(", ")[0]
                        
                            if AND_flag_list[i]:
                                locked_games_all_lines[prereq_list_index[i]] = f"{game_name}, {other_prereq_list[i]}\n"
                            else:
                                locked_games_all_lines.pop(prereq_list_index[i])

                                if(i + 1 in range(len(prereq_list_index))):
                                    prereq_list_index[i + 1] -= 1

                            found_line = True

                            if not AND_flag_list[i]:
                                print(f"~~~~~~~~~~You unlocked {game_name}!~~~~~~~~~~\n")

                                found_line = False
                                counter = 0

                                while(not found_line):

                                    if total_games_list[counter] == game_name:
                                        total_games_all_lines[counter] = f"{game_name}, unlocked\n"
                                        found_line = True

                                    counter += 1


                        with open("Locked_Games_List.txt", "w", encoding="utf-8") as locked_games_file:
                                locked_games_file.writelines(locked_games_all_lines)

                        with open("Total_Games_List.txt", "w", encoding="utf-8") as total_games_file:
                                    total_games_file.writelines(total_games_all_lines)
                        
                else:
                    print(f"\nInvalid game name, consider copy pasting the game directly from the spreadsheet.\nlink: {SPREADSHEET_LINK}\n")


                
        elif(choice == "exit"):
            print("\nHave a good day! Byeeee!\n")
            exit_trigger = True
        else:
            print("Invalid input. See the Usage section in the readme for more details")

        #TODO: write Usage section in the readme
        #      Code logic that unlocks the games when the finish option is selected
        #      Make a GUI???? Maybe
        #      Make the program epic and professional and not with debug stuff everywhere