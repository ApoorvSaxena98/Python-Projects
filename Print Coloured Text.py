from colorama import Fore, Back, Style

# "FORE" k/w is used to change the colors of the letters & "BACK" is used to change the BACKGROUND Color.
print(Fore.BLUE + Back.LIGHTYELLOW_EX + "Namaste! My Name Is Apoorv Saxena " + Fore.YELLOW+ Back.BLUE + "A Btech Graduate In CSE & A Job-Seeker")
print(Fore.RED + Back.GREEN+ "Namaste! My Name Is Apoorv Saxena")

print(Style.DIM + Fore.RED + Back.BLACK + 'some red text')
print(Fore.LIGHTWHITE_EX + Back.LIGHTRED_EX + 'and with a green background')
print(Style.DIM + 'and in dim text')  # "Style.DIM" is used to dim the appearance of words / "Style.BRIGHT" is for making the text dark / "Style.NORMAL" is for normal text 
#print(Style.RESET_ALL)
print("Back to normal now...")
