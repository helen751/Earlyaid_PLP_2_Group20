import os

class ColoredMessage:
    # function to show messages in different color (This will help make my application more interactive)
    def __init__(self):
        # Defining ANSI color codes
        self.colors = {
            "red": "\033[91m",  # red color code
            "green": "\033[92m",  # green color code
            "yellow": "\033[93m",  # orange color code
            "blue": "\033[94m",  # blue color code
            "reset": "\033[0m"  # default terminal color
        }

    def print(self, text, color):
        # Print the parsed text with the chosen color and reset after
        print(f'{self.colors[color]}{text}{self.colors["reset"]}')
