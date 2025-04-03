import time

class GameLogger:
    def __init__(self, filename="game_log.txt"):
        self.filename = filename

    def log_game(self, score, duration):
        with open(self.filename, "a") as file:
            file.write(f"Score: {score}, Duration: {duration:.2f} seconds, Time: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
