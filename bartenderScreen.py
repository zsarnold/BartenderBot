import pygame
import time
import random
import drinkDict
 
pygame.init()
 
screenW = 480
screenH = 320
bgColor=(230,235,230)
green=(140,245,152)
red=(255,0,0)
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

def whatsClicked(mousePOS,screen):
    if(screen=="Home"):
        #click test for lets drink button
        if(mousePOS[0]>=120 and mousePOS[0]<=360):
            if(mousePOS[1]>=85 and mousePOS[1]<=240):
                return "Lets Drink"
            else:
                return False
        else:
            return False
    elif(screen=="Drinks"):
        #click test for lets drink button
        if(mousePOS[0]>=220 and mousePOS[0]<=240):
            if(mousePOS[1]>=280 and mousePOS[1]<=300):
                return "HomeButton"
            else:
                return False
        else:
            return False

def drawDrinkSelection(availableDrinks):
    screen.fill(bgColor)
    drawRectangle(red,220,280,20,20)
    pygame.display.update()
    for i in availableDrinks:
        print(i)
        print(availableDrinks[i])

#Generic function used to draw rectangles as needed
def drawRectangle(color,positionalWidth,positionalHeight,width,height):
    values=[positionalWidth,positionalHeight,width,height]
    pygame.draw.rect(screen,color,values)
    
def generateAvailableDrinks():
    drinkDictionary=drinkDict.main()
    return drinkDictionary

def main():
    availableDrinks=generateAvailableDrinks()
    print(availableDrinks)
    homescreen = True
    drinksScreen = False
    currentScreen = "Lets Drink"

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
                clicked=whatsClicked(mousePOS,currentScreen)
                print(currentScreen)
                print("Clicked=" + clicked)

                #Checked for lets drink button click
                if(currentScreen=="Home" and clicked=="Lets Drink"):
                    print("lets drinks clicked")
                    drawDrinkSelection(availableDrinks)
                    currentScreen="Drinks"
                
                if(currentScreen!="Home" and clicked=="HomeButton"):
                    print("Home Button Pressed")
                    drawDrinkSelection(availableDrinks)
                    currentScreen="Drinks"

            else:
                pass
            #Game runs at 5 frames per second
            clock.tick(5)

if __name__ == "__main__":
    main()
