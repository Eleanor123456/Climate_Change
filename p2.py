from os import system

points = 10
dollars = 100
def start_function():
  print("Welcome to the game!\n\nWould you like to play part 1 or part 2?")
  answer=input("Type PART 1 for part 1")
  if answer=="PART 1":
    system("clear")
    print("")


def end_function():
  print("\n\nWould you like to play a different part?")
  answer=input("Type PART 1 for part 1")
  if answer=="PART 1":
    system("clear")
    print("")
  answer=input("Type PART 2 for part 2")
  if answer=="PART 2":
    system("clear")
    print("Would you like to order food in bulk, which is more than you need, but cheaper, (option A) or go to the farmer's market to buy fresh produce (option B)")
    answer = input("\nType your answer here ")
    if answer == "A":
      system("clear")
      print("you lost 10pts and gained $10")
      
    elif answer == "B":
      system("clear")
      print("you gain 10pts")
    answer2 = input("type 1 to continue")
    if answer2 == "1":
      system("clear")
      print("You find a tomato")
    
