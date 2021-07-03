import pygame

#Initializes PyGame 
pygame.init()

#Creates a window for game
win = pygame.display.set_mode((550,550))

#Sets the title of window
pygame.display.set_caption('PyGame Tic-Tac-Toe')

#Draws the game board
first = pygame.draw.rect(win, (255,255,255), (25,25,150,150))
second = pygame.draw.rect(win, (255,255,255), (200,25,150,150))
third = pygame.draw.rect(win, (255,255,255), (375,25,150,150))
fourth = pygame.draw.rect(win, (255,255,255), (25,200,150,150))
fifth = pygame.draw.rect(win, (255,255,255), (200,200,150,150))
sixth = pygame.draw.rect(win, (255,255,255), (375,200,150,150))
seventh = pygame.draw.rect(win, (255,255,255), (25,375,150,150))
eighth = pygame.draw.rect(win, (255,255,255), (200,375,150,150))
ninth = pygame.draw.rect(win, (255,255,255), (375,375,150,150))


#Sets first player's shape
draw_object = 'circle'

#Used to see if space is taken
first_open = True
second_open = True
third_open = True
fourth_open = True
fifth_open = True
sixth_open = True
seventh_open = True
eighth_open = True
ninth_open = True

#Main Loop
run = True
while run:

    #Refresh Time
    pygame.time.delay(100)
   

    #Pygame Events
    for event in pygame.event.get():

        #Quit Event
        if event.type == pygame.QUIT:
            run = False

        #Space bar to reset
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                first_open = True
                second_open = True
                third_open = True
                fourth_open = True
                fifth_open = True
                sixth_open = True
                seventh_open = True
                eighth_open = True
                ninth_open = True
                run = True
                #pygame.draw.rect(surface, (color), (startx,starty,length width))
                first = pygame.draw.rect(win, (255,255,255), (25,25,150,150))
                second = pygame.draw.rect(win, (255,255,255), (200,25,150,150))
                third = pygame.draw.rect(win, (255,255,255), (375,25,150,150))
                fourth = pygame.draw.rect(win, (255,255,255), (25,200,150,150))
                fifth = pygame.draw.rect(win, (255,255,255), (200,200,150,150))
                sixth = pygame.draw.rect(win, (255,255,255), (375,200,150,150))
                seventh = pygame.draw.rect(win, (255,255,255), (25,375,150,150))
                eighth = pygame.draw.rect(win, (255,255,255), (200,375,150,150))
                ninth = pygame.draw.rect(win, (255,255,255), (375,375,150,150))

        #Used to see which space is clicked
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()

            #Checks if mouse position is in a space and if space is available
            if first.collidepoint(pos) and first_open:
                #Draws a shapes based on whose turn it is
                if draw_object == 'circle':
                    #pygame.draw.circle(surface, (color), (centerx, centery),radius)
                    pygame.draw.circle(win,(255,0,0), (100,100),50)
                    draw_object = 'rect'
                else:
                    pygame.draw.rect(win,(0,255,0), (50,50,100, 100))
                    draw_object = 'circle'
                #Marks this space as taken
                first_open = False
                    
            if second.collidepoint(pos) and second_open:
                if draw_object == 'circle':
                    pygame.draw.circle(win,(255,0,0), (275,100),50)
                    draw_object = 'rect'
                else:
                    pygame.draw.rect(win,(0,255,0), (225,50,100, 100))
                    draw_object = 'circle'
                second_open = False
                    
            if third.collidepoint(pos) and third_open:
                if draw_object == 'circle':
                    pygame.draw.circle(win,(255,0,0), (450,100),50)
                    draw_object = 'rect'
                else:
                    pygame.draw.rect(win,(0,255,0), (400,50,100, 100))
                    draw_object = 'circle'
                third_open = False
                    
            if fourth.collidepoint(pos) and fourth_open:
                if draw_object == 'circle':
                    pygame.draw.circle(win,(255,0,0), (100,275),50)
                    draw_object = 'rect'
                else:
                    pygame.draw.rect(win,(0,255,0), (50,225,100, 100))
                    draw_object = 'circle'
                fourth_open = False
                    
            if fifth.collidepoint(pos) and fifth_open:
                if draw_object == 'circle':
                    pygame.draw.circle(win,(255,0,0), (275,275),50)
                    draw_object = 'rect'
                else:
                    pygame.draw.rect(win,(0,255,0), (225,225,100, 100))
                    draw_object = 'circle'
                fifth_open = False
                    
            if sixth.collidepoint(pos) and sixth_open:
                if draw_object == 'circle':
                    pygame.draw.circle(win,(255,0,0), (450,275),50)
                    draw_object = 'rect'
                else:
                    pygame.draw.rect(win,(0,255,0), (400,225,100, 100))
                    draw_object = 'circle'
                sixth_open = False
                    
            if seventh.collidepoint(pos) and seventh_open:
                if draw_object == 'circle':
                    pygame.draw.circle(win,(255,0,0), (100,450),50)
                    draw_object = 'rect'
                else:
                    pygame.draw.rect(win,(0,255,0), (50,400,100, 100))
                    draw_object = 'circle'
                seventh_open = False
                    
            if eighth.collidepoint(pos) and eighth_open:
                if draw_object == 'circle':
                    pygame.draw.circle(win,(255,0,0), (275,450),50)
                    draw_object = 'rect'
                else:
                    pygame.draw.rect(win,(0,255,0), (225,400,100, 100))
                    draw_object = 'circle'
                eighth_open = False
                    
            if ninth.collidepoint(pos) and ninth_open:
                if draw_object == 'circle':
                    pygame.draw.circle(win,(255,0,0), (450,450),50)
                    draw_object = 'rect'
                else:
                    pygame.draw.rect(win,(0,255,0), (400,400,100, 100))
                    draw_object = 'circle'
                ninth_open = False

    #Updates screen with new shapes
    pygame.display.update()


#Closes game once loop is broken
pygame.quit()
