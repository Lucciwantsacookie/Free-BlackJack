import daten_manager
import Interface

import questionary
import json

WHITE = "\033[37m"
RESET = "\033[0m"


    


with open("daten_manager.json") as f:
    daten = json.load(f)



def main() :
    Interface.Start()


if __name__ == "__main__":
    main()


