from turtle import Turtle,Screen
from paddle import Paddle
from shapes import Shapes
from score import Score
import time

# Create the game window
windo=Screen()
windo.bgcolor("black")
windo.setup(1200,900)
windo.tracer(0)  # Turn off auto-refresh (we will update manually)

# Create main game objects
paddle=Paddle()
shape=Shapes()
score=Score()

# Show the rules at the top of the screen
rules=Turtle()
rules.penup()
rules.goto(-450,330)
rules.color("yellow")
rules.hideturtle()
rules.write(
    f"Turtle = 5 points\n"
    f"Square = 2 points\n"
    f"Circle = 1 point\n"
    f"Triangle = return to zero\n"
    f"White turtle = game over ",
    align="center",
    font=("Comic Sans", 15, "normal")
)

game_on=True  # Controls whether the game is still running

while game_on:
    time.sleep(0.05)   # Control game speed (wait 0.05s every loop)
    windo.update()     # Refresh the screen
    score.display_score()  # Show the current score

    # Create or move the shape
    shape.create_shape()
    if shape.ycor() > -370 and shape.active:  # As long as the shape is above the bottom
        shape.go_down()  # Move it down
    elif shape.active:   # If the shape reached the bottom
        shape.remove_shape()  # Remove it

    # Collision detection with the paddle
    if abs(paddle.xcor() - shape.xcor()) < 80 and abs(paddle.ycor() - shape.ycor()) < 20 and shape.active:
        
        # If it’s a square => add 2 points
        if shape.my_shape=="square":
            score.add_two_points()
        
        # If it’s a triangle => reset score to zero
        elif shape.my_shape=="triangle":
            score.return_to_zero()

        # If it’s a turtle
        elif shape.my_shape=="turtle":
            if shape.my_colors !="white":
                score.add_five_points()  # Non-white turtle => add 5 points
            else:
                # White turtle => game over
                windo.bgcolor("red")
                score.game_over()
                game_on=False
        
        # Any other shape (circle etc.) => add 1 point
        else:
            score.add_one_point()
    
        # After collision, remove the shape
        shape.remove_shape()
    
    # Listen for keyboard 
    windo.listen()
    windo.onkey(paddle.move_right,"Right")   # Right arrow => move paddle right
    windo.onkey(paddle.move_left,"Left")     # Left arrow => move paddle left




# Wait for click before closing (when game ends)
windo.exitonclick()
