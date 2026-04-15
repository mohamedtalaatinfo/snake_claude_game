# 🐍 CLI Snake Game

A classic Snake game that runs in your terminal — built in Python, zero dependencies.

The default controls are `h j k l`, the same keys used to navigate in Vim. If you're trying to build that muscle memory, every game session is secretly a practice round.

---

## Requirements

- Python 3.x
- A terminal at least 30×15 in size

No external packages needed. The game uses Python's built-in `curses` library.

---

## How to run

```bash
python3 snake.py
```

---

## Controls

| Key | Action |
|-----|--------|
| `h` | Move left |
| `j` | Move down |
| `k` | Move up |
| `l` | Move right |
| `q` | Quit |

---

## Modifying game settings

All settings live in the `CONFIG` block at the top of `snake.py`. Open the file and tweak anything there — no need to touch the rest of the code.

```python
CONFIG = {
    "key_up":    ord('k'),
    "key_down":  ord('j'),
    "key_left":  ord('h'),
    "key_right": ord('l'),
    "speed": 0.12,
    "fruit_count": 3,
}
```

### Navigation keys

The default is `h j k l` (Vim-style). Two alternatives are already written in the file as commented-out lines — just swap which block is active.

**Switch to arrow keys:**
```python
"key_up":    curses.KEY_UP,
"key_down":  curses.KEY_DOWN,
"key_left":  curses.KEY_LEFT,
"key_right": curses.KEY_RIGHT,
```

**Switch to WASD:**
```python
"key_up":    ord('w'),
"key_down":  ord('s'),
"key_left":  ord('a'),
"key_right": ord('d'),
```

### Speed

The `speed` value is the delay in seconds between each move. Lower means faster.

| Value | Feel |
|-------|------|
| `0.05` | Blazing fast |
| `0.12` | Default |
| `0.20` | Relaxed |
| `0.30` | Very slow |

> The snake also speeds up slightly as you eat more fruits, regardless of the starting speed.

### Fruit count

`fruit_count` controls how many fruits appear on the board at the same time. Default is `3`. Increase it for a more chaotic board, lower it for a cleaner game.

---

## Scoring

- **+10 points** per fruit eaten
- Score and snake length are shown at the top of the screen during the game
