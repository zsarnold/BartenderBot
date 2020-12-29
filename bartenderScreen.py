import pygame
import time
import random
 
pygame.init()
 
screenW = 480
screenH = 320
bgColor=(230,235,230)
green=(140,245,152)
screen = pygame.display.set_mode((screenW,screenH))
pygame.display.set_caption('Bartender Bot')
screen.fill(bgColor)
letsDrinkPic = pygame.image.load(r'C:\Users\Randy\BartenderBot\Files\LetsDrink.png') 
pygame.display.update()
clock = pygame.time.Clock()

#Resets the screen to display the lets drink button
def drawHome():
    screen.fill(bgColor)
    letsDrinkSize=[screenW/4,screenH/4,screenW/2,screenH/2]
    pygame.draw.rect(screen,green,letsDrinkSize)
    screen.blit(letsDrinkPic, (120, 60)) 
    pygame.display.update()

def letsDrinkClicked(mousePOS):
    if(mousePOS[0]>=120 and mousePOS[0]<=360):
        if(mousePOS[1]>=85 and mousePOS[1]<=240):
            return True
        else:
            return False
    else:
        return False

def drawDrinkSelection():
    screen.fill(bgColor)
    pygame.display.update()

#Generic function used to draw rectangles as needed
def drawRectangle():
    pass
    
def main():
    homescreen = True
    currentScreen = None

    print("Main started")
    #Start variable and loop keeps event checking going for game control
    start = True
    while start: 

        #Resets to the homescreen "lets drink" button
        if(homescreen==True):
            drawHome()
            homescreen=False
            currentScreen = "Home"

        #Events tells script where the mouse is and when a click/quit happens
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            #All clickable sub actions will be checked under this elif
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print("Click Detected")

                mousePOS = pygame.mouse.get_pos()
                clicked=letsDrinkClicked(mousePOS)

                #Checked for lets drink button click
                if(currentScreen=="Home" and clicked==True):
                    print("lets drinks clicked")
                    drawDrinkSelection()
                    currentScreen="Drinks"

            else:
                pass
            #Game runs at 5 frames per second
            clock.tick(5)

if __name__ == "__main__":
    main()
