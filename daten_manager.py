import json


n = ("json try")
cards = list(range(1,12))
used_cards = []


daten = {
    "n": n,
       "cards": cards,
               "used_cards": used_cards
    }


with open("daten_manager.json", "w") as f:
    json.dump(daten, f)
    