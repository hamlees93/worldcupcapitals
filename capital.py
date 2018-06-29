country = (
  "Argentina",
  "Australia", 
  "Belgium",
  "Brasil",
  "Colomiba",
  "Costa Rica",
  "Croatia",
  "Denmark",
  "Egypt",
  "England",
  "France",
  "Germany",
  "Iceland",
  "Iran",
  "Japan",
  "Korea",
  "Mexico",
  "Morocco",
  "Nigeria",
  "Panama",
  "Peru",
  "Poland",
  "Portugal",
  "Russia",
  "Saudi Arabia",
  "Senegal",
  "Serbia",
  "Spain",
  "Sweden",
  "Switzerland",
  "Tunisia",
  "Uruguay"
)

capital = (
  ["Buenos Aires","Buenos airies"], 
  ["Canberra","canbera"],  
  ["Brussels","brussles"],
  ["Rio De Janerio","rio de janeiro"],
  ["Bogota","bogoto"],
  ["San Jose","sanjose"],
  ["Zagreb","zagrab"],
  ["Copenhagen","copenhagon"],
  ["Cairo","cario"],
  ["London","londen"],
  ["Paris","parie"],
  ["Berlin","berln"],
  ["Reykjavik","reykjavic"],
  ["Tehran","Tehren"],
  ["Tokyo","Tokoy"],
  ["Seoul","Soeul"],
  ["Mexico City","mexicocity"],
  ["Rabat","rabet"],
  ["Abuja","abjua"],
  ["Panama City","panamacity"],
  ["Lima","lema"],
  ["Warsaw","warsew"],
  ["Lisbon","lisben"],
  ["Moscow","moscuw"],
  ["Riyadh","riydah"],
  ["Dakar","dhakar"],
  ["Belgrade","belgrave"],
  ["Madrid","madride"],
  ["Stockholm","stockolm"],
  ["Bern","Berne"],
  ["Tunis","Tunisi"],
  ["Montevideo","montvideo"]
)

country_length = len(country)
incorrect_answers = []
correct_answers = []
count = 0
"""
for i in range(country_length):
  guess = str(input(f"capital of {country[i]}: "))
  if guess == capital[i][0].lower() or guess == capital[i][1].lower():
    correct_answers.append(capital[i][0])
    count += 1
  else:
    incorrect_answers.append(capital[i])

print(f"A reminder that the countries were: {country}")

if count = 0:
  print("You got ZERO! That was poor. Try again!")
elif count < 5:
  print(f"Unlucky, you only got {count} capitals. The correct answers you managed were: {correct_answers} and the answers you missed were: {incorrect_answers}")
elif count < 20:
  print(f"Well done, you got {count} capitals. The correct answers you managed were: {correct_answers} and the answers you missed were: {incorrect_answers}")
elif count < 32:
  print(f"Congratulations! You managed {count} correct capitals! The correct answers you managed were: {correct_answers} and the answers you missed were: {incorrect_answers}")
else:
  print("Congratulations!! You got a perfect score of 32. You are either a genuis, cheated or Hamish!")
  """


