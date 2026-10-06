import time, json, os

INTERVALLE = 30
CONFIG = "acces_sonde.env"

def mesurer():
    return {"charge": os.getloadavg()[0], "temperature": 41.5, "liaisons": "ok"}

while True:
    print(json.dumps(mesurer()))
    time.sleep(INTERVALLE)
