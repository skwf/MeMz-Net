import os
import colorama
from colorama import Fore
colorama.init()


# Main Menu
os.system("mode 45,20")
os.system("title MemzNet [Main Menu]")
print(Fore.LIGHTBLUE_EX + '''
░░░░░░░░░░░░░░░░░░░░░▄▀░░▌
░░░░░░░░░░░░░░░░░░░▄▀▐░░░▌
░░░░░░░░░░░░░░░░▄▀▀▒▐▒░░░▌
░░░░░▄▀▀▄░░░▄▄▀▀▒▒▒▒▌▒▒░░▌
░░░░▐▒░░░▀▄▀▒▒▒▒▒▒▒▒▒▒▒▒▒█
░░░░▌▒░░░░▒▀▄▒▒▒▒▒▒▒▒▒▒▒▒▒▀▄
░░░░▐▒░░░░░▒▒▒▒▒▒▒▒▒▌▒▐▒▒▒▒▒▀▄
░░░░▌▀▄░░▒▒▒▒▒▒▒▒▐▒▒▒▌▒▌▒▄▄▒▒▐
░░░▌▌▒▒▀▒▒▒▒▒▒▒▒▒▒▐▒▒▒▒▒█▄█▌▒▒▌
░▄▀▒▐▒▒▒▒▒▒▒▒▒▒▒▄▀█▌▒▒▒▒▒▀▀▒▒▐░░░▄
▀▒▒▒▒▌▒▒▒▒▒▒▒▄▒▐███▌▄▒▒▒▒▒▒▒▄▀▀▀▀
▒▒▒▒▒▐▒▒▒▒▒▄▀▒▒▒▀▀▀▒▒▒▒▄█▀░░▒▌▀▀▄▄
▒▒▒▒▒▒█▒▄▄▀▒▒▒▒▒▒▒▒▒▒▒░░▐▒▀▄▀▄░░░░▀
▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▄▒▒▒▒▄▀▒▒▒▌░░▀▄
▒▒▒▒▒▒▒▒▀▄▒▒▒▒▒▒▒▒▀▀▀▀▒▒▒▄▀''')
print(Fore.LIGHTWHITE_EX + '''
█████████████████████████████
█▄─▀█▀─▄█▄─▄▄─█▄─▀█▀─▄█░▄▄░▄█
██─█▄█─███─▄█▀██─█▄█─███▀▄█▀█
▀▄▄▄▀▄▄▄▀▄▄▄▄▄▀▄▄▄▀▄▄▄▀▄▄▄▄▄▀''')
print('')
UUID = input('UUID: ')


if UUID=='test':
    os.system("cls")
    os.system("mode 38,15")
    os.system("title MemzNet [Attack Selection]")
    print(Fore.LIGHTBLUE_EX + '''
    █████████████████████████████
    █▄─▀█▀─▄█▄─▄▄─█▄─▀█▀─▄█░▄▄░▄█
    ██─█▄█─███─▄█▀██─█▄█─███▀▄█▀█
    ▀▄▄▄▀▄▄▄▀▄▄▄▄▄▀▄▄▄▀▄▄▄▀▄▄▄▄▄▀''')
    print(Fore.LIGHTWHITE_EX + '''
    -----------------------------
          Types of Attacks
    -----------------------------''')
    print(Fore.LIGHTBLUE_EX + '''
                DNS
    ''' + Fore.WHITE)
    VictimIP = input('IP Address: ')
    AttackMethod = input('Attack Method: ')
else:
    exit(1)

input('')