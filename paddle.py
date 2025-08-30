from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")        # Paddle starts as a square
        self.penup()                # Prevent drawing lines when moving
        self.goto(0, -320)         
        self.shapesize(1, 8)        # Stretch shape => height=1, width=8
        self.color("white")         

    def move_right(self):
        # Move paddle to the right
        self.goto(self.xcor() + 60, self.ycor())
    
    def move_left(self):
        # Move paddle to the left
        self.goto(self.xcor() - 60, self.ycor())
