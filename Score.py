class Score:
    
    def __init__(self, canvas):
        self.canvas = canvas
        self.score = 0
        self.lost = 0
        self.text = ""
        self.show_text()

    def show_text(self):

        if self.text == "":
        
            self.text = self.canvas.create_text(
                350, 10, 
                text=f"Спіймав: 0 Пропустив: 0", 
                font=('Helvetica', 16)
            )
        else:
        
            self.canvas.itemconfig(
                self.text, 
                text=f"Спіймав: {self.score} Пропустив: {self.lost}"
            )