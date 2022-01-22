class Snake:
    def __init__(self):
        self.pos = 1

    def move(self, dice):
        self.pos += dice
        if self.pos == 99:
            self.pos = 77
        elif self.pos == 90:
            self.pos = 48
        elif self.pos == 54:
            self.pos = 19
        elif self.pos == 9:
            self.pos = 34
        elif self.pos == 40:
            self.pos = 64
        elif self.pos == 67:
            self.pos = 86
        return self.pos