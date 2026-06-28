# Py Asteroids Game

A simple Asteroids-style arcade game built with Python and Pygame.

## Overview

Pilot a ship through a field of asteroids. Rotate, thrust, and shoot to destroy incoming rocks before they collide with you.

## Gameplay

- `A` to rotate left
- `D` to rotate right
- `W` to thrust forward
- `S` to thrust backward
- `Space` to shoot

Asteroids spawn from the edges of the screen and move across the playfield. The player ship can fire shots to destroy asteroids. The game ends if an asteroid collides with the ship.

## Requirements

- Python 3.13 or newer
- Pygame 2.6.1

## Install

Install the dependency with pip:

```bash
python -m pip install pygame==2.6.1
```

## Run

From the project root:

```bash
python main.py
```

## Project Structure

- `main.py` — game entry point and main loop
- `player.py` — player ship movement, rotation, and shooting
- `asteroid.py` — asteroid behavior and collision handling
- `asteroidfield.py` — asteroid spawning logic
- `shot.py` — projectile movement
- `circleshape.py` — base shape and collision helpers
- `constants.py` — game configuration values
- `logger.py` — optional JSONL runtime logging for state and events
- `game_state.jsonl` — captured state snapshots while running
- `game_events.jsonl` — captured in-game events while running

## Notes

- The game uses `pygame.sprite.Group` for update and draw management.
- The logger writes snapshots of groups and sprites into `game_state.jsonl` once per second.

Enjoy the game!
