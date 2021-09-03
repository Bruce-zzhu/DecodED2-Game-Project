import pygame
from pygame.locals import KEYDOWN, KEYUP, K_LEFT, K_RIGHT, K_SPACE
from pygame import Color, Vector2
from src.constants import BLACK, WHITE

class Game:
    entities: "list"

    def __init__(self):
        self.entities = []

    def handle_input(self, events):
        for event in events:
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    print("move left")
                if event.key == K_RIGHT:
                    print("move right")
                if event.key == K_SPACE:
                    print("shoot")
            if event.type == KEYUP:
                if event.key == K_LEFT:
                    print("stop move left")
                if event.key == K_RIGHT:
                    print("stop move right")

    def update(self, delta):
        for i in range(len(self.entities) - 1, -1, -1):
            # execute entity logic
            obj = self.entities[i]

    def render_text(self, display, font, text: str, color: Color, position: Vector2):
        surface = font.render(text, True, color)
        display.blit(surface, position)

    def render(self, display, font):
        # loop through each entity and render it
        display.fill(BLACK)
        self.render_text(display, font, "Space Invaders", WHITE, (50,50))