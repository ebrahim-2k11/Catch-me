from turtle import Turtle
import random

class Shapes(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()         
        self.active = False  # Flag → tells if a shape is currently active (on screen)

    def create_shape(self):
        # Only create a new shape if there isn't already one active
        if not self.active:   
            colors=["white","red","green"]
            shapes=["turtle","square","triangle","circle","turtle","turtle"]
            x_line=(0,-100,-150,-200,-250,-300,-350,-400,-430,
                    100,150,200,250,300,350,400,430)
            size=(1,1.5,2)
        
            # Randomly shape and color
            self.my_shape=random.choice(shapes)
            self.my_colors=random.choice(colors)
        
            # Apply shape and color
            self.shape(self.my_shape)
            self.color(self.my_colors)
        
            # Place the shape at a random x position at the top of the screen
            self.goto(random.choice(x_line),350)
            
            # Randomly choose size
            self.shapesize(random.choice(size))
            
            # Set direction downwards (270 = south)
            self.setheading(270)

            # Mark the shape as active =visible on screen
            self.active = True   

    def go_down(self):
        # Move the shape down if it’s active
        if self.active:
            self.forward(20)

    def remove_shape(self):
        """Remove the current shape and allow new one to be created"""
        self.clear()         # Erase drawing (if any)
        self.active = False  # Reset flag => next loop can create another shape
