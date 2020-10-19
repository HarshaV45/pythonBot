

#importing random and datetime packages.
import random
from datetime import datetime

'''
Greeting function to greet the user.
'''
def greeting():
    responce = [
    "hello...! Hi Nice to see You",
    "welcome , nice to see you here"
    ]
    print(random.choice(responce))
  
def current_time_greet():
    current_time_greet=datetime.now()
    greeting="good morning"
    if current_time_greet.hour>12 and current_time_greet.hour<17:
        greeting="good afternoon"
    elif current_time_greet.hour>=17 and current_time_greet.hour<22:
        greeting="good evening"
    elif current_time_greet.hour>=22:
        greeting="Hi, its too late"
    return greeting

'''
this function gives us Welcome message 
'''

def welcome(name):
    message = [
        "welcome, Let's get started?",
        " Welcome.... whats your problem?"
    ]
    print(f"{current_time_greet()},! {name}, {random.choice(message)}")



def diseases():
  print("1.Fever")
  print("2.sore throat")
  print("3.cough")
  print("4.Sprains")
  print("5.Coronavirus")
  print("6.Astama")
  print("7.Indigestion")
  print("8.Exit")
  print("---------")
  try:
    return int(input("Enter your symptom : "))
  except Exception as e:
    print(str(e))


def Fever(): 
    print("Medicine : PARACETAMOL")
    print("     Weight 50kg or greater :")
    print("         1000 mg every 6 hours or 650 mg every 4 hours")
    print("     Weight less than 50kg or age between 2 to 12")
    print("         250 mg for every 6 hours")
    print("---NOTE--- See a doctor immidetly if your fever exceeds 102 and lasting more than 2 days")
def soreThroat():
    print("Medicine : IBUPROFEN and NAPROXEN")
    print("     Make sure you follow lables and direction for dosage ")
    print("--Natural Remedies--")
    print("     1.Gargle with luke warm salt water")
    print("     2.Honey mixed in tea or taken in its own is a common household remady for sore throat")
    print("     2.Drink plenty of water")
    print("----NOTE---- See a doctor if your sore throat last for more than 5 days")
def cough():
    print("Medicine : Cough syrups")
    print("--Natural Remedies--")
    print("     1.salt and water gargle")
    print("     2.Pineapple")
    print("     3.steam inhalation and drinking hot water")
    print("----NOTE----")
    print("See a doctor immediately if you : ")
    print("     Chocking and cant speak")
    print("     Having difficult breating")
    print('     Notice blood in your phlegm')
def sprains():
    print("Treatment varies")
    print("The best treatment for sprain is RICE(rest,ice,compression,elevation) method")
    print("if you have severe pain use pain killers like voloni sprays ")
    print("----Note---- see the doctor immediately if there is an infection")
def coronavirus():
     print("to date,there are no specific vaccines or medicines for COVid-19")
     print("Some of the medicines recomended by ICMR are : ")
     print("        Vitamin C")
     print("        Vitamin D")
     print("        ZINKOVITA")
     print("        DOLO 650 : to reduce fever")
     print("        AZITHROMYCIN : Antibiotic")
     print("        Steam Inhalation and hot water")
     print("        OXYMETER : to check oxygen levels in blood")
     print("----NOTE---- ")
     print("    go to hospital immidetly if you see: ")
     print("        Trouble breating")
     print("        Oxygen levels are below 93")
     print("        Heavy cough and high temperature last for more than 5 days")
def astama():
    print("Astama can usually be maanged with rescue inhalers to treat symptoms(salbutomal) ")
    print("FORMOTEROL and SALMETEROL as well as inhalent steroids")
def indigestion():
    print("Medicines : ANTACIDS")
    print("     Natural Remedies")
    print("         Peppermint tea")
    print("         Apple cider vinegar")
    print("         Ginger")
    print("         Lemon water")
    print("         Avoiding difficult-to-digest food") 
def final():
  greeting()
  name=input("Enter your name : ")
  welcome(name)
  choice=diseases()
  while choice!=8:
    if choice==1:
      Fever()
    elif choice==2:
      soreThroat()
    elif choice==3:
      cough()
    elif choice==4:
      sprains()
    elif choice==5:
      coronavirus()
    elif choice==6:
      astama()
    elif choice==7:
      Indigestion()
    else:
      print("Invalid")
    choice=diseases()
final()


