#from .Database import Player
import random

PlayerUID = "io"
PlayerPoints = 0

BlackjackThreshold = 21

print("Hey twin, welcome to Scanner Blackjack!")

score = 0
failCase = False

while not failCase:
    Barcode = input("Scan your barcode: ")
    number = random.choice(Barcode)
    score += int(number)

    print("You got a", number +".","You're total score is:", score)

    if score > BlackjackThreshold:
        failCase = True
        break

    choice = input("Would you like to keep going? [Y]: ")

    if choice.lower == ("y" or "yes"):
        pass
    elif choice.lower == ("n" or "no"):
        break

if failCase:
    print("Your score exceeds the limit of", str(BlackjackThreshold) + ".")
    print("You will lose the equivalent number of points from your account.")
    print("Points lost:", score)
    score *= -1

#Player.addPoints(score)
PlayerPoints += score

print("Your fi nal score is:", score)
print("Points won from this game have been added to your account.")
print("Account Balance:", PlayerPoints)