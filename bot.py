import pyHook
import pythoncom
from pymouse import PyMouse
from pymouse import PyMouseEvent
from pykeyboard import PyKeyboard

class Bot(object):
	def __init__(self):
		self._mouseObj = PyMouse()
		self._keyboardObj = PyKeyboard()
		self._commands = []
		self._pretty_commands = []
		self._LUT = {"Enter":self._keyboardObj.return_key,
				 "Tab":self._keyboardObj.tab_key,
				 "Backspace":self._keyboardObj.backspace_key,
				 "Shift":self._keyboardObj.shift_key,
				 "LShift":self._keyboardObj.shift_l_key,
				 "RShift":self._keyboardObj.shift_r_key,
				 "Control":self._keyboardObj.control_key,
				 "LControl":self._keyboardObj.control_l_key,
				 "RControl":self._keyboardObj.control_r_key,
				 "Alt":self._keyboardObj.alt_key,
				 "NumLock":self._keyboardObj.num_lock_key,
				 "ScrollLock":self._keyboardObj.scroll_lock_key,
				 "Space":self._keyboardObj.space_key,
				 "Escape":self._keyboardObj.escape_key,
				 "Page-Up":self._keyboardObj.page_up_key,
				 "Page-Down":self._keyboardObj.page_down_key,
				 "Down":self._keyboardObj.down_key,
				 "Left":self._keyboardObj.left_key,
				 "Right":self._keyboardObj.right_key,
				 "PrintScreen":self._keyboardObj.print_screen_key,
				 "Insert":self._keyboardObj.insert_key,
				 "Delete":self._keyboardObj.delete_key,
				 "Windows":self._keyboardObj.windows_l_key,
				 "LWindows":self._keyboardObj.windows_l_key,
				 "RWindows":self._keyboardObj.windows_r_key,
				 "F1":self._keyboardObj.function_keys[1],
				 "F2":self._keyboardObj.function_keys[2],
				 "F3":self._keyboardObj.function_keys[3],
				 "F4":self._keyboardObj.function_keys[4],
				 "F5":self._keyboardObj.function_keys[5],
				 "F6":self._keyboardObj.function_keys[6],
				 "F7":self._keyboardObj.function_keys[7],
				 "F8":self._keyboardObj.function_keys[8],
				 "F9":self._keyboardObj.function_keys[9],
				 "F10":self._keyboardObj.function_keys[10],
				 "F11":self._keyboardObj.function_keys[11],
				 "F12":self._keyboardObj.function_keys[12],
				 "Play":self._keyboardObj.play_key,
				 "VolMute":self._keyboardObj.volume_mute_key,
				 "VolUp":self._keyboardObj.volume_up_key,
				 "VolDown":self._keyboardObj.volume_down_key,
				 "MediaPlay":self._keyboardObj.media_play_pause_key,
				 "MediaPause":self._keyboardObj.media_play_pause_key,
				 "MediaNext":self._keyboardObj.media_next_track_key,
				 "MediaPrev":self._keyboardObj.media_prev_track_key}

	def click(self, x, y):
		self._mouseObj.click(x,y)

	def press(self, array):
		if array[0] in self._LUT.keys():
			for k,v in self._LUT.items():
				if array[0] == k:
					array[0] = v

		try: self._keyboardObj.tap_key(array[0], n=int(array[1]), interval=int(array[2]))
		except TypeError: print ">> Invalid key"
		except: print ">> Unexpected error"

	def type(self, array):
		for i in range(0,int(array[1])):
			for letter in array[0]:
				if list(array[0]).index(letter)+1 == len(array[0]):
					add_interval = int(array[2])
				else:
					add_interval = 0
				self._keyboardObj.tap_key(letter, n=1, interval=add_interval)		

	def get_click(self):
		self.Active = True
		self.position = None
        
		def onclick(event):
			if( self.Active ):
				self.position = event.Position
			return True        

		hm = pyHook.HookManager()
		hm.SubscribeMouseAllButtonsDown(onclick)
		hm.HookMouse()
		hm.HookKeyboard() #pyHook crashes if not included
		while self.position == None:
			pythoncom.PumpWaitingMessages()
		hm.UnhookMouse()
		hm.UnhookKeyboard()
		self.Active = False
		
		return self.position
		
	def get_key(self):
		self.Active = True
		self.key = None        
        
		def onKeyboardEvent(event):
			if( self.Active ):
				self.key = chr(event.Ascii)
			return True        

		hm = pyHook.HookManager()
		hm.KeyDown = onKeyboardEvent
		hm.HookMouse()  # hm.UnhookMouse throws an error otherwise
		hm.HookKeyboard()
		while self.key == None:
			pythoncom.PumpWaitingMessages()
		hm.UnhookMouse()
		hm.UnhookKeyboard()

		return self.key

	def run(self):
		for command in self._commands:
			for k,v in command.items():
				if k == 'click':
					self.click(v[0], v[1])

				if k == 'press':
					self.press(v)
					
				if k == 'type':
					self.type(v)

	def add_command(self, action, value):
		self._commands.append({action:value})
		if action == 'click':
			self._pretty_commands.append('Click at position {a}'.format(a=value))
		elif action == 'press':
			self._pretty_commands.append('Press {a} {b} times with {c}s delay'.format(a=value[0], b=value[1], c=value[2]))
		elif action == 'type':
			self._pretty_commands.append('Type {a} {b} times with {c}s delay'.format(a=value[0], b=value[1], c=value[2]))

	def print_commands(self):
		for command in self._pretty_commands:
			print ">>", command
				
	def save_commands(self, file):
		file = open('{f}.bot'.format(f=file), 'wb')
		for command in self._commands:
			for k,v in command.items():
				if type(v) is tuple:
					file.write('event:{k},value:{v}\n'.format(k=k, v=v))
				elif type(v) is list:
					file.write('event:{k},value:'.format(k=k))
					if len(v[0]) == 1:
						file.write('[key:"{v}",'.format(v=v[0]))
					else:
						file.write('[str:"{v}",'.format(v=v[0]))
					file.write(' repeat:{v},'.format(v=v[1]))
					file.write(' delay:{v}]\n'.format(v=v[2]))

		print ">> Save successful"

	def get_command(self,command):
		if '[' in command:
			new_command = []
			if 'str' in command:
				print command
				new_command.append(command.split('str:"')[1].split('"')[0])
			else:
				new_command.append(command.split("key:")[1].split('"')[0])
			new_command.append(command.split("repeat:")[1].split(',')[0])
			new_command.append(command.split("delay:")[1].split(']')[0])
			return new_command
		else:
			return (int(command.split(':(')[1].split(', ')[0]), int(command.split(':(')[1].split(', ')[1][0:-2]))

	def load_commands(self, file):
		if '.bot' in file:
			try: file = open(file).readlines()
			except: print "Invalid file"
		else:
			try: file = open('{f}.bot'.format(f=file)).readlines()
			except: print "Invalid file"
		for command in file:
			command_type = command.split(',')[0].split(':')[1]
			value = self.get_command(command)
			self._commands.append({command_type:value})
			
		print ">> Load successful"

	def commands_empty(self):
		return False if self._pretty_commands else True
		
	def is_valid_key(self, string):
		if len(string) > 1 and string not in self._LUT:
			return False
		else:
			return True