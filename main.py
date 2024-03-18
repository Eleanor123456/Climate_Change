from os import system
import turtle
import time
import p2

p2.start_function()

screen = turtle.Screen()
screen.setup(400,400)
x=0
screen.bgpic("background1.gif")
time.sleep(2)
tree = ("best-tree.gif")
screen.addshape(tree)

screen.bgpic("background2.gif")
screen.update()


tree_list = []


tom = turtle.Turtle()
tom.shape('turtle')
tom.color('green')

tom.left(90)
tom.forward(70)
tom.penup()
tom.right(90)
tom.forward(70)
tom.pendown()
tom.right(90)
tom.forward(70)
tom.left(90)
tom.penup()
tom.right(180)
tom.forward(130)
tom.left(90)
tom.pendown()
tom.circle(100,180)
tom.penup
style=('arial', 30)
tom.write("Hi!",font=style)
tom._delay(4000)
tom.clear()

def plant_trees(num_trees):
  tree_list.append(turtle.Turtle())
  tree_list[num_trees].speed(900)
  tree_list[num_trees].shape(tree)
  tree_list[num_trees].penup()
  tree_list[num_trees].goto(num_trees * 60-180,-110)
  tree_list[num_trees].shape(tree)

  num_trees = num_trees + 1
  print("trees planted: "+ str(num_trees))
  return num_trees
  
