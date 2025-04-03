# snake.py
import sys
import pygame
import random
import time
from logger import GameLogger

# Initialize pygame
pygame.init()

# Set screen width and height
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Yet Another Snake Game")

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (213, 50, 80)
blue = (50, 153, 213)

# Snake settings
snake_block = 10
snake_speed = 15

clock = pygame.time.Clock()
font = pygame.font.SysFont("bahnschrift", 25)

class SnakeGame:
    def __init__(self):
        self.game_over = False
        self.game_close = False
        self.x, self.y = width / 2, height / 2
        self.x_change, self.y_change = 0, 0
        self.snake = []
        self.length_of_snake = 1
        self.score = 0
        self.foodx, self.foody = self.random_food_position()
        self.logger = GameLogger()
        self.start_time = time.time()

    def random_food_position(self):
        return (round(random.randrange(0, width - snake_block) / 10.0) * 10.0,
                round(random.randrange(0, height - snake_block) / 10.0) * 10.0)

    def show_message(self, msg, color, x, y):
        mesg = font.render(msg, True, color)
        screen.blit(mesg, [x, y])

    def show_score(self):
        score_text = font.render(f"Score: {self.score}", True, white)
        screen.blit(score_text, [10, 10])

    def game_loop(self):
        while not self.game_over:
            while self.game_close:
                screen.fill(black)
                self.show_message("You Lost! Press Q-Quit or P-Play Again", red, 250, height / 2)
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            self.logger.log_game(self.score, time.time() - self.start_time)
                            self.game_over = True
                            self.game_close = False
                        if event.key == pygame.K_p:
                            self.__init__()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.logger.log_game(self.score, time.time() - self.start_time)
                    self.game_over = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT and self.x_change == 0:
                        self.x_change = -snake_block
                        self.y_change = 0
                    elif event.key == pygame.K_RIGHT and self.x_change == 0:
                        self.x_change = snake_block
                        self.y_change = 0
                    elif event.key == pygame.K_UP and self.y_change == 0:
                        self.y_change = -snake_block
                        self.x_change = 0
                    elif event.key == pygame.K_DOWN and self.y_change == 0:
                        self.y_change = snake_block
                        self.x_change = 0

            if self.x >= width or self.x < 0 or self.y >= height or self.y < 0:
                self.game_close = True

            self.x += self.x_change
            self.y += self.y_change
            screen.fill(blue)
            pygame.draw.rect(screen, green, [self.foodx, self.foody, snake_block, snake_block])

            snake_head = [self.x, self.y]
            self.snake.append(snake_head)
            if len(self.snake) > self.length_of_snake:
                del self.snake[0]

            for segment in self.snake[:-1]:
                if segment == snake_head:
                    self.game_close = True

            for segment in self.snake:
                pygame.draw.rect(screen, white, [segment[0], segment[1], snake_block, snake_block])

            self.show_score()
            pygame.display.update()

            if self.x == self.foodx and self.y == self.foody:
                self.foodx, self.foody = self.random_food_position()
                self.length_of_snake += 1
                self.score += 1

            clock.tick(snake_speed)

        pygame.quit()
        sys.exit()