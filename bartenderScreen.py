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
drinkTilePositions=[[30,30],[190,30],[350,30],[30,160],[190,160],[350,160]]
letsDrinkPic = pygame.image.load(r'LetsDrink.png') 
homeButtonPic = pygame.image.load(r'home.png') 
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

    elif(screen=="Drinks"):
        #click test for touch points on the drink selection page
        if(mousePOS[0]>=210 and mousePOS[0]<=250):
            if(mousePOS[1]>=270 and mousePOS[1]<=310):
                return "HomeButton"
        #click test for the 6 drink buttons
        if(mousePOS[0]>=30 and mousePOS[0]<=130):
            if(mousePOS[1]>=30 and mousePOS[1]<=130):
                return "drink1"
        if(mousePOS[0]>=190 and mousePOS[0]<=290):
            if(mousePOS[1]>=30 and mousePOS[1]<=130):
                return "drink2"
        if(mousePOS[0]>=350 and mousePOS[0]<=450):
            if(mousePOS[1]>=30 and mousePOS[1]<=130):
                return "drink3"
        if(mousePOS[0]>=30 and mousePOS[0]<=130):
            if(mousePOS[1]>=160 and mousePOS[1]<=260):
                return "drink4"
        if(mousePOS[0]>=190 and mousePOS[0]<=290):
            if(mousePOS[1]>=160 and mousePOS[1]<=260):
                return "drink5"
        if(mousePOS[0]>=350 and mousePOS[0]<=450):
            if(mousePOS[1]>=160 and mousePOS[1]<=260):
                return "drink6"
    return "Empty Space -_-"

def drawDrinkSelection(availableDrinks):
    #For each drink in the dictionary draws a box using the coordinates stored in
    #the drinkTilePositions list
    screen.fill(bgColor)
    drawRectangle(red,230,280,20,20,"")
    screen.blit(homeButtonPic, (225, 280)) 
    for i in range(len(availableDrinks)):
        drawRectangle(red,drinkTilePositions[i][0],drinkTilePositions[i][1],100,100,"test")

    pygame.display.update()    

#Generic function used to draw rectangles as needed
def drawRectangle(color,positionalWidth,positionalHeight,width,height,txt):
    values=[positionalWidth,positionalHeight,width,height]
    pygame.draw.rect(screen,color,values)
    
#Calls drinkDict.py to return dictionary of drink names as key and a tuple of time as the value
def generateAvailableDrinks():
    drinkDictionary=drinkDict.main()
    return drinkDictionary

#Main controlling function for the GUI
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
                tempPrint= "Clicked= " + str(clicked)
                print(tempPrint)

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
