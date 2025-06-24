#Auhor: Colin Stokes
#Date: 6/24/2025

if __name__ == '__main__':
    print("epic")

    with open("Total_Games_List.txt") as file:

        all_lines = file.readlines()

        for line in all_lines:
            print(line)