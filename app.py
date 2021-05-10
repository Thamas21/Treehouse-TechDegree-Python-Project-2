import constants

def bball_stats_game():
	# global variables
	new_teams = []
	player_data = []
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
		for items in constants.PLAYERS:
			player_data.append(items)
		for tallness in player_data:
			tallness['height'] = tallness['height'][:3]
			tallness['height'] = int(tallness['height'])
		for xper in player_data:
			if xper['experience'] == 'NO':
				xper['experience'] = False
			if xper['experience'] == 'YES':
				xper['experience'] = True
		return player_data

	clean_data()

	def team_names():
		for i in constants.TEAMS:
			new_teams.append(i)
		return new_teams
	team_names()
# function that prints out each team name in a specific format
	def print_teams():
		counter = 1
		for i in new_teams:
			print(f'{counter}: {i}')
			counter += 1
# function that gives the number of players per team as an integer
	def players_per_team():
		per_team = len(player_data) / len(new_teams)
		return (int(per_team))
	"""functin that creates a new key-value team pair for each player . Honestly 
	I don't really like it. It's clunky and feels like it could be DRYer and more Pythonic
	I kinda got stuck and this is what I came up with
	"""
	def balance_teams(teams, players):
		for player in players[:6]:
			team1.append(player['name'])
		
		for player in players[6:12]:
			team2.append(player['name'])
		
		for player in players[12:]:
			team3.append(player['name'])
		return player
# basketball stats program.
	balance_teams(new_teams, player_data)
	players_per_team()

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
			print(f"\n \n{new_teams[0]} total players: {players_per_team()}")
			print(", ".join(team1))
			proceed = input("\n \nPress enter to continue or enter 'quit' to end program... ")
			proceed = proceed.lower()
			if proceed == "quit":
				break
		elif pick_team == "2":
			print(f" \n \n{new_teams[1]} total players: {players_per_team()}")
			print(", ".join(team2))
			proceed = input("\n \nPress enter to continuer enter 'quit' to end program... ")
			proceed = proceed.lower()
			if proceed == "quit":
				break
		elif pick_team == "3":
			print(f"\n\n{new_teams[2]} total players: {players_per_team()}")
			print(", ".join(team3))
			proceed = input("\n \nPress enter to continuer enter 'quit' to end program... ")
			proceed = proceed.lower()
			if proceed == "quit":
				break

bball_stats_game()