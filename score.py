from turtle import Turtle

class Score(Turtle):
    
    def __init__(self):
        self.score = 0             
        super().__init__()
        self.goto(0, 360)          
        self.color("white")        
        self.penup()            
        self.hideturtle()       
    
    def display_score(self):
        # Clear previous score and rewrite the current score
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Comic Sans", 27, "normal"))

    def add_two_points(self):
        """+2 points when catching a square"""
        self.score += 2

    def add_one_point(self):
        """+1 point when catching circle (or other shapes except square/turtle)"""
        self.score += 1
    
    def return_to_zero(self):
        """Score goes back to 0 when catching a triangle"""
        self.score = 0
    
    def add_five_points(self):
        """+5 points when catching a turtle (except white turtle)"""
        self.score += 5

    def game_over(self):
        # Display final "Game Over" message in the center of the screen
        self.goto(0, 0)
        self.write("  Game over", align="center", font=("Comic Sans", 27, "normal"))
        self.goto(0, -35)
        self.write(f"Your final score {self.score}", align="center", font=("Comic Sans", 27, "normal"))
