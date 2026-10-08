import time, json, os

INTERVALLE = 30
CONFIG = os.environ.get("SONDE_CONFIG", "acces_sonde.env")  # fichier local, jamais publié

def mesurer():
    return {"charge": os.getloadavg()[0], "temperature": 41.5, "liaisons": "ok"}

while True:
    print(json.dumps(mesurer()))
    time.sleep(INTERVALLE)
