🐍 Snake Claude Game

A modern, customizable implementation of the classic Snake game, built with simplicity and extensibility in mind. This version features smooth gameplay, score tracking, and a modular code structure that allows for easy customization of controls and game mechanics.
🚀 Features

    Classic Gameplay: Eat the food to grow longer while avoiding the walls and your own tail.

    Score System: Real-time score tracking to challenge your high scores.

    Responsive Controls: Default support for keyboard navigation.

    Highly Customizable: Easily modify game settings like speed, colors, and controls.

🕹️ How to Play

    Open index.html in any modern web browser.

    Use the Arrow Keys (default) to move the snake.

    Collect the food to increase your score and length.

    The game ends if you hit a wall or yourself.

⚙️ Customization

This project is designed to be easily tweaked. You can modify the following settings directly in the source code (usually within script.js or the main configuration block):
1. Modifying Navigation Keys

If you prefer WASD or other keys, you can change the key mappings in the event listener section.

    Locate: Look for the keydown event listener.

    Change: Update the key codes (e.g., change ArrowUp to KeyW).

2. Game Physics & Difficulty

You can adjust the core difficulty of the game by changing variables such as:

    Game Speed: Adjust the interval timer (e.g., 100ms for normal, 50ms for hard).

    Grid Size: Change the canvas dimensions or tile size to make the playing field larger or smaller.

3. Visuals

Want a different look? You can modify:

    Snake Color: Change the fill style for the snake segments.

    Food Color: Change the color of the spawned food.

    Background: Update the CSS or Canvas background color.

🛠️ Installation

No installation is required. This is a client-side web application.

    Clone the repository:
    Bash

    git clone https://github.com/mohamedtalaatinfo/snake_claude_game.git

    Navigate to the project folder.

    Open index.html in your browser.

🧪 Technologies Used

    HTML5: For the game structure and Canvas element.

    CSS3: For styling and layout.

    JavaScript (ES6+): For game logic, rendering, and input handling.
