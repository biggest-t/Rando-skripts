import os
from pathlib import Path
import subprocess
import argparse

pth = Path()
history = []

parser = argparse.ArgumentParser()
parser.add_argument("-a", "--all", action="store_true")
args = parser.parse_args()
while True:
	os.system("clear")
	current_dir = pth.cwd() 
	new_dir = current_dir
	print(f"your current path: {current_dir.name}")
	files = []
	history.append(current_dir)

	for fl in history[-1].iterdir():

		if args.all == False:
			if fl.name[0] != '.':
				files.append(fl.name)
				print(f"{files.index(fl.name)}: {fl.name}")
		else:
			files.append(fl.name)
			print(f"{files.index(fl.name)}: {fl.name}")
	print("\n")

	i =  input("index:")
	if i == "q":
		break
	elif i == 'b':
		history.pop()
		if len(history) != 1:
			history.pop()

		new_dir = history[-1]
	elif i == "!":
		rundmc = input("function?: ")
		os.system(rundmc)
		input("done?")
	else:
		new_dir = f"{current_dir}/{files[int(i)]}"
	
	if Path(new_dir).is_dir() == False:
		subprocess.run(["vim", new_dir])
	else:
		os.chdir(new_dir)
