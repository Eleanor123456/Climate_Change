from os import system
import turtle

from main import display_points

points = 10
dollars = 100

def start_function(tree_list, tree):
  print("Welcome to the game!\n\nWould you like to play part 1 or part 2?")
  answer=input("Type PART 1 for part 1")
  if answer=="PART 1":
    part_1function(tree_list, tree)
  if answer=="PART 2":
    part_2function()
    

def end_function():
  print("\n\nWould you like to play a different part?")
  answer=input("Type PART 1 for part 1")
  if answer=="PART 1":
    system("clear")
  answer=input("Type PART 2 for part 2")


def part_2function():
  global points
  global dollars
  print("Do you take time to plan a grocery list(option A) or go straight to the store (option B)")
  answer = input("\nType your answer here ")
  if answer == "A":
    system("clear")
    print("you gain 10pts and $10")
    points = points+10
    dollars = dollars+10
  elif answer == "B":
    system("clear")
    print("you lose $10")
    dollars = dollars-10
  display_points(points,dollars)
  answer2 = input("type 1 to continue")
  if answer2 == "1":
    system("clear")
    print("would you like to spend time to research appropriate serving size (A) or guess (B)")
    answer = input("\nType your answer here ")
    if answer == "A":
      system("clear")
      print("you gain 10pts and lose $10")
      points = points+10
      dollars = dollars-10
    elif answer == "B":
     system("clear")
     print("you lose 10pts")
     points = points-10
  display_points(points,dollars)
  answer2 = input("type 1 to continue")
  if answer2 == "1":
    system("clear")
    print("Would you like to order food in bulk, which is more than you need, but cheaper, (A) or go to the farmer's market to buy fresh produce (B)")
    answer = input("\nType your answer here ")
    if answer == "A":
      system("clear")
      print("you lost 10pts and gained $10")
      points = points-10
      dollars=dollars+10
    elif answer == "B":
     system("clear")
     print("you gain 10pts")
     points = points+10
  display_points(points,dollars)
  answer2 = input("type 1 to continue")
  if answer2 == "1":
    system("clear")
    print("At the store you find tomatoes that are misshapen and cheaper than the other tomatoes. Do you buy them (A) or not (B)")
    if answer == "A":
      system("clear")
      print("you gain 10pts and $10")
      points = points+10
      dollars = dollars+10
    elif answer == "B":
      system("clear")
      print("you lost 10pts and $10")
      points = points-10
      dollars = dollars-10
  display_points(points,dollars)
  answer2 = input("type 1 to continue")
  if answer2 == "1":
    system("clear")
    print("you cut up some veggies do you chose to leave them on the counter(A) or put them in the fridge(B)")
    if answer == "A":
      system("clear")
      print("you lose 10pts")
      points = points-10
    elif answer == "B":
      system("clear")
      print("you gain 10pts")
      points = points+10
  display_points(points,dollars)
  if answer2 == "1":
    system("clear")
    print("It is almost time to close the restaurant and you have lots of food left do you want to give it away for free(A) or not(B)")
    if answer == "A":
      system("clear")
      print("you gain 10pts and lose $10")
      points = points+10
      dollars = dollars-10
    elif answer == "B":
      system("clear")
      print("you lose 10pts")
      points = points-10
  display_points(points,dollars)
  answer2 = input("type 1 to continue")
  if answer2 == "1":
    system("clear")
    print("You still have food left over do you choose to throw it away (A) or freeze it (B)")
    if answer == "A":
      system("clear")
      print("you lost 10pts")
      points = points-10
    elif answer == "B":
      system("clear")
      print("you gain 10pts")
      points = points+10
    display_points(points,dollars)
    answer2 = input("type 1 to continue")
    if answer2 == "1":
      system("clear")

def plant_trees(tree_list, num_trees, tree):
  tree_list.append(turtle.Turtle())
  tree_list[num_trees].speed(900)
  tree_list[num_trees].shape(tree)
  tree_list[num_trees].penup()
  tree_list[num_trees].goto(num_trees * 60 - 180, -110)
  #tree_list[num_trees].shape(tree)

  num_trees = num_trees + 1
  print("trees planted: " + str(num_trees))
  return num_trees

