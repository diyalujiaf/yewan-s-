import pygame
class card:
    def __init__(self,img):
        self.img = pygame.image.load(img)
        self.card_size = (120,80)
