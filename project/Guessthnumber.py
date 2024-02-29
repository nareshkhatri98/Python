import random

Target = random.randint(1,10)


while True:
   userChoice = int(input("Guess the Number or Quit(Q): "))
   if(userChoice =='Quite'):
      break
   if(userChoice == Target):
      print("Success : Correct Guess!!!")
      break

   if(userChoice<=Target):
      print("Guess number is smaller than the target")

   if(userChoice>=Target):
      print("Guess numbe is grather than target")
         


print("GAME OVER -----------")

