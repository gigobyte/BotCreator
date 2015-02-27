from bot import Bot
	
if __name__ == '__main__':
	bot = Bot()
	print "Welcome to the BotCreator commandline"
	while 1:
		input = raw_input(">> ")
		if input == 'reset':
			answer = raw_input(">> Are you sure (this will remove all commands) ? (y/n) ")
			if answer == 'y':
				bot = Bot()
				print ">> Bot reset"

		elif 'load ' in input:
			try: var = input.split()[1]
			except IndexError: print "Invalid file"
			else: bot.load_commands(input.split()[1])

		elif input == 'add click':
			pos = bot.get_click()
			bot.add_command('click', pos)
			print ">> Click added"
		
		"""
		elif input == 'add trigger':
			trigger_key = raw_input(">> Trigger key: ")
			if not bot.is_valid_key(trigger_key):
				print ">> Invalid key"
			else:
				print ">> Trigger added"
		"""
		elif input == 'add string':
			text = raw_input(">> Text: ")
			times = raw_input(">> Repeats: ")
			try:
				int(times)
			except ValueError:
				times = 1
				print ">> Invalid input"
			
			if int(times) > 1:
				interval = raw_input(">> Interval (in secs): ")
			else:
				interval = '0'
			bot.add_command('type', [text,times,interval])
			print ">> String added"

		elif 'run ' in input or input == 'run':
			if bot.commands_empty():
				print ">> Nothing to run."
			else:
				try: times = int(input.split()[1])
				except (ValueError, IndexError): times = 1

				bot.print_commands()
				if times > 0:
					answer = raw_input(">> Are you sure? (y/n) ")
					if answer == 'y':
						for i in range(0,times):
							bot.run()

				elif times == -1:
					answer = raw_input(">> This will endlessly run the bot. Are you sure? (y/n)")
					if answer == 'y':
						while 1:
							bot.run()

		elif input == 'add key':
			key = raw_input(">> Key: ")
			times = raw_input(">> Repeats: ")
			if int(times) > 1:
				interval = raw_input(">> Interval (in secs): ")
			else:
				interval = '0'
			bot.add_command('press', [key,times,interval])
			print ">> Key added"
		elif 'save ' in input:
			try: bot.save_commands(input.split()[1])
			except: print "Invalid filename"

		elif input == 'list commands':
			bot.print_commands()

		elif input:
			print ">>", input, "not recognised"