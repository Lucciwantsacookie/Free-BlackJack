import json

import daten_manager


import questionary
WHITE = "\033[37m"
RESET = "\033[0m"



with open("daten_manager.json") as f:
    daten = json.load(f)


def Start():
    blackjack = r"""
    ██████╗ ██╗      █████╗  ██████╗██╗  ██╗     ██╗ █████╗  ██████╗██╗  ██╗
    ██╔══██╗██║     ██╔══██╗██╔════╝██║ ██╔╝     ██║██╔══██╗██╔════╝██║ ██╔╝
    ██████╔╝██║     ███████║██║     █████╔╝      ██║███████║██║     █████╔╝
    ██╔══██╗██║     ██╔══██║██║     ██╔═██╗ ██   ██║██╔══██║██║     ██╔═██╗
    ██████╔╝███████╗██║  ██║╚██████╗██║  ██╗╚█████╔╝██║  ██║╚██████╗██║  ██╗
    ╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝ ╚════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
    """

    print(WHITE + blackjack + RESET)


    desicion = questionary.select(
        "Was möchtest du tun?",
        choices=[
            "Spielen",
            "Spielbeenden",
            "Einstellungen"
            
        ]
    ).ask()

    if desicion == "Spielen":
        if daten_manager.Start_Logik_Daten()  == True: 
            Main_Game()
                 
    elif desicion == "Spielbeenden":
        exit()
    elif desicion == "Einstellungen":
        print("Settings")


def Main_Game():
    pass