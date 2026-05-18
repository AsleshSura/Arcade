import Player
import bisect


# Given UID and name from scanner app

class Database:
    Database = {}

    def newPlayer(UID, name):
        Database.append(UID, Player(UID))
    
    def findPlayer(UID):
        if UID not in Database:
            self.newPlayer(UID)
        return Database[UID]
        