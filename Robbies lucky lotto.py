import random
def displayintro():
  print("Welcome to Robbie's Lucky Lotto. Please select three numbers from 0 to 9,or type in 10 for quick pick!")

displayintro()

user_num1 = int(input("First Number:"))
user_num2 = int(input("Second Number:"))
user_num3 = int(input("Third Number:"))

if user_num1 == 10:
    user_num1 = random.randint(0, 9)

if user_num2 == 10:
    user_num2 = random.randint(0, 9)

if user_num3 == 10:
    user_num3 = random.randint(0, 9)
print("Your Numbers:", user_num1, user_num2, user_num3)

random_num1 = random.randint(0, 9)
random_num2 = random.randint(0, 9)
random_num3 = random.randint(0, 9)

print("Winning Numbers:", random_num1, random_num2, random_num3)

if user_num1 == random_num1 and user_num2 == random_num2 and user_num3 == random_num3:
  print("You win $10,000")
elif user_num1 == random_num2 and user_num2 == random_num3 and user_num3 == random_num1:
  print("You win $1,000")
elif user_num2 == random_num1 and user_num3 == random_num2 and user_num1 == random_num3:
  print("You win $500")
elif user_num1 == random_num1 and user_num2 == random_num2:
  print("You win $50")
elif user_num2 == random_num2 and user_num3 == random_num3:
  print("You win $50")
elif user_num1 == random_num1 and user_num3 == random_num3:
  print("You win $50")
elif user_num1 == random_num2 and user_num2 == random_num1:
  print("You win $15")
elif user_num1 == random_num3 and user_num3 == random_num1:
  print("You win $15")
elif user_num2 == random_num3 and user_num3 == random_num2:
  print("You win $15")
elif user_num1 == random_num1:
  print("You win $5")
elif user_num2 == random_num2:
  print("You win $5")
elif user_num3 == random_num3:
  print("You win $5")
elif user_num1 == random_num2:
  print("You win $1")
elif user_num1 == random_num3:
  print("You win $1")
elif user_num2 == random_num1:
  print("You win $1")
elif user_num2 == random_num3:
  print("You win $1")
elif user_num3 == random_num1:
  print("You win $1")
elif user_num3 == random_num2:
  print("You win $1")
else:
  print("Better luck next time")

print("Do you want to play again? (yes or no)")
playAgain = input()

if playAgain == "no" or playAgain == "n":
  print("Thanks for playing! Come back soon!")

while playAgain == "yes" or playAgain == "y":
  displayintro()
  user_num1 = int(input("First Number:"))
  user_num2 = int(input("Second Number:"))
  user_num3 = int(input("Third Number:"))
  if user_num1 == 10:
    user_num1 = random.randint(0, 9)

  if user_num2 == 10:
    user_num2 = random.randint(0, 9)

  if user_num3 == 10:
    user_num3 = random.randint(0, 9)
  print("Your Numbers:", user_num1, user_num2, user_num3)

  random_num1 = random.randint(0, 9)
  random_num2 = random.randint(0, 9)
  random_num3 = random.randint(0, 9)

  print("Winning Numbers:", random_num1,        random_num2, random_num3)

  if user_num1 == random_num1 and user_num2 == random_num2 and user_num3 == random_num3:
    print("You win $10,000")
  elif user_num1 == random_num2 and user_num2 == random_num3 and user_num3 == random_num1:
    print("You win $1,000")
  elif user_num2 == random_num1 and user_num3 == random_num2 and user_num1 == random_num3:
    print("You win $500")
  elif user_num1 == random_num1 and user_num2 == random_num2:
    print("You win $50")
  elif user_num2 == random_num2 and user_num3 == random_num3:
    print("You win $50")
  elif user_num1 == random_num1 and user_num3 == random_num3:
    print("You win $50")
  elif user_num1 == random_num2 and user_num2 == random_num1:
    print("You win $15")
  elif user_num1 == random_num3 and user_num3 == random_num1:
    print("You win $15")
  elif user_num2 == random_num3 and user_num3 == random_num2:
    print("You win $15")
  elif user_num1 == random_num1:
    print("You win $5")
  elif user_num2 == random_num2:
    print("You win $5")
  elif user_num3 == random_num3:
    print("You win $5")
  elif user_num1 == random_num2:
    print("You win $1")
  elif user_num1 == random_num3:
    print("You win $1")
  elif user_num2 == random_num1:
    print("You win $1")
  elif user_num2 == random_num3:
    print("You win $1")
  elif user_num3 == random_num1:
    print("You win $1")
  elif user_num3 == random_num2:
    print("You win $1")
  else:
    print("Better luck next time")

  print("Do you want to play again? (yes or no)")
  playAgain = input()
  
  if playAgain == "no" or playAgain == "n":
   print("Thanks for playing! Come back soon!")
