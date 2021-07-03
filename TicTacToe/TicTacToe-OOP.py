import pygame

pygame.init()

win = pygame.display.set_mode((550, 550))

pygame.display.set_caption('Tic Tac Toe')

white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

class Tile(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([150, 150])
        self.image.fill(white)
        self.rect = self.image.get_rect()
    
tile_list = pygame.sprite.Group()
taken_list = pygame.sprite.Group()
    
for row in range(3):
    for column in range(3):
        tile = Tile()
        tile.rect.x = 25 + 175 * row
        tile.rect.y = 25 + 175 * column
        tile_list.add(tile)
tile_list.draw(win)
    
def redraw():
    pygame.display.update()
    
draw_object = 'rect'

run = True

while run:
    
    pygame.time.delay(100)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                tile_list.draw(win)
                taken_list = pygame.sprite.Group()
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            for i in tile_list:
                if i.rect.collidepoint(pos) and i not in taken_list:
                    taken_list.add(i)
                    if draw_object == 'rect':
                        pygame.draw.rect(win, red, (i.rect.x + 25, i.rect.y + 25, 100, 100))
                        draw_object = 'circle'
                    else:
                        pygame.draw.circle(win, green, (i.rect.x + 75, i.rect.y + 75), 50)
                        draw_object = 'rect'
    redraw()

pygame.quit()
