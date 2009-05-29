import pygame, sys, os, time, gtk
from pygame.locals import *

pygame.init()

window = pygame.display.set_mode((600,400))

screen = pygame.display.get_surface()

font = pygame.font.Font(None,36)
text = font.render("Hello", True, (10,10,10))
textRect = text.get_rect()

# while True:

#     for event in pygame.event.get():
#         print event

#         if event.type == QUIT:
#             sys.exit()

#         elif event.type == KEYDOWN:
#             sys.exit()

screen.fill((250, 250, 250))

screen.blit(text, textRect)

pygame.display.flip()

textRect.move_ip([1,1])

time.sleep(0.1)

gtk.main()



