#lager en fil i json format, bruker de eksisterende filene,(load_records og save_records)
import json
from .health import Health

#henter filen get_statistics
def get_statistics(filename: str = "health_records.json") -> dict:
 theHealth_records = load_records(filename)

 
#lager en liste som lagrer health objektene, som lagrer navn, vekt, høyde, bmi kalkulator
