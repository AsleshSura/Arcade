class Player:
    points = 0
    UID = ""

    def __init__(self, uid):
        self.UID = uid

    def addPoints(self, num):
        self.points += num

    def getPoints(self):
        return self.points