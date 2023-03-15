import os
import sys
import GTM

# Define the menu options
options = ["Add a new team", "Remove a team", "List all teams", "Search for a team", "Quit"]
selected_option = ""

# Event loop to process events and update window
while selected_option != "Quit":
    # Clear the screen
    os.system("clear" if os.name == "posix" else "cls")

    # Display the menu options
    print("CAPTrak - Civil Air Patrol Ground Team Management")
    print("=" * 30)
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")
    print("=" * 30)

    # Get the user's input
    selected_option = input("Select an option: ")

    # Process the user's input
    if selected_option == "1":
        team_name = input("Enter the name of the new team: ")
        team_leader = input("Enter the name of the team leader: ")
        team_size = input("Enter the size of the team: ")
        GTM.add_team(team_name, team_leader, team_size, "./data/Teams.txt")
        # TODO: Implement the logic for adding a new team
    elif selected_option == "2":
        team_name = input("Enter the name of the team to remove: ")
        GTM.remove_team(team_name, "./data/Teams.txt")
        # TODO: Implement the logic for removing a team
    elif selected_option == "3":
        GTM.list_teams("./data/Teams.txt")
        # TODO: Implement the logic for listing all teams
    elif selected_option == "4":
        query = input("Enter the name or leader name of the team to search for: ")
        GTM.search_teams(query, "./data/Teams.txt")
        # TODO: Implement the logic for searching for a team
    elif selected_option == "5":
        sys.exit()
    elif selected_option == "Quit":
        print("Goodbye!")
    else:
        print("Invalid option. Please try again.")
    input("Press enter to continue...") # Pause the program and wait for user input before clearing the screen and showing the menu again
