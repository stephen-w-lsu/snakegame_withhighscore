from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.load_high_score()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def save_high_score(self):
        save_score_file = open("high_score.txt", "w+")
        save_score_file.write(f"{self.high_score}")
        save_score_file.close()

    def load_high_score(self):
        load_score_file = open("high_score.txt")
        latest_high_score = load_score_file.readlines()
        load_score_file.close()
        return int(latest_high_score[0])
