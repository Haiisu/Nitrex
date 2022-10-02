import random
import os
import platform
import time
import sys
# -------------------------------------------- 
from os import system, name
from colorama import Fore, Back, Style, ansi, init
from sty import fg, bg, ef, rs

def clear():
    if name == 'nt':
        _ = system('cls')
  
    else:
        _ = system('clear')

def g(rolls):
	data = "qwertyuioplkjhgfdsazxcvbnm1234567890QWERTYUIOPLKJHGFDSAZXCVBNM"
	result = ""
	while rolls >= 1:
		c = random.choice(data)
		result = c + result
		rolls = rolls - 1
	return result

def y():	
	result = " "	
	for x in range(1200):	
		rdmnum = random.randrange(723,981, 52)	
		rdmnumstr = str(rdmnum)	
		c = rdmnumstr	
	return c	

def zone1():
	clear()
	print(f'''	
         {fg(203)} _  _  ___  _____  ___  ___ __  __{fg.rs}
         {fg(204)}| \| ||_ _||_   _|| _ \| __|\ \/ /{fg.rs}
         {fg(205)}| .  | | |   | |  |   /| _|  >  < {fg.rs}
         {fg(206)}|_|\_||___|  |_|  |_|_\|___|/_/\_\{fg.rs}
    {fg(207)}[*]--------------------------------------[*]{fg.rs}
      {fg(213)}(Your best Free Discord Nitro Generator){fg.rs}
	  ''')	

	time.sleep(0.8)
	packst = input(f'{fg(255)}[ > ]{fg.rs}{fg(147)} Number of threads (Recommended: 2-5 / Normal: 1) {fg(159)}>>> ')

	if packst == '1':
		for x in range(1200):
				time.sleep(0.08)
				print(f'{fg(124)} [> Invalid Code]{fg.rs} {fg(255)}https://discord.gift/{g(16)} {fg.rs}|{fg(129)} Response Time:{fg.rs} {fg(78)}[{y()} ms] {fg.rs}')
		rp()
	elif packst == '2':
		for x in range(1200):
				time.sleep(0.07)
				print(f'{fg(124)} [> Invalid Code]{fg.rs} {fg(255)}https://discord.gift/{g(16)} {fg.rs}|{fg(129)} Response Time:{fg.rs} {fg(78)}[{y()} ms] {fg.rs}')
		rp()
	elif packst == '3':
		for x in range(1200):
				time.sleep(0.06)
				print(f'{fg(124)} [> Invalid Code]{fg.rs} {fg(255)}https://discord.gift/{g(16)} {fg.rs}|{fg(129)} Response Time:{fg.rs} {fg(78)}[{y()} ms] {fg.rs}')
		rp()
	elif packst == '4':
		for x in range(1200):
				time.sleep(0.05)
				print(f'{fg(124)} [> Invalid Code]{fg.rs} {fg(255)}https://discord.gift/{g(16)} {fg.rs}|{fg(129)} Response Time:{fg.rs} {fg(78)}[{y()} ms] {fg.rs}')
		rp()
	elif packst == '5':
		for x in range(1200):
				time.sleep(0.04)
				print(f'{fg(124)} [> Invalid Code]{fg.rs} {fg(255)}https://discord.gift/{g(16)} {fg.rs}|{fg(129)} Response Time:{fg.rs} {fg(78)}[{y()} ms] {fg.rs}')
		rp()		
	else:
		clear()
		zone1()

time.sleep(1)

def rp():
	clear()
	yn = input(f"{Fore.RED + Back.BLACK }[ Error ] Sorry, we couldn't find any valid code. Do you want to try again? [Y/n]: {fg.rs}")
	if yn.lower == 'yes' or 'y':
		clear()
		zone1()
	else:
		exit()


if __name__ == "__main__":
    zone1()