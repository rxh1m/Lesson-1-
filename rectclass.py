import pygame

WIDTH = 600
HEIGHT = 900

screen = pygame.display.set_mode((WIDTH,HEIGHT))

class Rect():
    def __init__(self,x,y,w,h, color):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
    def display(self):
        pygame.draw.rect(screen,self.color,(self.x, self.y, self.w, self.h))

#object of the class
r1 = Rect(300,300,200,50,"yellow")
r2 = Rect(100,200,200,50,"lime")

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.QUIT()
    screen.fill("sky blue")
    r1.display()
    r2.display()
    pygame.display.update()