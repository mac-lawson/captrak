import os
from graphics import Graphics
from colorama import Fore

Graphics.init()
# Function to read team data from a text file
def read_team_data(file_path):
    with open(file_path, "r") as file:
        team_data = file.readlines()
    return [line.strip() for line in team_data]

# Function to write team data to a text file
def write_team_data(file_path, team_data):
    with open(file_path, "w") as file:
        for line in team_data:
            file.write(line + "\n")

# Function to add a new team to the database
def add_team(team_name, team_leader, team_size, file_path):
    team_data = read_team_data(file_path)
    team_data.append(f"{team_name}, {team_leader}, {team_size}")
    write_team_data(file_path, team_data)
    print(f"Team {team_name} has been added to the database.")

# Function to remove a team from the database
def remove_team(team_name, file_path):
    team_data = read_team_data(file_path)
    new_team_data = [line for line in team_data if not line.startswith(team_name)]
    if len(new_team_data) == len(team_data):
        print(f"No team with the name {team_name} was found in the database.")
    else:
        write_team_data(file_path, new_team_data)
        print(f"Team {team_name} has been removed from the database.")

# Function to list all teams in the database
def list_teams(file_path):
    team_data = read_team_data(file_path)
    if len(team_data) == 0:
        print(Fore.RED + "There are no teams in the database.\n\n" + Fore.RESET)
    else:
        print("Teams in the database:")
        for line in team_data:
            print(f"- {line}")

# Function to search for teams by team name or leader name
def search_teams(query, file_path):
    team_data = read_team_data(file_path)
    matching_teams = [line for line in team_data if query.lower() in line.lower()]
    if len(matching_teams) == 0:
        print(f"No teams matching '{query}' were found in the database.")
    else:
        print(f"Matching teams:")
        for line in matching_teams:
            print(f"- {line}")
# Main program loop
# while True:

#     # Prompt the user for the action they want to take
#     print("1. Add a new team")
#     print("2. Remove a team")
#     print("3. List all teams")
#     print("4. Search for a team")
#     print("5. Quit")
#     choice = input("Enter your choice (1-5): ")

#     # Take the appropriate action based on the user's choice
#     if choice == "1":

#     elif choice == "2":

#     elif choice == "3":
#     elif choice == "4":

#     elif choice == "5":
#         break
#     else:
#         print("Invalid choice. Please enter a number from 1 to 5.")
