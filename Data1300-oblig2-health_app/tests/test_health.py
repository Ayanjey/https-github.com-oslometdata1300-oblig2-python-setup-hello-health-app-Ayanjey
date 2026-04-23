#lager test for/health.py 

import pytest 
from health_app.health import Health

#lager en funksjon for å teste verdiene fra klassen health.
def testHealth_creation():
    helse = Health(name = "Jon", height_m = 1.70, weight_kg = 60)
    #bruker assert funksjon for å se om verdiene er riktig.
    assert helse.name == "Jon"
    assert helse.height_m == 1.70
    assert helse.weight_kg == 60


#denne funksjonen tester bmi kalkulatoren
def testCALbmi():
    helse = Health (name = "Lise", height_m = 1.80, weight_kg = 75)
    assert helse.bmi == 25

#disse funskjonene tester "advice" 
def test_h_advice_normal():
     helse = Health (name = "Trish", height_m = 1.80, weight_kg = 75)
     assert "this shows that you are normal" in helse.get_health_advice()

def test_h_advice_obese():
     helse = Health(name= "Carl", height_m= 1.75, weight_kg= 110)
     assert "this shows that you are obese" in helse.get_health_advice()
     
def test_h_advice_underweight():
        helse = Health(name= "Dag", height_m= 1.70, weight_kg= 50)
        assert "this shows that you are underweight" in helse.get_health_advice()

       


def test_bmi_Cat():
      helse = Health (name = "La", height_m = 1.85, weight_kg = 75)
      assert #usikker på hvilke verdier jeg skal bruke.



def test_idealWeight():
     helse = Health (name = "Ole", height_m = 1.90, weight_kg = 75)
     assert #usikker på hvilke verdier jeg skal bruke.


