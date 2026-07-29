import questionary
WHITE = "\033[37m"
RESET = "\033[0m"


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
        print("Gameloop")
    elif desicion == "Spielbeenden":
        exit()
    elif desicion == "Einstellungen":
        print("Settings")


