from os import closerange, system
import turtle
import time
import p2

screen = turtle.Screen()
screen.setup(400, 400)
x = 0
screen.bgpic("background1.gif")
time.sleep(2)
tree = ("best-tree.gif")
onion = ("onions.gif")
corn = ("corn.gif")
lettuce = ("lettuce.gif")
tomato = ("tomato.gif")
steak = ("steak for tacos.gif")
chicken = ("chicken for taco.gif")
screen.addshape(tree)
screen.addshape(onion)
screen.addshape(corn)

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
tom.circle(100, 180)
tom.penup()
style = ('arial', 30)
tom.write("Hi!")
#tom._delay(4000)
tom.clear()
tom.hideturtle()
screen.bgpic("nopic")




bob = turtle.Turtle()
bob.hideturtle()
bob.penup()
bob.goto(80,100)
def display_points(points,dollars):
  bob.clear()
  bob.pendown()
  bob.write(str(points)+"pts",font=("arial",30,"normal"))
  bob.penup()
  bob.backward(200)
  bob.pendown()
  bob.write("$"+str(dollars),font=("arial",30,"normal"))
  bob.penup()
  bob.forward(200)

def main():

  
  p2.start_function(tree_list, tree, onion,screen,corn,chicken,lettuce,steak,tomato)
  p2.end_function()


if __name__ == "__main__":
  main()