def part_1function(tree_list, tree):
  num_trees = 0
  answer = input("Type START to start the game")
  if answer == "START":
    system("clear")
    print(
        "What is climate change NOT doing to affect the earth?\n\n"
        "A) Worsening water quality\nB) Worsening air quality\nC) Melting icebergs\n"
        "D) Make the world colder")
    answer = input("\nType your answer here ")
    if answer == "D":
      system("clear")
      print("You are correct! :D\n")
      num_trees = plant_trees(tree_list, num_trees, tree)
    elif answer in ["A", "B", "C"]:
      system("clear")
      print("You are incorrect :(\n")
      print("trees planted: " + str(num_trees))
      print(
          "\nThe correct answer is D. Climate change does not make the climate of"
          " the earth colder, it makes it warmer.")
    answer = input("\nType 1 to continue")
    if answer == "1":
      system("clear")
      print(
          "What year could climate change be irreversible by?\n\nA)2030\nB)2040"
          "\nC)2050\nD)2060")
      answer = input("\nType your answer here ")
      if answer == "A":
        system("clear")
        print("You are correct :D\n")
        num_trees = plant_trees(tree_list, num_trees, tree)
      elif answer in ["B", "C", "D"]:
        system("clear")
        print("You are incorrect :(\n")
        print("trees planted: " + str(num_trees))
        print(
            "\nThe correct answer is A. Climate change could be irreversible by"
            " 2030!! Isn't that insane?")
      answer = input("\nType 1 to continue")
      system("clear")
      if answer == "1":
        print(
            "How many tons of ice are we losing each year?\n\nA)2 billion\nB)1.2 trillion\n"
            "C)1 trillion\nD)7.6 billion")
        answer = input("\nType your answer here")
        if answer == "B":
          system("clear")
          print("You are correct :D\n")
          num_trees = plant_trees(tree_list, num_trees, tree)
        elif answer in ["A", "C", "D"]:
          system("clear")
          print("You are incorrect :(\n")
          print("trees planted: " + str(num_trees))
          print(
              "\nThe correct answer is B. Climate change is causing 1.2 trillion tons"
              " of ice to melt each year! That is crazy.")
        answer = input("\nType 1 to continue")
        if answer == "1":
          system("clear")
          print(
              "What was the first known animal to go extinct due to climate change?\n"
              "\nA)California condor\nB)Golden toad\nC)Baiji Dolphin\nD)Mountain gorilla"
          )
          answer = input("\nType your answer here")
          if answer == "B":
            system("clear")
            print("You are correct :D\n")
            num_trees = plant_trees(tree_list, num_trees, tree)
          elif answer in ["A", "C", "D"]:
            system("clear")
            print("You are incorrect :(\n")
            print("trees planted: " + str(num_trees))
            print(
                "\nThe correct answer is B. Climate change has gotten 1 known animal"
                " to go extinct so far. If we don't prevent it soon, it'll cause more "
                "beautiful animals to go extinct.")
          answer = input("\nType 1 to continue")
          if answer == "1":
            system("clear")
            print("INTERESTING FACT TIME!\n\nDid you know that sea level has"
                  " risen 4 inches since January 1993?")
            answer = input("\nType 1 to move on")
            if answer == "1":
              system("clear")
              print(
                  "What is NOT a renewable energy source?\n\nA)Water\nB)Light"
                  "\nC)Oil\nD)Wind")
              answer = input("\nType your answer here")
              if answer == "C":
                system("clear")
                print("You are correct! :D\n")
                num_trees = plant_trees(tree_list, num_trees, tree)
              elif answer in ["A", "B", "D"]:
                system("clear")
                print("You are incorrect :(\n")
                print("trees planted: " + str(num_trees))
                print(
                    "\nThe correct answer is C. Light, water, and wind are all"
                    " clean resources you can use instead of unclean ones like oil, fossil "
                    "fuels, and gas. You might want to consider switching to a clean energy"
                    " source. It is healthier and better in the long run!")
              answer = input("\nType 1 to continue")
              if answer == "1":
                system("clear")
                print(
                    "What absorbs most of the heat we produce?\n\nA)Oceans\nB)"
                    "Air\nC)Trees\nD)Crops")
                answer = input("\nType your answer here")
                if answer == "A":
                  system("clear")
                  print("You are correct! :D\n")
                  num_trees = plant_trees(tree_list, num_trees, tree)
                elif answer in ["B", "C", "D"]:
                  system("clear")
                  print("You are incorrect :(\n")
                  print("trees planted: " + str(num_trees))
                  print(
                      "\nThe correct answer is A. The ocean actually absorbs most of the"
                      " heat we produce! So if we want to save the ocean and the animals living"
                      " in the ocean, we should all work to stop climate change."
                  )
                answer = input("\nType 1 to continue")
                if answer == "1":
                  system("clear")
                  print(
                      "INTERESTING FACT TIME!\n\nDid you know that climate change"
                      " increases the spread of annoying bugs and causes fatal diseases like"
                      " malaria, Lyme disease, and dengue?")
                  answer = input("\nType 1 to move on")
                  if answer == "1":
                    system("clear")
                    print(
                        "What do green house gasses do?\n\nA)Release toxins that clog air particles"
                        "\nB)Slowly destroy grass\nC)Change temperatures in green houses\n"
                        "D)Trap heat and ruin the climate")
                  answer = input("\nType your answer here")
                  if answer == "D":
                    system("clear")
                    print("You are correct! :D\n")
                    num_trees = plant_trees(tree_list, num_trees, tree)
                  elif answer in ["A", "B", "C"]:
                    system("clear")
                    print("You are incorrect :(\n")
                    print("trees planted: " + str(num_trees))
                    print(
                        "\nThe correct answer is D. Green house gasses trap heat and build up"
                        ", affecting the climate little by little.")
                  answer = input("\nType 1 to continue")
                  if answer == "1":
                    system("clear")
                    print(
                        "What element makes up most of green house gasses?\n\n"
                        "A)Oxygen\nB)Nitrogen\nC)Carbon dioxide\nD)Helium")
                  answer = input("\nType your answer here")
                  if answer == "C":
                    system("clear")
                    print("You are correct! :D\n")
                    num_trees = plant_trees(tree_list, num_trees, tree)
                  elif answer in ["A", "B", "D"]:
                    system("clear")
                    print("You are incorrect :(\n")
                    print("trees planted: " + str(num_trees))
                    print(
                        "\nThe correct answer is C. Carbon dioxide makes up "
                        " almost 80% of green house gas emissions in the US (as of"
                        " 2020)")
                  answer = input("\nType 1 to continue")
                  if answer == "1":
                    system("clear")
                    print("THE END OF PART 1!!\nThank you for playing")
    
