from turtle import Turtle

class Score(Turtle):
    
    def __init__(self):
        self.score = 0     
        # Added highscore system: reads saved highscore from "Highscore.txt"
        self.highscore = self.get_high_score()      
        super().__init__()
        self.goto(0, 360)          
        self.color("white")        
        self.penup()            
        self.hideturtle()       
    
    
    def display_score(self):
        # Show current score and highscore on screen
        self.clear()
        self.write(f"Score: {self.score}\nHighscore: {self.highscore} ", 
                   align="center", font=("Comic Sans", 27, "normal"))

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

    def get_high_score(self):
        # Reads the saved highscore from file
        with open("Highscore.txt","r") as highscore:
            return int(highscore.read())
    
    def save_high_score(self):
        # Saves the current score as the new highscore into file
        with open("Highscore.txt","w") as highscore:
            highscore.write(str(self.score))

    def game_over(self):
        # At game over, update highscore if current score is higher
        if self.score > self.highscore:
            self.highscore = self.score
            self.save_high_score()

        # Display final messages in the center
        self.goto(0, 0)
        self.write("  Game over\n", align="center", font=("Comic Sans", 27, "normal"))
        self.goto(0, -35)
        self.write(f"   Your final score {self.score}\n   Your high score {self.highscore}", 
                   align="center", font=("Comic Sans", 27, "normal"))
