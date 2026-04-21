#dette er selve application koden
from .health import Health, load_records, save_records, get_statistics

#funksjon add health recoords
def add_healthRecords (): #spør om bruker input 
user_name = input("Enter your name here: ")
user_height = input("Enter your height here: ")
user_weight = input("Enter your weight here: ")

#bruker en if løkke for å validere bruker input:
if not user_name or not user_height or not user_weight:
    print("not correct, try again!: ")

def view_ALL_records():
    h_records = load_records()
    for data in h_records: #bruker en for-løkke til å 
        print () #jeg vet det er en måte jeg skriv skrive det ut på, men er usikker på hvordan jeg skal skrive print()



def view__statistics():
    The_stats = get_statistics()
    print ("here are the statistics: ", The_stats)




def Save_Quit():
