import random

class Egg:
    def __init__(self, canvas, color, score):
        self.canvas = canvas
        self.color = color
        self.score = score
        
        self.id = canvas.create_oval(0, 0, 25, 25, fill=color)
        
        self.canvas.move(self.id, random.randint(10, 490), -10)
        
        self.y = random.randint(1, 4)