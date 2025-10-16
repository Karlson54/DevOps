import random

class Egg:
    def __init__(self, canvas, color, score):
        self.canvas = canvas
        self.color = color
        self.score = score
        
        self.id = canvas.create_oval(0, 0, 25, 25, fill=color)
        
        self.canvas.move(self.id, random.randint(10, 490), -10)
        
        self.y = random.randint(1, 4)

    def draw(self):
        
        self.canvas.move(self.id, 0, self.y)
        
        pos = self.canvas.coords(self.id)
        
        if pos[3] >= self.canvas.winfo_height():
            self.score.lost_egg()
            self.canvas.delete(self.id)
            return 'hit bottom'
        
        return None