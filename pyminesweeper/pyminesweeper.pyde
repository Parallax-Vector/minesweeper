#Minesweeper isn't my idea... :)
from menu import *
from board import Board
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 600
MARGIN = 10
MARGIN_COLOR = color(20)
BACKGROUND_COLOR = color(51)

DISPLAY_MM = True #Display main menu                                          |PLAY OSM PSM QUIT                                      
DISPLAY_OSM = False #Display options sub-menu                                 |BACK GRAPHICS SOUND
DISPLAY_GSM = False #Display graphics options sub-menu                        |BACK FULLSCREEN
DISPLAY_SSM = False #Display sound options sub-menu                           |BACK MUTE
DISPLAY_CSM = False #Display colour sub-menu (colour settings etc)            |BACK COLOUR
SETUP_LEVEL = False #Level generation call                                    |
DISPLAY_LEVEL = False #Display the board - called by level generation function|
DISPLAY_PM = False #Display pause menu                                        |CONTINUE QUIT
DISPLAY_LM = False #Display lose menu                                         |MAIN MENU  TRY AGAIN
DISPLAY_WM = False #Display win menu                                          |MAIN MENU  PLAY AGAIN  NEXT LEVEL

#LEVEL VARS
global board
NUMBER_OF_MINES = 10
COLUMNS = 10
ROWS = 10

#DEFINING THE MENUS
def setupMM():
    MM = Menu()
    MM.setDimensions(0,0) #top left corner. This is default but shown for clear reading
    def level(): 
        global DISPLAY_MM; global DISPLAY_LEVEL; DISPLAY_MM = False; DISPLAY_LEVEL = True
        global DISPLAY_WM; global DISPLAY_LM; global DISPLAY_PM;
        DISPLAY_WM = False; DISPLAY_LM = False; DISPLAY_PM = False
        global board; board.generate(COLUMNS,ROWS,NUMBER_OF_MINES)
    def options(): 
        global DISPLAY_MM; global DISPLAY_OSM; DISPLAY_MM = False; DISPLAY_OSM = True
    def colour(): 
        global DISPLAY_MM; global DISPLAY_CSM; DISPLAY_MM = False; DISPLAY_CSM = True
    def quit(): exit()
    MM.addButton(width/2-120,height*0.6,110,50,"Play",level)
    MM.addButton(width/2+20,height*0.6,110,50,"Quit",quit)
    MM.addButton(width/2-120,height*0.8,110,50,"Options",options)
    MM.addButton(width/2+20,height*0.8,110,50,"Colour!",colour)
    MM.addCaption(width/2-500,height*0.2,1000,200,"MINESWEEPER")
    return MM

def setupOSM():
    OSM = Menu()
    OSM.setDimensions(0,0) #top left corner. This is default but shown for clear reading
    def back(): 
        global DISPLAY_OSM; global DISPLAY_MM; DISPLAY_OSM = False; DISPLAY_MM = True
    def graphics(): 
        global DISPLAY_OSM; global DISPLAY_GSM; DISPLAY_OSM = False; DISPLAY_GSM = True
    def sound(): 
        global DISPLAY_OSM; global DISPLAY_SSM; DISPLAY_OSM = False; DISPLAY_SSM = True
    OSM.addButton(width/2-120,height*0.6,110,50,"Back",back)
    OSM.addButton(width/2+20,height*0.6,110,50,"Graphics",graphics)
    OSM.addButton(width/2-120,height*0.8,110,50,"Sound",sound)
    return OSM

def setupSSM():
    SSM = Menu()
    SSM.setDimensions(0,0) #top left corner. This is default but shown for clear reading
    def back(): 
        global DISPLAY_SSM; global DISPLAY_OSM; DISPLAY_SSM = False; DISPLAY_OSM = True
    def mute(): 
        return
    SSM.addButton(width/2-120,height*0.6,110,50,"Back",back)
    SSM.addButton(width/2+20,height*0.6,110,50,"Mute",mute)
    return SSM

def setupGSM():
    GSM = Menu()
    GSM.setDimensions(0,0) #top left corner. This is default but shown for clear reading
    def back(): 
        global DISPLAY_GSM; global DISPLAY_OSM; DISPLAY_GSM = False; DISPLAY_OSM = True
    def fs(): 
        return
    GSM.addButton(width/2-120,height*0.6,110,50,"Back",back)
    GSM.addButton(width/2+20,height*0.6,110,50,"Fullscreen",fs)
    return GSM

def setupCSM():
    CSM = Menu()
    CSM.setDimensions(0,0) #top left corner. This is default but shown for clear reading
    def back(): 
        global DISPLAY_CSM; global DISPLAY_MM; DISPLAY_CSM = False; DISPLAY_MM = True
    def graphics(): 
        global DISPLAY_CSM; global DISPLAY_GSM; DISPLAY_CSM = False; DISPLAY_GSM = True
    def sound(): 
        global DISPLAY_CSM; global DISPLAY_SSM; DISPLAY_CSM = False; DISPLAY_SSM = True
    CSM.addButton(width/2-120,height*0.6,110,50,"Back",back)
    CSM.addButton(width/2+20,height*0.6,110,50,"Graphics",graphics)
    CSM.addButton(width/2-120,height*0.8,110,50,"Sound",sound)
    return CSM

