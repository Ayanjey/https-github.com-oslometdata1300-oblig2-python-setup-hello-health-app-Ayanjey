import pytest
from health_app.data import get_statistics
from health_app.data import save_records


#lager funksjon som tester statistikken og lagrer det i en liste
def test_get_statistics():
    Data_test = []#lager en liste som lagrer objektene i en liste
    Data_test.append({"name": "Ole", "height_m": 1.85, "weight_kg": 100, "bmi": 30.2, "bmi_category": "Obese", "ideal_weight": 75})
    Data_test.append({"name": "Kari", "height_m": 1.60, "weight_kg": 50, "bmi": 19, "bmi_category": "Normal", "ideal_weight": 55})
#lagrer all daten i en fil som en json fil.
    save_records(Data_test) 

