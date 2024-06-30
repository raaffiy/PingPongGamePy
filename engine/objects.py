# engine/objects.py

import numpy as np
import pygame

class Paddle:
    def __init__(self, position):
        self.position = np.array(position, dtype=float)
        self.velocity = np.zeros(2)
        self.speed = 5
        self.rect = pygame.Rect(self.position[0], self.position[1], 10, 60)

    def move_up(self):
        self.velocity[1] = -self.speed

    def move_down(self):
        self.velocity[1] = self.speed

    def update(self):
        # Update posisi berdasarkan kecepatan
        self.position += self.velocity
        # Batas atas dan bawah
        if self.position[1] < 80:
            self.position[1] = 80
        elif self.position[1] > 440:
            self.position[1] = 440
        self.rect.topleft = self.position
        self.velocity[1] = 0

class Ball:
    def __init__(self, position):
        self.position = np.array(position, dtype=float)
        self.velocity = np.array([5, 5], dtype=float)
        self.rect = pygame.Rect(self.position[0], self.position[1], 30, 30)

    def update(self):
        # Update posisi berdasarkan kecepatan
        self.position += self.velocity
        self.rect.topleft = self.position

    def reset_position(self):
        self.position = np.array([400, 300], dtype=float)
        self.velocity = np.array([5, 5], dtype=float)
        self.rect.topleft = self.position
