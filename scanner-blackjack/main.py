import Player
import random
import tkinter as tk
import sqlite3
import threading
import queue
import time
import sys
import os
import subprocess
import uuid
from datetime import datetime

BG       = "#0d0d1a"
CARD_BG  = "#004191"
PANEL_BG = "#1a1a2e"
ACCENT   = "#e94560"
BLUE     = "#004191"
TEXT     = "#ffffff"
MUTED    = "#8888aa"
GREEN    = "#4caf50"
YELLOW   = "#f0c040"

F_TITLE   = ("Helvetica", 28, "bold")
F_HEAD    = ("Helvetica", 18, "bold")
F_SUBHEAD = ("Helvetica", 14, "bold")
F_BODY    = ("Helvetica", 13)
F_MUTED   = ("Helvetica", 11)
F_NUM     = ("Helvetica", 36, "bold")
F_BTN     = ("Helvetica", 14, "bold")
F_BTN_SM  = ("Helvetica", 12, "bold")

def _btn(parent, text, command, color=ACCENT, fg=TEXT, font=None, **kw):
    return tk.Button(
        parent, text=text, command=command,
        bg=color, fg=fg, font=font or F_BTN,
        relief="flat", cursor="hand2",
        padx=16, pady=9,
        activebackground=color, activeforeground=fg,
        **kw,
    )

def _lbl(parent, text, color=TEXT, bg=None, font=None, anchor="center", **kw):
    return tk.Label(
        parent, text=text, fg=color, bg=bg or PANEL_BG,
        font=font or F_BODY, anchor=anchor, **kw,
    )

def _card(parent, **kw):
    return tk.Frame(parent, bg=CARD_BG, bd=0, relief="flat", **kw)

class ScannerBlackjackGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Scanner Blackjack")
        self.configure(bg=PANEL_BG)
        self.geometry("960x620")
        self.resizable(False, False)


        self._build_header()
        self.body = tk.Frame(self, bg=PANEL_BG)
        self.body.pack(fill=tk.BOTH, expand=True)

        self.show_idle()

    def _build_header(self):
        hdr = tk.Frame(self, bg=BLUE, height=52)
        hdr.pack(fill=tk.X)
        hdr.pack_propagate(False)

        _lbl(hdr, "Scanner Blackjack", font=F_HEAD, bg=BLUE).pack(
            side=tk.LEFT, padx=18, pady=10
        )
        _lbl(hdr, "Game Manager", color=MUTED, font=F_BODY, bg=BLUE).pack(
            side=tk.LEFT, pady=10
        )

    def _clear(self):
        for w in self.body.winfo_children():
            w.destroy()

    def _center(self):
        """Return a frame centered in body."""
        f = tk.Frame(self.body, bg=PANEL_BG)
        f.place(relx=0.5, rely=0.5, anchor="center")
        return f


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

if __name__ == "__main__":
    app = ScannerBlackjackGame()
    app.mainloop()