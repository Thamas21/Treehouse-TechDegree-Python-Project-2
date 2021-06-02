
import constants
import copy

# copy from https://www.geeksforgeeks.org/copy-python-deep-copy-shallow-copy/

def basketball_stats():
	# variables
	new_teams = copy.deepcopy(constants.TEAMS)
	player_data = copy.deepcopy(constants.PLAYERS)
	pick_team = ''
	team1 = []
	team2 = []
	team3 = []

	# Display function creates an opening message 

	def opening_display():
		opening_message = "\n\nbasketball team stats tool\n"
		opening_message = opening_message.upper()
		print(opening_message)
		menu = "MENU"
		dashs = '-' * len(menu)
		menu = "\n" + dashs + menu + dashs
		options = "\n\nHere are you choices:" 
		disply_stats = "\n\nA) Display Team Stats"
		quit_program = "\n\nB) Quit"
		#enter_option = input("Enter Option A or B: ") is placed outside of this function because it really handles logic
		options += disply_stats + quit_program + "\n\n"
		print(menu + options)


	#functions that provide program logic

	# clean_data function appends constants from constants.py
	# nests each players' data dictionary in a list called player_data
	# loops through each player in player_data to make ['height'] an integer for each player
	# clean_data function also uses a loop to change each players ['expereience'] to a boolean value
	""" I fully recognize that the variables have silly names the example below seemed excessively confusing.
					for height in player_data:
						height['height'] = height['height'][:3]
						height['height'] = int(height['height'])
	"""
	def clean_data():
		for tallness in player_data:
			tallness['height'] = tallness['height'][:3]
			tallness['height'] = int(tallness['height'])
		for exp in player_data:
			if exp['experience'] == 'NO':
				exp['experience'] = False
			if exp['experience'] == 'YES':
				exp['experience'] = True
		return player_data

	clean_data()

	# function that prints out each team name in a specific format I like numbers
	# more than letters feels cleaner for some reason.
	def print_teams():
		counter = 1
		for i in new_teams:
			print(f'{counter}: {i}')
			counter += 1
	# function that gives the number of players per team as an integer
	def players_per_team():
		per_team = len(player_data) / len(new_teams)
		return (int(per_team))
	players_per_team()
	"""function that appends a set range, using scile not range, to append player names 
	to a list so they can be printed in the proper style according to instructions
	if more teams or players are added you will need to update the teams variables at
	the top of the program(if more teams are added) if more players are added you will need 
	to adjust your slice based on players_per_team function. I feel like there is probably
	a cleaner way of doing this.  
	"""
	def balance_teams(teams, players):
		for player in players[:6]:
			team1.append(player['name'])

		for player in players[6:12]:
			team2.append(player['name'])
		
		for player in players[12:]:
			team3.append(player['name'])
		return player

	balance_teams(new_teams, player_data)
	# basketball stats program.


	opening_display()
	enter_option = input("Enter Option A or B: ")
	enter_option = enter_option.lower()

	while enter_option != 'a' or enter_option != 'b':
		if enter_option == 'b':
			print("Program Ending")
			break
		elif enter_option == 'a':
			print("\n \nPlease pick a team:")
			print_teams()
			pick_team = input("\n \nEnter an option: ")
			
		else:
			enter_option = input("I couldn't quite get that, please re-enter (A/B): ")
			enter_option = enter_option.lower()

		if pick_team == "1":
			print(f"\n \n{new_teams[0]} total players: {players_per_team()} \n")
			print(", ".join(team1))
			proceed = input("\n \nPress enter to continue or enter 'quit' to end program... ")
			proceed = proceed.lower()
			if proceed == "quit":
				break
		elif pick_team == "2":
			print(f" \n \n{new_teams[1]} total players: {players_per_team()} \n")
			print(", ".join(team2))
			proceed = input("\n \nPress enter to continuer enter 'quit' to end program... ")
			proceed = proceed.lower()
			if proceed == "quit":
				break
		elif pick_team == "3":
			print(f"\n\n{new_teams[2]} total players: {players_per_team()} \n")
			print(", ".join(team3))
			proceed = input("\n \nPress enter to continuer enter 'quit' to end program... ")
			proceed = proceed.lower()
			if proceed == "quit":
				break

if __name__ == "__main__":
	basketball_stats()