import pygame
import time
import random

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
blue = (0,0,255)
green = (0,155,0)
grey = (155, 155, 155)

display_width = 600
display_height = 800

gameDisplay = pygame.display.set_mode((display_height,display_width))
pygame.display.set_caption('Slither') 


clock = pygame.time.Clock()
block_size = 20
FPS = 15


font = pygame.font.SysFont(None, 25)

def snake(block_size,snakelist):
    for XnY in snakelist:
        pygame.draw.rect (gameDisplay, green, [XnY[0],XnY[1],block_size,block_size])
    
def message_to_screen (msg, color):
    screen_text = font.render (msg, True, color)
    gameDisplay.blit(screen_text, [display_height/2, display_width/2])


def gameLoop():
    gameExit = False
    gameOver =False

    snakeList = []
    snakeLength = 1
           
    lead_x = display_width/2    
    lead_y = display_height/2
    
    lead_x_change = 0
    lead_y_change = 0

    randAppleX = round(random.randrange(0, display_height-block_size)) #/10.0)*10.0
    randAppleY = round(random.randrange(0, display_width-block_size)) #/10.0)*10.0
    
    while not gameExit:

#GameOver
        while gameOver == True:
            gameDisplay.fill(white)
            message_to_screen("You've lost! Press C to play again or Q to quit.", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    gameOver = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False

                    if event.key == pygame.K_c:
                        gameLoop()
        #controls                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event. key == pygame.K_LEFT:
                    lead_x_change = -block_size
                    lead_y_change = 0
                if event.key == pygame.K_RIGHT:
                    lead_x_change = block_size
                    lead_y_change = 0
                if event.key == pygame.K_UP:
                    lead_y_change = -block_size
                    lead_x_change = 0
                if event.key == pygame.K_DOWN:
                    lead_y_change = block_size
                    lead_x_change = 0
                    
        lead_y += lead_y_change           
        lead_x += lead_x_change

        if lead_y >= display_width or lead_y < 0 or lead_x >= display_height or lead_x < 0:
                gameOver = True

             
        gameDisplay.fill(grey)

        AppleThickness = 30
        pygame.draw.rect (gameDisplay, red, [randAppleX, randAppleY, AppleThickness, AppleThickness])

        
        snakeHead = []
        snakeHead.append (lead_x)
        snakeHead.append (lead_y)
        snakeList.append (snakeHead)
        
        if len(snakeList) > snakeLength:
            del snakeList [0]
            
        for eachSegment in snakeList [:-1]:
            if eachSegment == snakeHead:
                gameOver = True
        
        
        
        snake(block_size, snakeList)

        
        
        pygame.display.update()
        


        if lead_x >= randAppleX and lead_x <= randAppleX + AppleThickness:
           if lead_y >= randAppleY and lead_y <= randAppleY + AppleThickness:
                randAppleX = round(random.randrange(0,display_height-block_size))#/10.0)*10.0
                randAppleY = round(random.randrange(0,display_width-block_size))#/10.0)*10.0
                snakeLength += 1

        if lead_x > randAppleX and lead_x < randAppleX + AppleThickness or lead_x + block_size > randAppleX and lead_x + block_size + AppleThickness:
            print ("x crossover")
        if lead_y > randAppleY and lead_y  < randAppleY + AppleThickness:
            print (" x and y crossover" )



        clock.tick(FPS)
        
        
        

    pygame.quit()
    quit()

gameLoop()