def setupPM():
    PM = Menu()
    PM.setDimensions(0,0) #top left corner. This is default but shown for clear reading
    def mainmenu(): 
        global DISPLAY_PM; global DISPLAY_MM; global DISPLAY_LEVEL;
        DISPLAY_PM = False; DISPLAY_MM = True; DISPLAY_LEVEL = False
    def resume(): 
        global DISPLAY_PM; DISPLAY_PM = False;
    PM.addButton(width/2-120,height*0.6,110,50,"Main Menu",mainmenu)
    PM.addButton(width/2+20,height*0.6,110,50,"Resume",resume)
    return PM

def setupLM():
    LM = Menu()
    LM.setDimensions(0,0) #top left corner. This is default but shown for clear reading
    def mainmenu(): 
        global DISPLAY_LM; global DISPLAY_MM; global DISPLAY_LEVEL;
        DISPLAY_LM = False; DISPLAY_MM = True; DISPLAY_LEVEL = False
    def restart(): 
        global DISPLAY_LM; global DISPLAY_LEVEL; 
        DISPLAY_LEVEL = True; DISPLAY_LM = False
        global board; board.generate(COLUMNS, ROWS, NUMBER_OF_MINES)
    LM.addButton(width/2-140,height*0.6,130,50,"Main Menu",mainmenu)
    LM.addButton(width/2+20,height*0.6,130,50,"Try Again",restart)
    LM.addCaption(width/2-140,height*0.4,280,80,"You lost")
    return LM

def setupWM():
    WM = Menu()
    WM.setDimensions(0,0) #top left corner. This is default but shown for clear reading
    def mainmenu(): 
        global DISPLAY_WM; global DISPLAY_MM; global DISPLAY_LEVEL
        DISPLAY_WM = False; DISPLAY_MM = True; DISPLAY_LEVEL = False
    def restart(): 
        global DISPLAY_WM; DISPLAY_WM = False; global DISPLAY_LEVEL; DISPLAY_LEVEL = True
        global board; board.generate(COLUMNS, ROWS, NUMBER_OF_MINES)
    WM.addButton(width/2-140,height*0.6,130,50,"Main Menu",mainmenu)
    WM.addButton(width/2+20,height*0.6,130,50,"Try Again",restart)
    WM.addCaption(width/2-140,height*0.4,280,80,"You won!")
    return WM

def setup():
    global board; global MM; global OSM; global GSM; global SSM; global CSM; global PM; global LM; global WM
    size(WINDOW_WIDTH,WINDOW_HEIGHT)
    #fullScreen(P2D)
    MM = setupMM()
    OSM = setupOSM()
    GSM = setupGSM()
    SSM = setupSSM()
    CSM = setupCSM()
    PM = setupPM()
    LM = setupLM()
    WM = setupWM()
    board = Board(MARGIN,MARGIN,width-MARGIN*2,height-MARGIN*2)
    textAlign(CENTER,CENTER)
    frameRate(60)
    return

def draw():
    noStroke();
    background(BACKGROUND_COLOR)
    #Draw margins
    fill(MARGIN_COLOR)
    rect(0,0,MARGIN,height)
    rect(width-MARGIN,0,MARGIN,height)
    rect(MARGIN,0,width-MARGIN,MARGIN)
    rect(MARGIN,height-MARGIN,width-MARGIN,MARGIN)
    if DISPLAY_MM:
        MM.display() #display main menu
    elif DISPLAY_OSM:
        OSM.display()
    elif DISPLAY_GSM:
        GSM.display()
    elif DISPLAY_SSM:
        SSM.display()
    elif DISPLAY_CSM:
        CSM.display()
    elif DISPLAY_LEVEL:
        board.display()
        if DISPLAY_PM:
            PM.display()
        elif DISPLAY_WM:
            WM.display()
        elif DISPLAY_LM:
            LM.display()
    return

def mouseClicked():
    global DISPLAY_WM; global DISPLAY_LM; global DISPLAY_PM;
    if DISPLAY_MM:
        #check if a button was clicked on main menu
        MM.checkClick(mouseX, mouseY)
    elif DISPLAY_OSM:
        OSM.checkClick(mouseX, mouseY)
    elif DISPLAY_GSM:
        GSM.checkClick(mouseX, mouseY)
    elif DISPLAY_SSM:
        SSM.checkClick(mouseX, mouseY)
    elif DISPLAY_CSM:
        CSM.checkClick(mouseX, mouseY)
    elif DISPLAY_LEVEL:
        if DISPLAY_PM:
            PM.display()
        elif DISPLAY_WM:
            WM.checkClick(mouseX, mouseY)
        elif DISPLAY_LM:
            LM.checkClick(mouseX, mouseY)
        else:
            cellx, celly = board.checkClick(mouseX, mouseY)
            if cellx != None and celly != None:
                if cellx == 'mine' and celly == 'mine': 
                    DISPLAY_LM = True
                    return
                else:
                    board.revealFrom(cellx, celly)
            if board.checkWin(): 
                board.revealAll()
                print('You won!')
                DISPLAY_WM = True
        