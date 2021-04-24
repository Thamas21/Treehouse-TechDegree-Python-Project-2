import constants

def bball_stats_game():
	
	new_teams = []
	player_data = []


	# funtions that provide program display

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

	def print_teams():
		counter = 1
		for i in new_teams:
			print(f'{counter}: {i}')
			counter += 1

	def players_per_team():
		per_team = len(player_data) / len(new_teams)
		return (int(per_team))

	def balance_teams(teams, players):
		for player in players[:6]:
			player['team'] = teams[0]

		for player in players[6:12]:
			player['team'] = teams[1]

		for player in players[12:]:
			player['team'] = teams[2]
		return player	 
# basketball stats program.
	balance_teams(new_teams, player_data)
	players_per_team()

	opening_display()
	enter_option = input("Enter Option A or B: ")
	enter_option = enter_option.lower()
	pick_team = ''
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

	#while pick_team != '1' or pick_team != '2' or pick_team != '3':
		if pick_team == "1":
			print(f"\n \n{new_teams[0]} total players: {players_per_team()}")
			for name in player_data:
				if name['team'] == 'Panthers':
					print(name['name'])
			proceed = input("\n \nPress enter to continue or enter 'quit' to end program... ")
			proceed = proceed.lower()
			if proceed == "quit":
				break
		elif pick_team == "2":
			print(f" \n \n{new_teams[1]} total players: {players_per_team()}")
			for name in player_data:
				if name['team'] == 'Bandits':
					print(name['name'])
			proceed = input("\n \nPress enter to continuer enter 'quit' to end program... ")
			proceed = proceed.lower()
			if proceed == "quit":
				break
		elif pick_team == "3":
			print(f"\n\n{new_teams[2]} total players: {players_per_team()}")
			for name in player_data:
				if name['team'] == 'Warriors':
					print(name['name'])
			proceed = input("\n \nPress enter to continuer enter 'quit' to end program... ")
			proceed = proceed.lower()
			if proceed == "quit":
				break

bball_stats_game()