class Health:
    #lager konstruktøren
    def __init__(self, name:(str), weight_kg:(float), height_m:(float)) -> None:
        

        #validerer alle input med if-setninger med valueError
        #ValueError: if name is empty, weight <= 0 or height <= 0
#bruker if setninger til å validere

        if not isinstance (name, str) or len(name.strip()) == 0:
            raise ValueError ("name has to be a non-empty str")
        if not isinstance (weight_kg (float)) <= 0:
            raise ValueError ("not correct weight")
        if not isinstance (height_m(float)) <= 0:
            raise ValueError ("not correct height")
        
        self.name = name.strip()
        self.weight_kg = float(weight_kg)
        self.height_m = float(height_m)

#Calculates BMI: weight_kg / height_m², rounded to 2 decimals
        self.bmi = (self.weight_kg/ (self.height_m ** 2), 2) 

     
#category for the weight
        
    def bmi_category (self) -> str:
        if self.bmi < 18.5:
            return "underweight"
        elif self.bmi < 24.5:
            return "Normal"
        elif self.bmi 29.9
            return "Overweight"
        else:
            return "Obese"
    
        

#Returns personalized advice based on BMI category. 
# Minimum 2–3 sentences per category. 
# Examples: "Maintain balanced diet", "Consider weight loss consultation".
    def get_health_advice(self) -> str:
        B_category = self.bmi_category()
        if B_category == "underweight":
            return "this category shows that you are underweight, and " \
            "you should start a health journy where weight gain is the main focus"
        elif B_category == "Normal":
            return "This category shows that you have a normal and balanced " \
            "weight. That means that you should keep doing the excersice that you´re currently doing" \
            "and continue your diet."    
        else:
            return "this means that you´re obese and that you should really consider changing your ways." \
            "by getting a balanced diet and a healthier lifestyle, so you could lose some weight."    
    
   

#Formula: 22 × height_m² — returns ideal weight rounded to 1 decimal place.
#bruker round() til å runde av 
    def get_ideal_weight(self) -> float:
        return round(22 * (self.height_m ** 2),1)
    
    #åpner en json fil som lagrer inneholde til filen i en ny variabel.
def load_records(filename ="health_records.json"):
with open (filename, "file") as healthFile:
    j
    


#åpner en json fil o
def load_records(filename ="health_records.json"):
    with open (filname ="this is the file") as healthFile:
        TOdata = json.load(healthFile)