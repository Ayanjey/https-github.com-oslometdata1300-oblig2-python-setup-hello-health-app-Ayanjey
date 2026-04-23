#lager en fil i json format, bruker de eksisterende filene,(load_records og save_records)
import json
from .health import Health

#henter filen get_statistics som returnerer en ordbok med statistikk 
def get_statistics(D_file: str = "health_records.json") -> dict:
 theHealth_records = load_records(D_file)
 if not theHealth_records:
        return {
            "all_records": 0, 
            "average_bmi": 0.0,
            "typical_bmi_catergory": None,
            "category_distribution": {}
        
        }
   
 






