# A Rock, Paper and Scissors Game
#### Video Demo:  <https://youtu.be/vxvlg9EFi90>
#### Description:
This project is a terminal-based, interactive implementation of the classic game "Rock, Paper, Scissors," enhanced with automated input validation, a dynamic score-tracking system, custom ASCII graphics, and robust unit testing. Built as the final project for CS50's Introduction to Programming with Python (CS50P), the application provides a modular, clean, and user-friendly experience directly inside the command-line interface.

The primary objective of the program is to allow a human user to play consecutive rounds of Rock, Paper, Scissors against a randomized computer opponent. The game maintains an ongoing score for both players and continues executing until either the user or the computer reaches a predetermined threshold of 5 points. Once the score threshold is met, the program declares the ultimate winner, displays a custom banner using the third-party `cowsay` library, and terminates.

---

### Project File Structure

The project repository is structured into four primary files, each serving a distinct purpose in the application lifecycle:

* **`project.py`**: This is the main file where the program runs. It implements the main application workflow and defines four helper functions: `main`, `valid`, `win`, `lose`, and `draw`.
* The `random` library is used for computer led choices
* The `valid` function verifies whether user input conforms to expected choices (`rock`, `paper`, or `scissors`), safely returning `None` for invalid inputs to trigger re-prompting in `main` function
* The `win`, `lose`, and `draw` functions encapsulate the win/loss conditional evaluation logic, comparing player choices against computer choices and returning standardized string outputs.
* **`test_project.py`**: This file contains the automated unit tests written for `pytest`. It tests each helper function (`valid`, `win`, `lose`, and `draw`) across multiple test cases—including uppercase/lowercase inputs, invalid string entries, and edge-case winning/losing combinations—without relying on manual user interaction or terminal prompts.
* **`requirements.txt`**: This file lists the external third-party dependencies required to run the project. It is strictly limited to `cowsay`, ensuring clean dependency management.
* **`README.md`**: The comprehensive documentation file describing the project overview, file mechanics, design choices, and setup instructions.

---

### Key Design Choices & Trade-offs

During the development process, several structural and design choices were evaluated to balance code maintainability, testing requirements, and user experience:

1. **Decoupling Logic from Side Effects for `pytest` Compatibility:**
   Initially, conditional checks directly printed output messages to the console inside helper functions. However, to make functions testable with `pytest`, all helper functions (`valid`, `win`, `lose`, `draw`) were altered to be pure functions that return values rather than printing or calling `input()`. This separation ensures that the main loop handles console I/O while helper functions remain strictly computational.

2. **Input Normalization vs. Strict Validation:**
   To make the interface forgiving, user inputs are converted to lowercase immediately upon entry using `.lower()`. If an invalid string (like "banana" or empty space) is entered, the `valid` function returns `None`, forcing the program into an inner validation loop that re-prompts the user until a valid move is submitted.

3. **Win/Loss Score Thresholding:**
   Instead of running an infinite game or fixed number of rounds, a score threshold of 5 was selected. This guarantees a decisive outcome per session, providing a clear stopping condition for both human players and automated test demonstrations.

---

### How to Run the Project

1. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt





