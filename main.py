import sys

print("")
print(" _____             _          _____      ")                       
print("|  __ \           | |        |  __ \ ")                            
print("| |  | |_   _  ___| | ___   _| |__) |   _ _ __  _ __   ___ _ __ ")
print("| |  | | | | |/ __| |/ / | | |  _  / | | | '_ \| '_ \ / _ \ '__|")
print("| |__| | |_| | (__|   <| |_| | | \ \ |_| | | | | | | |  __/ |   ")
print("|_____/ \__,_|\___|_|\_\\\__, |_|  \_\__,_|_| |_|_| |_|\___|_|   ")
print("                         __/ |                 ")                 
print("                        |___/                   ")               
print("                     By: ibijon4")
path = sys.argv[1]
f = open(path,"r",encoding='utf-8')
payload = open("payload.py", "w")
payload.write("import pyautogui\n")
payload.write("import time\n")
duckyScript = f.readlines()
duckyScript = [x.strip() for x in duckyScript] 

defaultDelay = 0
if duckyScript[0][:7] == "DEFAULT":
	defaultDelay = int(duckyScript[0][:13]) / 1000
prev = ""	


ducky = ["WINDOWS", "GUI", "APP", "MENU", "SHIFT", "ALT", "CONTROL", "CTRL", "DOWNARROW", "DOWN",
"LEFTARROW", "LEFT", "RIGHTARROW", "RIGHT", "UPARROW", "UP", "BREAK", "PAUSE", "CAPSLOCK", "DELETE", "END",
"ESC", "ESCAPE", "HOME", "INSERT", "NUMLOCK", "PAGEUP", "PAGEDOWN", "PRINTSCREEN", "SCROLLLOCK", "SPACE", 
"TAB", "ENTER", " a", " b", " c", " d", " e", " f", " g", " h", " i", " j", " k", " l", " m", " n", " o", " p", " q", " r", " s", " t",
" u", " v", " w", " x", " y", " z", " A", " B", " C", " D", " E", " F", " G", " H", " I", " J", " K", " L", " M", " N", " O", " P",
" Q", " R", " S", " T", " U", " V", " W", " X", " Y", " Z"]

pycommands = ["win", "win", "optionleft", "optionleft", "shift", "alt", "ctrl", "ctrl", "down", "down",
"left", "left", "right", "right", "up", "up", "pause", "pause", "capslock", "delete", "end",
"esc", "escape", "home", "insert", "numlock", "pageup", "pagedown", "printscreen", "scrolllock", "space",
"tab", "enter", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
"u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
"q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

for line in duckyScript:
	if line[0:3] == "REM" :
		prev = line.replace("REM","#")
	elif line[0:5] == "DELAY" :
		prev = "time.sleep(" + str(float(line[6:]) / 1000) + ")"
	elif line[0:6] == "STRING" :
		prev = "pyautogui.typewrite(\"" + line[7:] + "\", interval=0.01)"
	elif line[0:6] == "REPEAT" :
		for i in range(int(line[7:]) - 1):
			payload.write(prev)
			payload.write("\n")
	else:
		prev = "pyautogui.hotkey("
		for j in range(len(pycommands)):
			if line.find(ducky[j]) != -1:
				prev = prev + "\'" + pycommands[j] + "\'," 
		prev = prev[:-1] + ")"
	if defaultDelay != 0:
		prev = "time.sleep(" + defaultDelay + ")"
	payload.write(prev)
	payload.write("\n")
payload.close()	
print("Task Finished")
exec(open('payload.py').read())