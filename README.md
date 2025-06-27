# Riracina's 3ds marathon game picker program

    Author: Colin Stokes

## Description

    Riracina needs a program that returns an amount of games from the total games list that aren't locked or finished. This program manages the games list and returns random games for her.

    See the stream here!: https://www.twitch.tv/riracina

## File Explainations

    I created some database files. Here are the explainations for the conventions used in these files.

### Locked_Games_List.txt

    This file keeps track of all games that are locked and their prerequesites. I have seperated the the game that is locked and the game that locks it by using a comma. The game that is locked is on the left of the comma and the game that locks it is on the right of the comma.

    example: 

        locked_game, prerequesite_game
    
    For games that have an OR prerequesite (like a lot of pokemon games) I used a pipe | operator to denote that there are 2 (or more) games that can unlock that game.

    example:

        locked_game, prereq_1|prereq_2
    
    For games that had an AND prerequesite, I used a ++ operator to denote that there are 2 games that need to be finished to unlock that game

    example:

        locked_game, prereq_1++prereq_2

### Total_Games_List.txt

    For each game in the spreadsheet, I ported them here. To denote whether the game was locked or unlocked, I added the word "unlocked" or "locked" to each game after a comma. When a game becomes unlocked, it will switch from locked to unlocked to denote the change. 

    example:

        ds_game, unlocked

        OR

        ds_game, locked

    I also use this file to denote whether the game is finished or not. I do this by replacing unlocked or locked with the word "finished".

    example:

        ds_game, finished

### Finished_Games_List.txt

    When a game is finished, it will be added to a line in this file. Pretty simple.

    example:

        finished_game1
        finished_game2
        finished_game3

## Usage

    For now: Run the python script however you can in the folder with all of the .txt files. When prompted with the menu:

    ----------Welcome to Riracina's Game Picker and Tracker!----------

    What would you like to do?
    1. Select a subset of games
    2. Finish a game
    
    Type "exit" to exit the program.

    >> 

    Type the number of the option you would like into your keyboard and hit enter.

    "Select a subset of games" allows the user to generate a list of however many games they wish from the list of unlocked games for use however they wish.
    After selecting this option, you will be propmpted to enter an integer. If you choose an integer that is less than 1 or greater than the max number of unlocked games, it will default to either 1 or the max amount of unlocked games respectively.

    The second option is to log finishing a game. This will mark the game as finished and will no longer be eiligible for selection again. This will also automatically unlock games that are locked by it. 
