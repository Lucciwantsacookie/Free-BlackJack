import random

import json


n = ("json try")
cards = list(range(1,12))
used_cards = []
player_cards = []
bot_cards = []


def Start_Logik_Daten():
    for i in range(2):
        player_cards.append(random.randint(1, 11))
        #bot_cards.append(random.randint(1, 11))                 
    for i in player_cards:
        used_cards.append(i)    
    #for i in bot_cards:
        #used_cards.append(i)  
    for i in used_cards:
        if i in cards:
            cards.remove(i)  
    print("Player Cards: ", player_cards)
    print("Bot Cards: ", bot_cards)
    print("Used Cards: ", used_cards)
    print("Cards: ", cards)
    return True



daten = {
    "n": n,
       "cards": cards,
               "used_cards": used_cards,
               "player_cards": player_cards,
               "bot_cards": bot_cards

    }


with open("daten_manager.json", "w") as f:
    json.dump(daten, f)
