import pygame

WIDTH = 600
HEIGHT = 900

screen = pygame.display.set_mode((WIDTH,HEIGHT))

class Circle():
    def __init__(self,x,y,r, color):
        self.x = x
        self.y = y
        self.r = r
        self.color = color
    def display(self):
        pygame.draw.circle(screen,self.color,(self.x, self.y),self.r)

#object of the class
c1 = Circle(100,200,50,"white")
c2 = Circle(200,400,50,"blue")
c3 = Circle(50,100,50,"yellow")
c4 = Circle(400,800,50,"dark green")
c5 = Circle(200,800,50,"red")

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.QUIT()
    screen.fill("sky blue")
    c1.display()
    c2.display()
    c3.display()
    c4.display()
    c5.display()
    pygame.display.update()