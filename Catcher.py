class Catcher:
    
    def __init__(self, canvas, color, score):
        
        self.canvas = canvas
        self.score = score

        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)

        self.canvas.move(self.id, 200, 350)
        
        self.x = 0
        
        self.canvas_width = self.canvas.winfo_width()
        
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)