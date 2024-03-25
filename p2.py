from os import system

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
    print("")
