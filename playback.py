#!/usr/bin/env python3
import keyboard
import ast
import time, sys

filename=sys.argv[1]

# stop after this many commits
stopearly=9999



def vimcmd(x):
	keyboard.write(x)
	keyboard.press_and_release('enter')

def window(lr):
	keyboard.press_and_release('ctrl+w, '+lr)

time.sleep(3)

vimcmd("vim")
time.sleep(0.3)

# probably should have grabbed this from the repo 
vimcmd(":set syntax=html")
vimcmd(":set timeoutlen=1000 ttimeoutlen=0") #not sure if this helps

lines_added=0
lines_removed=0
current_line=0
msgwindow=0

def navigate(to):
	global current_line

	jump=abs(current_line-to)

	vimcmd(":"+str(to))
	current_line=to
	if jump>3:
		keyboard.write('zz') # centre scroll
	if jump>15:
		vimcmd(':syntax sync fromstart')
		vimcmd(':')

	time.sleep(min(0.3,jump*0.005))


for line in open(filename):
	try:
		(d,i,t)= ast.literal_eval(line)
	except:
		try:
			(name,msg) = ast.literal_eval(line)
		except:
			continue;
		if (msgwindow==0):
			vimcmd(':set splitright')
			vimcmd(":vnew")
			keyboard.write('40')
			keyboard.press_and_release('ctrl+w')
			keyboard.write('|')
			vimcmd(':set linebreak')
			vimcmd(":set syntax=xml")
			vimcmd(':file commit_messages')
			msgwindow=1
		else:
			window('right')
		keyboard.write('i<'+name+'>: '+msg)
		keyboard.press_and_release('esc')
		window('left')

		stopearly=stopearly-1
		if stopearly<=0: exit()

		lines_added=0
		lines_removed=0
		continue;

	if keyboard.is_pressed('esc'):
		exit()

	time.sleep(0.01)
	if d==None: #insertion
		navigate(i)
		keyboard.write("O"+t, delay=0.001 )
		keyboard.press_and_release('esc')
		lines_added=1+lines_added
	elif i==None:
		navigate(d+lines_added-lines_removed)

		keyboard.write("dd")
		lines_removed=1+lines_removed


