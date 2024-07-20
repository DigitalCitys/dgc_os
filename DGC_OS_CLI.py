import turtle

wn = turtle.Screen()
wn.title("DGC OS Alpha")
wn.bgcolor("black")

wn.addshape("DGC_OS_LOGO.gif")

turtle.shape("DGC_OS_LOGO.gif")

pen = turtle.Turtle()
pen.hideturtle()
pen.color("white")
pen.penup()
pen.goto(0, 200)
# pen.write(f"Clicks: {clicks}", align="center", font=("Arial", 32, "normal"))
pen.write(f"Welcome to DGC OS.\nThis simulated firmware's development is still in its infancy.\nPlease check back later.", align="center", font=("Arial", 12, "normal"))

def clicked(x, y):
    global clicks
    clicks += 1
    pen.clear()
    pen.write(f"Clicks: {clicks}", align="center", font=("Arial", 32, "normal"))

wn.mainloop()