def main():
  num_trees=0
  def start_function():
    print("Welcome to the game!\n\nWould you like to play part 1 or part 2?")
    answer=input("Type PART 1 for part 1")
    if answer=="PART 1":
      system("clear")
  p2.start_function()
  print("Welcome to the game!\n\nMake sure to type your answers in all caps!\n")
  answer=input("Type START to start the game")
  if answer=="START":
    system("clear")
    print("What is climate change NOT doing to affect the earth?\n\n"
    "A) Worsening water quality\nB) Worsening air quality\nC) Melting icebergs\n"
    "D) Make the world colder")
    answer=input("\nType your answer here ")
    if answer=="D":
      system("clear")
      print("You are correct! :D\n")
      num_trees = plant_trees(num_trees)
    elif answer in["A","B","C"]:
      system("clear")
      print("You are incorrect :(\n")
      print("trees planted: "+ str(num_trees))
      print("\nThe correct answer is D. Climate change does not make the climate of"
      " the earth colder, it makes it warmer.")
    answer=input("\nType 1 to continue")
    if answer=="1":
      system("clear")
      print("What year could climate change be irreversible by?\n\nA)2030\nB)2040"
      "\nC)2050\nD)2060")
      answer=input("\nType your answer here ")
      if answer=="A":
        system("clear")
        print("You are correct :D\n")
        num_trees = plant_trees(num_trees)
      elif answer in["B","C","D"]:
        system("clear")
        print("You are incorrect :(\n")
        print("trees planted: "+ str(num_trees))
        print("\nThe correct answer is A. Climate change could be irreversible by"
        " 2030!! Isn't that insane?")
      answer=input("\nType 1 to continue")
      system("clear")
      if answer=="1":
        print("How many tons of ice are we losing each year?\n\nA)2 billion\nB)1.2 trillion\n"
        "C)1 trillion\nD)7.6 billion")
        answer=input("\nType your answer here")
        if answer=="B":
          system("clear")
          print("You are correct :D\n")
          num_trees = plant_trees(num_trees)
        elif answer in["A","C","D"]:
          system("clear")
          print("You are incorrect :(\n")
          print("trees planted: "+ str(num_trees))
          print("\nThe correct answer is B. Climate change is causing 1.2 trillion tons"
          " of ice to melt each year! That is crazy.")
        answer=input("\nType 1 to continue")
        if answer=="1":
          system("clear")
          print("What was the first known animal to go extinct due to climate change?\n"
          "\nA)California condor\nB)Golden toad\nC)Baiji Dolphin\nD)Mountain gorilla")
          answer=input("\nType your answer here")
          if answer=="B":
            system("clear")
            print("You are correct :D\n")
            num_trees = plant_trees(num_trees)
          elif answer in["A","C","D"]:
            system("clear")
            print("You are incorrect :(\n")
            print("trees planted: "+ str(num_trees))
            print("\nThe correct answer is B. Climate change has gotten 1 known animal"
            " to go extinct so far. If we don't prevent it soon, it'll cause more "
            "beautiful animals to go extinct.")
          answer=input("\nType 1 to continue")
          if answer=="1":
            system("clear")
            print("INTERESTING FACT TIME!\n\nDid you know that sea level has"
            " risen 4 inches since January 1993?")
            answer=input("\nType 1 to move on")
            if answer=="1":
              system("clear")
              print("What is NOT a renewable energy source?\n\nA)Water\nB)Light"
              "\nC)Oil\nD)Wind")
              answer=input("\nType your answer here")
              if answer=="C":
                system("clear")
                print("You are correct! :D\n")  
                num_trees = plant_trees(num_trees)
              elif answer in["A","B","D"]:
                system("clear")
                print("You are incorrect :(\n")
                print("trees planted: "+ str(num_trees))
                print("\nThe correct answer is C. Light, water, and wind are all"
                " clean resources you can use instead of unclean ones like oil, fossil "
                "fuels, and gas. You might want to consider switching to a clean energy"
                " source. It is healthier and better in the long run!")
              answer=input("\nType 1 to continue")
              if answer=="1":
                system("clear")
                print("What absorbs most of the heat we produce?\n\nA)Oceans\nB)"
                "Air\nC)Trees\nD)Crops")
                answer=input("\nType your answer here")
                if answer=="A":
                  system("clear")
                  print("You are correct! :D\n")
                  num_trees = plant_trees(num_trees)
                elif answer in["B","C","D"]:
                  system("clear")
                  print("You are incorrect :(\n")
                  print("trees planted: "+ str(num_trees))
                  print("\nThe correct answer is A. The ocean actually absorbs most of the"
                    " heat we produce! So if we want to save the ocean and the animals living"
                    " in the ocean, we should all work to stop climate change.")
                answer=input("\nType 1 to continue")
                if answer=="1":
                  system("clear")
                  print("INTERESTING FACT TIME!\n\nDid you know that climate change"
                  " increases the spread of annoying bugs and causes fatal diseases like"
                  " malaria, Lyme disease, and dengue?")
                  answer=input("\nType 1 to move on")
                  if answer=="1":
                    system("clear")
                    print("What do green house gasses do?\n\nA)Release toxins that clog air particles"
                    "\nB)Slowly destroy grass\nC)Change temperatures in green houses\n"
                    "D)Trap heat and ruin the climate")
                  answer=input("\nType your answer here")
                  if answer=="D":
                    system("clear")
                    print("You are correct! :D\n")
                    num_trees = plant_trees(num_trees)
                  elif answer in["A","B","C"]:
                      system("clear")
                      print("You are incorrect :(\n")
                      print("trees planted: "+ str(num_trees))
                      print("\nThe correct answer is D. Green house gasses trap heat and build up"
                      ", affecting the climate little by little.")
                  answer=input("\nType 1 to continue")
                  if answer=="1":
                    system("clear")
                    print("What element makes up most of green house gasses?\n\n"
                    "A)Oxygen\nB)Nitrogen\nC)Carbon dioxide\nD)Helium")
                  answer=input("\nType your answer here")
                  if answer=="C":
                    system("clear")
                    print("You are correct! :D\n")
                    num_trees = plant_trees(num_trees)
                  elif answer in["A","B","D"]:
                      system("clear")
                      print("You are incorrect :(\n")
                      print("trees planted: "+ str(num_trees))
                      print("\nThe correct answer is C. Carbon dioxide makes up "
                      " almost 80% of green house gas emissions in the US (as of"
                      " 2020)")
                  answer=input("\nType 1 to continue")
                  if answer=="1":
                    system("clear")
print("THE END OF PART 1!!\nThank you for playing")

p2.start_function()



if __name__ == "__main__":
  main()
