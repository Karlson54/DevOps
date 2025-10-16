class Score:
    
    def __init__(self, canvas):
        self.canvas = canvas
        self.score = 0
        self.lost = 0
        self.text = ""
        self.show_text()