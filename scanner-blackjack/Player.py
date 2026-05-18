class Player:
    def __init__(self, uid="", name="Player"):
        self.UID = uid
        self.name = name
        self.points = 0

    def addPoints(self, num):
        self.points += num

    def getPoints(self):
        return self.points

# Default player instance for module-style usage.
player = Player()