class Snake:
    def __init__(self):
        self.position = 1

    def move(self):
        dice_value = int(input("Enter the sum of dice: "))
        if dice_value == 0:
            return 0

        self.position += dice_value
        if self.position == 9:
            self.position = 34
            return "you are now on square " + str(self.position)
        elif self.position == 40:
            self.position = 64
            return "you are now on square " + str(self.position)
        elif self.position == 54:
            self.position = 19
            return "you are now on square " + str(self.position)
        elif self.position == 67:
            self.position = 86
            return "you are now on square " + str(self.position)
        elif self.position == 90:
            self.position = 48
            return "you are now on square " + str(self.position)
        elif self.position == 99:
            self.position = 77
            return "you are now on square " + str(self.position)
        elif self.position >= 100:
            return 100
        else:
            return "you are now on square " + str(self.position)
