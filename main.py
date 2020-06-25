
state_capital = {
  "Abia":"Umuahia",
  "Adamawa":"Yola",
  "Akwa Ibom":"Uyo",
  "Anambra":"Awka",
  "Bauchi":"Bauchi",
  "Bayelsa":"Yenagoa",
  "Cross Rivers":"Calabar","Delta":"Asaba",
  "Benue":"Makurdi",
  "Enugu":"Enugu",
  "Borno":"Maiduguri",
  "Ebonyi":"Abakiliki",
  "Edo":"Benin City",
  "Ekiti":"Ado Ekiti",
  "Gombe":"Gombe",
  "Jigawa":"Dutse",
  "Katsina":"Katsina",
  "Kaduna":"Kaduna",
  "Kano":"Kano",
  "Kebbi":"Birnin Kebbi",
  "Kogi":"Lokoji",
  "Kwara":"Ilorin",
  "Lagos":"Ikeja",
  "Imo":"Owerri",
  "Nasarawa":"Lafia",
  "Niger":"Minna",
  "Ogun":"Abeokuta",
  "Oyo":"Ibadan",
  "Osun":"Osogbo",
  "Ondo":"Akure",
  "Plateau":"Jos",
  "Rivers":"Portharcourt",
  "Taraba":"Jalingo",
  "Sokoto":"Sokoto",
  "Yobe":"Damaturu",
  "Zamfara":"Gusau"}
import random
#for key, value in state_capital.items():
state=list(state_capital.keys())
for i in [1,2,3,4,5]:
  ran_state= random.choice(state)
  capital=state_capital[ran_state]
  user_input=input("The capital of " ""+ ""+ran_state+"" + ""+""+"is:" )   
  if user_input==capital:
    print("You answered right")
  else:
    print("wrong answer, the correct answer is"+"" + "" + state_capital[ran_state])
print("all done")