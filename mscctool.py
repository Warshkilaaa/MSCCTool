#импорт говна
import socket
from colorama import init, Fore
import requests
from bs4 import BeautifulSoup
import hashlib
import os
import sys
import time
import requests
import json
import re
import socket
import uuid
import subprocess
import shutil
import base64
import traceback


#цвета
init()
red = Fore.RED
lred = Fore.LIGHTRED_EX
black = Fore.BLACK
lblack = Fore.LIGHTBLACK_EX
white = Fore.WHITE
lwhite = Fore.LIGHTWHITE_EX
green = Fore.GREEN
lgreen = Fore.LIGHTGREEN_EX
cyan = Fore.CYAN
lcyan = Fore.LIGHTCYAN_EX
magenta = Fore.MAGENTA
lmagenta = Fore.LIGHTMAGENTA_EX
yellow = Fore.YELLOW
lyellow = Fore.LIGHTYELLOW_EX
blue = Fore.BLUE
lblue = Fore.LIGHTBLUE_EX
reset = Fore.RESET
def is_port_open(host, port):
    """
    determine whether `host` has the `port` open
    """
    # нужные строчки кода для работы portscanner
    s = socket.socket()
    try:
        s.connect((host, port))
    except:
        return False
    else:
        return True



#баннер
gay_porno = rf"""
                 $**$_$$***$$_$**$
                $*__*$*******$*__*$
                $*__***********__*$
                 $***************$
                 $*************$
                 $**$******$***$
                $**$$*****$$**$
                $****__$*$__****$
               $**__*__$$$__*__**$
               $**__*___$___*__**$
               $******_____******$
                $******$$$******$            MSCCTool by WARSHKILM v1
                 $*************$
                 $****_______****$
                $****_________****$
              $***$*_________*$***$
             $$***$*___$$_$$___*$***$$
           $****$**__$**$**$__**$****$
          $*$$**$*___$*****$___*$**$$*$
          $****$**____$***$____**$****$
           $***$**_____$*$_____**$***$
            $$$$**______$______**$$$$
              $***______________***$
                $***_________***$
                $****_ ______****$
                 $*****$*$*****$
                  $*****$*****$
               $$$$*****$*****$$$$
              $*********$*********$
              $********$_$********$


"""
print(gay_porno)
#начало кода
while True:





#переменая которая используется как строка ввода
    cmd = input("@")



#help
    def help():
        if cmd == "help":
            print("")
            print("")
            print("")
            print("На что способна программа?")
            print("help - показать этот список")
            print("portscanner - просканировать порты")
            print("server - получить настоящий айпи сервера(еще нету в программе)")
            print("player - получить информацию о игроке(еще нету в программе)")
            print("discord - дискорд сервера людей что участвовали в создание программы")
            print("")
            print("")
            print("")
    help()

    
#discord
    def discord():
        if cmd == "discord":
            print("")
            print("")
            print("")
            print("Спасибо kkcrash за идею - https://discord.gg/qDVanmKMvh")
            print("Спасибо mighty community за помощь в написании кода - https://discord.gg/7mRGsmDJk9")
            print("Дискорд разработчика программы - пока что нет =)")
            print("")
            print("")
            print("")
    discord()




 #не рабочий в v1.1 допилю 
    def server():
        if cmd == "server":
            print("")
            print("")
            print("")
            f = input("Введите айпи сервера: ")
            print("")
            print("")
            print("")

    server()




#portscanner
    def portscanner():
        if cmd == "portscanner":
            print("")
            print("")
            print("")
            host = input("Введите ip: ")
            print("начало сканирования....")
            for port in range(25000, 27000):
                if is_port_open(host, port):
                    print(f"{GREEN}[+] {host}:{port} Открыт попробуйте зайти по этому айпи      {RESET}")
            print("")
            print("")
            print("")
    portscanner()





    #не рабочий в v1.1 допилю 
    def player():
        if cmd == "player":
            try:
                nick = argument[1]
                player_command(nick)

                r = requests.get(f"{mojang_api}{nick}")
                r_json = r.json()
                player_uuid = r_json["id"]
                player_uuid_ = f"{player_uuid[0:8]}-{player_uuid[8:12]}-{player_uuid[12:16]}-{player_uuid[16:21]}-{player_uuid[21:32]}"

                offline_player_uuid = str(uuid.UUID(bytes=hashlib.md5(bytes(f"OfflinePlayer:{nick}", "utf-8")).digest()[:16], version=3))
                offline_player_uuid_ = offline_player_uuid.replace("-", "")

                print(f"\n{lblack}     [{lred}UU{white}ID{lblack}] {white}{player_uuid_}")
                print(f"{lblack}     [{lred}UU{white}ID{lblack}] {white}{player_uuid}\n")
                print(f"{lblack}     [{lred}UUID{white} Offline{lblack}] {white}{offline_player_uuid}")
                print(f"{lblack}     [{lred}UUID{white} Offline{lblack}] {white}{offline_player_uuid_}")

            except KeyboardInterrupt:
                pass

            except JSONDecodeError:
                offline_player_uuid = str(uuid.UUID(bytes=hashlib.md5(bytes(f"OfflinePlayer:{nick}", "utf-8")).digest()[:16], version=3))
                offline_player_uuid_ = offline_player_uuid.replace("-", "")
                print(f"\n{lblack}     [{lred}UUID{white} Offline{lblack}] {white}{offline_player_uuid}")
                print(f"{lblack}     [{lred}UUID{white} Offline{lblack}] {white}{offline_player_uuid_}")

            except requests.exceptions.ConnectionError:
                print(f"\n     {lblack}[{lred}ERR{white}OR{lblack}] {white}Connection error.")

            except Exception as e:
                if DEBUG:
                    print(f"\n     {lblack}[{lred}ERR{white}OR{lblack}] {white}DEBUG: \n {e} {traceback.format_exc()}")

                    offline_player_uuid = str(uuid.UUID(bytes=hashlib.md5(bytes(f"OfflinePlayer:{nick}", "utf-8")).digest()[:16], version=3))
                    offline_player_uuid_ = offline_player_uuid.replace("-", "")
                    print(f"\n{lblack}     [{lred}UUID{white} Offline{lblack}] {white}{offline_player_uuid}")
                    print(f"{lblack}     [{lred}UUID{white} Offline{lblack}] {white}{offline_player_uuid_}")