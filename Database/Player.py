class Player:
    def __init__(self, uid, name=None):
        self.UID = uid
        self.name = name
        self.points = 0

    def addPoints(self, num):
        self.points += num

    def getPoints(self):
        return self.points