# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 22:33:47 2020

@author: Xine Ong
"""

user = input("Hello there! What's your name? ")
print(f"\nHi, {user.title()}! How well do you know the spells used in the \"Harry Potter\" series? Take this quiz to find out!\nJust input the letter of your answer for each question. Let's begin!")

title="\n\n[[ HARRY POTTER SPELLS QUIZ ]]\n"
print(title)

score = 0
qnumber = 1

### CHOICES FUNCTION

def printchoices():
  letters = ["a", "b", "c", "d"]
  letter = 0
  for choice in choices:
    print (f"\t{letters[letter]}. {choice}")
    letter += 1

### QUIZ FUNCTION

def runquiz ():
  global score
  global qnumber
  letters_dict = {"a":0, "b":1, "c":2, "d":3}
  print(f"{qnumber}. {question}")
  printchoices()
  user_answer = input("\nAnswer: ")
  if user_answer.lower() == correct_answer:
    print ("That's correct!\n")
    score += 1
  else:
    choiceindex = letters_dict[correct_answer]
    print (f"Sorry, that is incorrect. The correct answer is {correct_answer}. {choices[choiceindex]}.\n")
  qnumber += 1



###   QUESTION 1

question = "Every great hero has a signature move, so what's Harry Potter's signature duelling spell?"
choices = ["Alohomora", "Expelliarmus", "Muffliato", "Ascendio"]
correct_answer = "b"

runquiz()

###   QUESTION 2

question = "Which charm is responsible for uncontrollable leg movements?"
choices = ["Tarantallegra", "Macarena", "Accio", "Legilimens"]
correct_answer = "a"

runquiz ()

###   QUESTION 3

question = "Why should you cover your mouth when struck by the incantation 'Densaugeo'?"
choices = ["It causes the teeth to grow at an alarming rate", "It turns your tongue into a bullfrog", "It causes you to reveal embarrassing secrets", "It leads you to vomit uncontrollably"]
correct_answer = "a"

runquiz ()

###   QUESTION 4

question = "What spell would you most likely use to make something float in the air?"
choices = ["Colloportus", "Obliviate", "Wingardium Leviosa", "Petrificus Totalus"]
correct_answer = "c"

runquiz ()

###   QUESTION 5

question = "Which volatile spell could blast open a sealed door with a small explosion?"
choices = ["Blasto", "Alohomora", "Explosiano", "Bombarda"]
correct_answer = "d"

runquiz ()

###   QUESTION 6

question = "Which protective charm warns of intruders in an area by letting out a high-pitched shriek?"
choices = ["Alarmo", "Cheering Charm", "Caterwauling Charm", "Fidelius Charm"]
correct_answer = "c"

runquiz ()

###   QUESTION 7

question = "Following an evil use of dark magic, what spell do the Death Eaters use to send a 'Dark Mark' into the sky?"
choices = ["Morsmordre", "Impervius", "Finite Incantatem", "Protego"]
correct_answer = "a"

runquiz ()

###   QUESTION 8

question = "Which spell would you use to defeat a boggart?"
choices = ["Diffindo", "Locomotor Mortis", "Protego", "Riddikulus"]
correct_answer = "d"

runquiz ()

###   QUESTION 9

question = "Which incantation will amplify your voice?"
choices = ["Scourgify", "Sonorus", "Stupefy", "Aguamenti"]
correct_answer = "b"

runquiz ()

###   QUESTION 10

question = "Which secretive spell perfectly prevents eavesdropping by filling the victim's ears with an annoying buzzing sound?"
choices = ["Muffliato", "Silencio", "Incendio", "Episkey"]
correct_answer = "a"

runquiz ()

###   END OF QUIZ

rate = float(score / 10) * 100

if int(rate) >= 70:
  pass_fail = "Congrats, you passed!"
else:
  pass_fail = "Sorry, you failed."

print ("\n\nTOTAL SCORE: " + str(score) + " out of 10")
print(f"You got {int(rate)}%. {pass_fail}")

