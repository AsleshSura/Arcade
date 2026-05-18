import Player
import random
import game_manager


player = Player.player
PlayerUID = player.UID
PlayerName = player.name
PlayerPoints = player.points

BlackjackThreshold = 21

print("Hey", PlayerName + ", welcome to Scanner Blackjack!")

score = 0
failCase = False

while not failCase:
    Barcode = input("Scan your barcode: ")
    number = random.choice(Barcode)
    score += int(number)

    print("You got a", number +".","You're total score is:", score)

    if score > BlackjackThreshold:
        failCase = True

    choice = input("Would you like to keep going? [Y]: ")

    if choice.lower() in ("y", "yes"):
        pass
    elif choice.lower() in ("n", "no"):
        break

if failCase:
    print("Your score exceeds the limit of", str(BlackjackThreshold) + ".")
    print("You will lose the equivalent number of points from your account.")
    print("Points lost:", score)
    score *= -1

player.addPoints(score)

print("Your final score is:", score)
print("Points won from this game have been added to your account.")
print("Account Balance:", player.points)
