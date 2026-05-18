class Database:
    players = {}

    @staticmethod
    def newPlayer(uid, name=None):
        import Player
        Database.players[uid] = Player.Player(uid, name)
    
    @staticmethod
    def findPlayer(uid, name=None):
        if uid not in Database.players:
            Database.newPlayer(uid, name)
        return Database.players[uid]
        