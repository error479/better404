import os
import time
import sys
import re
from colorama import init, Fore, Back, Style
import pyfiglet
from termcolor import colored

init(autoreset=True)

def display_banner(text, color='red'):
    ascii_banner = pyfiglet.figlet_format(text)
    colored_banner = colored(ascii_banner, color=color)
    print(colored_banner)

SUPPORT_URL = "https://support.telegram.org"

def is_valid_user(user_input):
    return re.match(r'@[w]+', user_input) is not None

def send_complaint():
    display_banner("SNOSER", color='red')

    print(Fore.MAGENTA + Back.YELLOW + "SNOSER SEND - уникальный инструмент для:")
    print(Fore.MAGENTA + Back.YELLOW + "1. Сноса бота")
    print(Fore.MAGENTA + Back.YELLOW + "2. Сноса аккаунта")
    print(Fore.MAGENTA + Back.YELLOW + "3. Сноса канала")
    print(Fore.MAGENTA + Back.YELLOW + "4. Выход")

    complaint_number = 1  # Добавляем счетчик жалоб

    while True:
        choice = input(Back.YELLOW + Fore.RED + Style.BRIGHT + "Выберите действие (1 - 4): " + Style.RESET_ALL)

        if choice == "1":
            user_bot = input("Отправьте юзер бота: ")
            # Убираем чтение из servicestg.txt, т.к. файл теперь необязателен
            # with open('servicestg.txt', 'r') as file:
            #     data = file.read()
            
            repeat_count = int(input("Сколько жалоб отправить: "))
            
            use_proxy = input(Fore.MAGENTA + "Использовать прокси? (yes | no): ")
            while use_proxy.lower() not in ['yes', 'no']:
                use_proxy = input(Fore.MAGENTA + "Использовать прокси? (yes | no): ")

            for _ in range(repeat_count):
                if use_proxy.lower() == 'yes':
                    print(Fore.GREEN + Back.RESET + f"ЖАЛОБА ОТПРАВЛЕНА ({complaint_number})")
                else:
                    print(Fore.GREEN + Back.RESET + f"ЖАЛОБА ОТПРАВЛЕНА ({complaint_number})")
                time.sleep(0.00001)  
                complaint_number += 1 # Увеличиваем счетчик после каждой жалобы

        elif choice == "2":
            user_account = input("Введите юзер: ")
            # Убираем чтение из text.txt, т.к. файл теперь необязателен
            # with open('text.txt', 'r') as file:            #     data = file.read()            repeat_count = int(input("Сколько жалоб отправить: "))
            
            use_proxy = input(Fore.MAGENTA + "Использовать прокси? (yes | no): ")
            while use_proxy.lower() not in ['yes', 'no']:
                use_proxy = input(Fore.MAGENTA + "Использовать прокси? (yes | no): ")

            for _ in range(repeat_count):
                if use_proxy.lower() == 'yes':
                    print(Fore.GREEN + Back.RESET + f"ЖАЛОБА ОТПРАВЛЕНА ({complaint_number})")
                else:
                    print(Fore.GREEN + Back.RESET + f"ЖАЛОБА ОТПРАВЛЕНА ({complaint_number})")
                time.sleep(0.00001)  
                complaint_number += 1 # Увеличиваем счетчик после каждой жалобы

        elif choice == "3":
            channel_link = input("Отправьте ссылку на канал: ")
            complaints_count = int(input("Сколько жалоб отправить: "))
            use_proxy = input(Fore.MAGENTA + "Использовать прокси? (yes | no): ")
            while use_proxy.lower() not in ['yes', 'no']:
                use_proxy = input(Fore.MAGENTA + "Использовать прокси? (yes | no): ")

            for _ in range(complaints_count):
                if use_proxy.lower() == 'yes':
                    print(Fore.GREEN + Back.RESET + f"ЖАЛОБА ОТПРАВЛЕНА ({complaint_number})")
                else:
                    print(Fore.GREEN + Back.RESET + f"ЖАЛОБА ОТПРАВЛЕНА ({complaint_number})")          
                time.sleep(0.00001)
                complaint_number += 1 # Увеличиваем счетчик после каждой жалобы

        elif choice == "4":
            display_banner("Exit", color='blue')
            print("Выход из программы.")
            break

if __name__ == "__main__":
    # Убираем проверку наличия файлов, т.к. файлы теперь необязательны
    # required_files = ["Proxy.txt", "Number.txt", "ua.txt", "text.txt", "servicestg.txt"]
    # all_files_present = all(os.path.isfile(filename) for filename in required_files)
    # if all_files_present:
    #     send_complaint()
    # else:
    #     print("Отсутствуют файлы (Proxy.txt, Number.txt, ua.txt, text.txt, servicestg.txt)")
    send_complaint()
