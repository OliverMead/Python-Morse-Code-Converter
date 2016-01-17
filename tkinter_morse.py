#!/usr/bin/env python

# A simple implementation of Morse Code in python with Tkinter

from Tkinter import *
from curses.ascii import ispunct # to identify punctuation in converting to morse code

class Morse:
	'''A class to convert English text to morse code'''
	def __init__(self):
		self.CODE = {'A': '.-',     'B': '-...',   'C': '-.-.',
		        'D': '-..',    'E': '.',      'F': '..-.',
		        'G': '--.',    'H': '....',   'I': '..',
		        'J': '.---',   'K': '-.-',    'L': '.-..',
		        'M': '--',     'N': '-.',     'O': '---',
		        'P': '.--.',   'Q': '--.-',   'R': '.-.',
		        'S': '...',    'T': '-',      'U': '..-',
		        'V': '...-',   'W': '.--',    'X': '-..-',
		        'Y': '-.--',   'Z': '--..',
		        '0': '-----',  '1': '.----',  '2': '..---',
		        '3': '...--',  '4': '....-',  '5': '.....',
		        '6': '-....',  '7': '--...',  '8': '---..',
		        '9': '----.',  ' ': '/'
		        }
		self.CODE2 = dict(zip(self.CODE.values(), self.CODE.keys())) # create a dictionary that is the inverse of self.CODE

	def E_to_M(self, Entry): # convert to morse
		self.result = "" # initialize a string variable
		for char in Entry: # for every character in Entry
			if ispunct(char): # if it is punctuation:
				pass # do nothing (omit punctuation)
			else: # otherwise
				self.result += self.CODE[char.upper()] + " " # convert to morse, add a space and add to the end of self.result
		return self.result[:-1] # give back the result without the final space

	def M_to_E(self, Entry): # convert from morse
		self.result = "" # initialize a string variable
		Entry = Entry.split(" ") # create a list of all of the morse characters
		for morse_char in Entry: # for every morse character
			self.result += self.CODE2[morse_char.upper()] # convert from morse and add to the end of self.result
		return self.result # give back the result

class App: # the tkinter GUI
	def __init__(self, master):
		self.tkmorse = Morse() # create an instance of Morse named tkmorse
		frame = Frame(master) # create a frame in window master
		frame.pack(padx = 20, pady = 20) # pack it into frame with padding
		Label(frame, text = "Morse Code Machine").grid(row = 0, columnspan = 3) # create a label as the title of the program
		Label(frame, text = "English in/out:").grid(row = 1, column = 0) # create a label to explain the first entry box
		self.eng_inout = StringVar() # initialize the variable for English I/O
		Entry(frame, textvariable = self.eng_inout).grid(row = 1, column = 1) # create an entry box using self.eng_inout and grid it in the centre
		Label(frame, text = "Morse in/out:").grid(row = 2, column = 0) # create a label to explain the second entry box
		self.mo_outin = StringVar() # initialize the variable for morse I/O
		Entry(frame, textvariable = self.mo_outin).grid(row = 2, column = 1)# create an entry box using self.mo_outin and grid it below the other
		Button(frame, text = "[English-Morse]", command = self.convert_EM).grid(row = 1, column = 2) # button to convert to morse
		Button(frame, text= "[Morse-English]", command = self.convert_ME).grid(row = 2, column = 2) # button to convert from morse

	def convert_EM(self): # convert English to Morse
		e = self.eng_inout.get() # get the contents of the relevant entry box
		self.mo_outin.set(self.tkmorse.E_to_M(e)) # convert to morse using E_to_M()

	def convert_ME(self): # convert Morse to English
		m = self.mo_outin.get() # get the contents of the relevant entry box
		self.eng_inout.set(self.tkmorse.M_to_E(m)) # convert to morse using M_to_E()

def main(): # to be run if not imported as a module
	win = Tk() # create a Tkinter window
	win.wm_title("Morse Code Converter") # set the title of the window
	app = App(win) # create an instance of App named app
	win.mainloop() # run the application ()

if __name__ == "__main__": main() # if the program is the main program running (e.g. not imported as a module), run main()
