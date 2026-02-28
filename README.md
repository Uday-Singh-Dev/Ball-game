# Orb Chase

A top-down survival game built in Python using Tkinter, where the player collects orbs, avoids a tracking enemy, and spends currency on upgrades — featuring a full save and load system, character customisation, and a letter-by-letter text engine.

---

## Overview

This project was built to explore enemy AI, a progression and upgrade system, and user authentication through a file-based save system. The gameplay loop centres on collecting orbs while avoiding an enemy that tracks the player using normalised vector movement, with an in-game shop allowing the player to spend orbs on permanent upgrades between sessions.

The objective was to build a complete game experience — from the main menu and save system through to the shop, customisation screen, and level progression — without the use of any classes, relying entirely on functions and global state.

---

## Key Features

- Enemy AI that tracks the player using normalised vector movement
- Three orb types — blue orbs for currency, green orbs for healing, purple orbs that teleport the player
- In-game shop with upgradeable speed, health orb value, and a full heal option
- Level progression system that increases enemy speed and damage while raising orb value
- Username and password save system using plain text files
- Save and load functionality that restores all game state including upgrades and player colour
- Character customisation with five colour options
- Letter-by-letter text engine with skippable animations and a bobbing triangle pointer
- Health bar that changes colour based on current health
- Death sequence that halves orb currency and resets stats on respawn

---

## Architecture Highlights

- Entirely function-based structure with no classes
- Enemy movement calculated each frame using distance, normalisation, and speed scaling
- Collision detection handled by querying canvas overlap IDs for each object
- Save file encodes all game state into a single delimited string, parsed on load
- Scene switching managed by packing and unpacking individual canvas layers

---

## Technologies Used

- Python
- Tkinter

---

## What I Learned

- Building enemy AI that tracks and reacts to the player using vector maths
- Designing a progression and upgrade system that stays balanced across levels
- Implementing username and password authentication using file handling
- Building a complete game loop without OOP, relying purely on functions and global state

---

## Controls

- W A S D - Move

---

## How to Run

1. Install Python 3.x
2. Run the game:
   python orb_chase.py
3. On first launch select New Game, enter a username and password
4. On return select Load Game and enter your credentials to restore your save
