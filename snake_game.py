#!/usr/bin/env python3
"""
╔══════════════════════════════════════╗
║        🐍  CLI SNAKE GAME  🐍        ║
╚══════════════════════════════════════╝
Configurable controls, speed & fruits!
"""

import curses
import random
import time
import sys

# ──────────────────────────────────────────
#  CONFIGURATION  ← tweak anything here!
# ──────────────────────────────────────────
CONFIG = {
    # Movement keys — HJKL (vim-style) are the defaults
    "key_up":    ord('k'),   # k = up
    "key_down":  ord('j'),   # j = down
    "key_left":  ord('h'),   # h = left
    "key_right": ord('l'),   # l = right

    # Arrow keys — uncomment to use instead:
    # "key_up":    curses.KEY_UP,
    # "key_down":  curses.KEY_DOWN,
    # "key_left":  curses.KEY_LEFT,
    # "key_right": curses.KEY_RIGHT,

    # WASD — uncomment to use instead:
    # "key_up":    ord('w'),
    # "key_down":  ord('s'),
    # "key_left":  ord('a'),
    # "key_right": ord('d'),

    # Snake speed: seconds between each move (lower = faster)
    # Suggested range: 0.05 (blazing) → 0.3 (relaxed)
    "speed": 0.12,

    # How many fruits are on the board at the same time
    "fruit_count": 3,
}
# ──────────────────────────────────────────


def draw_border(win, h, w):
    win.attron(curses.color_pair(3))
    win.border()
    win.attroff(curses.color_pair(3))


def place_fruits(snake, fruits, h, w, count):
    """Ensure exactly `count` fruits exist on the board."""
    occupied = set(map(tuple, snake)) | {tuple(f) for f in fruits}
    while len(fruits) < count:
        pos = [random.randint(1, h - 2), random.randint(1, w - 2)]
        if tuple(pos) not in occupied:
            fruits.append(pos)
            occupied.add(tuple(pos))


def main(stdscr):
    # ── curses setup ──────────────────────────────────────────────
    curses.curs_set(0)
    stdscr.nodelay(True)
    stdscr.timeout(0)

    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN,  curses.COLOR_BLACK)  # snake
    curses.init_pair(2, curses.COLOR_RED,    curses.COLOR_BLACK)  # fruit
    curses.init_pair(3, curses.COLOR_CYAN,   curses.COLOR_BLACK)  # border
    curses.init_pair(4, curses.COLOR_YELLOW, curses.COLOR_BLACK)  # score
    curses.init_pair(5, curses.COLOR_WHITE,  curses.COLOR_BLACK)  # text

    h, w = stdscr.getmaxyx()
    if h < 15 or w < 30:
        stdscr.addstr(0, 0, "Terminal too small! Please resize to at least 30x15.")
        stdscr.refresh()
        time.sleep(3)
        return

    # ── initial state ─────────────────────────────────────────────
    mid_y, mid_x = h // 2, w // 2
    snake  = [[mid_y, mid_x], [mid_y, mid_x - 1], [mid_y, mid_x - 2]]
    direction = CONFIG["key_right"]   # always matches whatever keys are configured
    fruits: list = []
    place_fruits(snake, fruits, h, w, CONFIG["fruit_count"])
    score  = 0
    speed  = CONFIG["speed"]

    key_up    = CONFIG["key_up"]
    key_down  = CONFIG["key_down"]
    key_left  = CONFIG["key_left"]
    key_right = CONFIG["key_right"]

    last_move = time.time()

    # ── game loop ─────────────────────────────────────────────────
    while True:
        # --- input ---
        key = stdscr.getch()
        if key == ord('q'):
            break
        if key in (key_up, key_down, key_left, key_right):
            # prevent 180° reversal
            if not (
                (key == key_up    and direction == key_down)  or
                (key == key_down  and direction == key_up)    or
                (key == key_left  and direction == key_right) or
                (key == key_right and direction == key_left)
            ):
                direction = key

        # --- tick only when enough time has passed ---
        now = time.time()
        if now - last_move < speed:
            time.sleep(0.005)
            continue
        last_move = now

        # --- move head ---
        head = snake[0][:]
        if   direction == key_up:    head[0] -= 1
        elif direction == key_down:  head[0] += 1
        elif direction == key_left:  head[1] -= 1
        elif direction == key_right: head[1] += 1

        # --- collision: walls ---
        if head[0] <= 0 or head[0] >= h - 1 or head[1] <= 0 or head[1] >= w - 1:
            break

        # --- collision: self ---
        if head in snake:
            break

        snake.insert(0, head)

        # --- eat fruit? ---
        eaten = None
        for f in fruits:
            if head == f:
                eaten = f
                break
        if eaten:
            fruits.remove(eaten)
            score += 10
            # speed up slightly every 5 fruits (floor at 0.04)
            speed = max(0.04, speed - 0.003)
            place_fruits(snake, fruits, h, w, CONFIG["fruit_count"])
        else:
            snake.pop()

        # --- draw ---
        stdscr.erase()
        draw_border(stdscr, h, w)

        # score bar
        stdscr.attron(curses.color_pair(4))
        stdscr.addstr(0, 2, f" Score: {score}  Length: {len(snake)}  [Q] Quit ")
        stdscr.attroff(curses.color_pair(4))

        # fruits
        stdscr.attron(curses.color_pair(2) | curses.A_BOLD)
        for f in fruits:
            if 0 < f[0] < h - 1 and 0 < f[1] < w - 1:
                stdscr.addstr(f[0], f[1], "●")
        stdscr.attroff(curses.color_pair(2) | curses.A_BOLD)

        # snake
        stdscr.attron(curses.color_pair(1) | curses.A_BOLD)
        stdscr.addstr(snake[0][0], snake[0][1], "▓")   # head
        stdscr.attroff(curses.color_pair(1) | curses.A_BOLD)
        stdscr.attron(curses.color_pair(1))
        for seg in snake[1:]:
            if 0 < seg[0] < h - 1 and 0 < seg[1] < w - 1:
                stdscr.addstr(seg[0], seg[1], "░")     # body
        stdscr.attroff(curses.color_pair(1))

        stdscr.refresh()

    # ── game over screen ──────────────────────────────────────────
    stdscr.erase()
    draw_border(stdscr, h, w)
    msg1 = "💀  GAME OVER  💀"
    msg2 = f"Final Score : {score}"
    msg3 = f"Snake Length: {len(snake)}"
    msg4 = "Press any key to exit"
    cx = w // 2
    cy = h // 2
    stdscr.attron(curses.color_pair(4) | curses.A_BOLD)
    stdscr.addstr(cy - 2, cx - len(msg1) // 2, msg1)
    stdscr.attroff(curses.color_pair(4) | curses.A_BOLD)
    stdscr.attron(curses.color_pair(5))
    stdscr.addstr(cy,     cx - len(msg2) // 2, msg2)
    stdscr.addstr(cy + 1, cx - len(msg3) // 2, msg3)
    stdscr.addstr(cy + 3, cx - len(msg4) // 2, msg4)
    stdscr.attroff(curses.color_pair(5))
    stdscr.refresh()
    stdscr.nodelay(False)
    stdscr.getch()


if __name__ == "__main__":
    print(__doc__)
    print("Starting in 1 second…  (resize your terminal if needed)\n")
    time.sleep(1)
    try:
        curses.wrapper(main)
    except KeyboardInterrupt:
        pass
    print("\nThanks for playing! 🐍")
