# Arcade

Arcade is a badge-driven arcade and point system built for Hack Club Stasis, a weekend-long 60 hour hardware hackathon in downtown Austin. The project uses NFC badge scans as the front door, then routes each player into a set of game experiences that let them earn, lose, or gamble points. The overall idea is a pyramid or arcade: the NFC badge system is the entry point, and every other game is a way to save, spend, or invest your in-game balance.

## What’s In This Repo

This repo is split into a few connected pieces:

- `game-manager/` contains the Tkinter dashboard that reads NFC badges, creates player profiles, tracks balances, and launches games.
- `pcsclite_backend.py` wraps PC/SC smart-card access for badge scanning.
- `Scanner&Database.py`, `Database.py`, and `Player.py` provide SQLite-backed badge and player storage.
- `scanner-blackjack/` is a small scanner-based blackjack prototype.
- `piano-game/` contains the rhythm game, chart editor, chart loader, and chart conversion tools.

## How The System Works

1. A badge is scanned through the NFC reader.
2. The badge UID is looked up in the local database.
3. New players can enter their name and start with an initial point balance.
4. Returning players are loaded automatically.
5. The game manager then sends players into one of the available games.
6. Game outcomes update the stored points for that badge.

## Key Components

### NFC Badge and Player Data

The badge database stores scan history, badge metadata, and point totals in SQLite. The helper modules in the repo handle creating players, finding existing players, and recording badge activity.

### Game Manager

The main hub is the Tkinter dashboard in `game-manager/game_manager.py`. It handles:

- badge scans
- new player setup
- returning player lookup
- point tracking
- game selection

### Scanner Blackjack

`scanner-blackjack/` is a smaller game prototype built around barcode or badge-based input. It is meant to demonstrate how a badge scan can be turned into a simple point-based mini-game.

### Piano Rhythm Game

`piano-game/` contains a rhythm game and charting workflow:

- `game.py` is the game itself
- `chart_editor.py` is the visual note editor
- `loader.py` loads chart JSON files
- `charts.py` discovers available songs
- `convert_charts_to_json.py`, `make_charts.py`, and `list_charts.py` support chart creation and management

## Setup

This project is Python-based and uses a mix of desktop UI, hardware access, and game libraries. Typical dependencies include:

- Python 3
- `pygame`
- `pyserial`
- `pyscard` / smartcard support for NFC scanning

Exact setup will vary depending on which part of the repo you want to run and whether you have NFC hardware connected.

## Running The Main Pieces

The repo does not have a single unified launcher yet. The main entry points are:

- `python game-manager/game_manager.py` for the badge-driven arcade dashboard
- `python scanner-blackjack/main.py` for the blackjack prototype
- `python piano-game/game.py` for the rhythm game
- `python piano-game/chart_editor.py` for the visual chart editor

# Created by
This amazing project was created due to the combined effort of Aslesh Sura, Connor, OJ, Eli, Nina, and Sharon.