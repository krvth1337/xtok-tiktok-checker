import sys
import os
import msvcrt

def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def print_menu(options, selected_index):
    clear_console()
    print('\033[95m' + r" __  _______ ___  _  __   ____ _   _ _____ ____ _  _______ ____  " + '\033[0m')
    print('\033[95m' + r" \ \/ /_   _/ _ \| |/ /  / ___| | | | ____/ ___| |/ / ____|  _ \ " + '\033[0m')
    print('\033[95m' + r"  \  /  | || | | | ' /  | |   | |_| |  _|| |   | ' /|  _| | |_) |" + '\033[0m')
    print('\033[95m' + r"  /  \  | || |_| | . \  | |___|  _  | |__| |___| . \| |___|  _ < " + '\033[0m')
    print('\033[95m' + r" /_/\_\ |_| \___/|_|\_\  \____|_| |_|_____\____|_|\_\_____|_| \_|" + '\033[0m')
    print("")
    print("\033[95m" + "Wähle eine Methode aus")
    print("")
    separator = '\033[95m' + "x───────────────────────────────────────────────────────────────x" + '\033[0m'
    print(separator)
    print("")

    for i, option in enumerate(options):
        if i == selected_index:
            print('\033[92m' + f'[{option}]' + '\033[0m')
        else:
            print(f' {option} ')

def menu(options):
    selected_index = 0
    while True:
        print_menu(options, selected_index)

        key = ord(msvcrt.getch())
        if key == 72:
            selected_index = (selected_index - 1) % len(options)
        elif key == 80:
            selected_index = (selected_index + 1) % len(options)
        elif key == 13:
            return options[selected_index]

options = ['4l', '4c', '5l', '5c']
selected_option = menu(options)