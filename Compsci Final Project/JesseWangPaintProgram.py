#Halo Paint
#Jesse Wang
#A paint program with a Halo theme
#Special Thanks to Aaron Taylor, Mustafa Abumieez, Christopher Gregorian and Mr. Mckenzie

from pygame import*
from random import*
from math import*
import os

font.init()
statusFont = font.SysFont("Verdana", 14)
textFont = font.SysFont("Candara", 30)
def fontQuit (): #Fixes an error that says "module has no attribute "quit" "
    font.quit()  #caused by "from tkinter import"

from tkinter import *
from tkinter.filedialog import askopenfilename 
from tkinter.filedialog import asksaveasfilename 

root = Tk() 
root.withdraw()

os.environ['SDL_VIDEO_WINDOW_POS'] = '25,50' #Opens up in the upper left corner 
screen = display.set_mode((1024,768)) #4:3 aspect ratio
display.set_caption("HALO Paint")
mouse.set_cursor(*cursors.tri_left) 

#Constants for these colours, helps to visualize the code
BLACK = (0,0,0)
WHITE = (255,255,255) 

#Loading Screen
loadingPic = image.load ("Loading.jpg")
screen.blit(loadingPic, (0,0))
display.flip()
    
#Setup
colour = BLACK #default 
currentTool = "Pencil" #default
drawStampStatus = 0 #default no stamp chosen
frameApplied = False #default for applying frames
thickness = 1 #default
thicknessThin = True #default 
thicknessMed = False
thicknessThick = False 
fillStatus = True #Filled shapes or not
flipped = False #For flipping stamps, default 
snapStatus = False #default
snapSize = "" #Not active yet since snap is not turned on.

pencilTrail = [] #For pencil's trail of points

polyTrail = [] #Stores the pts for the polygon tool 
endpointX = [] #Stores the X-coord of the pts to be joined
endpointY = [] #Stores the Y-coord of the pts to be joined

lx,ly = mouse.get_pos() #For brush and eraser

fillList = [] #Stores the coordinates of the pixels to be filled

textToolText = "" #default

#Uses the winding function for its angle measurements
#Defaults for drawing arcs 
arcAngleStart = 0 
arcAngleEnd = pi/2

lineStart = 0,0

clicked = False 

songPlaylist = ["Halo4.mp3","Mjolnir.mp3","Reach.mp3","Wandering.mp3","Winter.mp3"]
playlistCounter = 0 #Keeps track of the songs being played
init() #Initialize the mixer
mixer.music.load(songPlaylist[playlistCounter])  
mixer.music.play() #This fixes a bug where the music won't
                   #play even when clicked.
mixer.music.pause()
pauseStatus = True #A flag that keeps track of whether or not the button plays or
                   #pauses a song. See the music player for more details.

#Background
pic = image.load ("background.jpg")
screen.blit(pic, (-150,0))

#Canvas
draw.rect(screen,WHITE,[208,25,800,600]) #Canvas of 800x600
canvas = Rect(208,25,800,600)
oldCanvas = screen.subsurface(canvas).copy()

undoRedoCanvas = screen.subsurface(canvas).copy()
undoList1 = [undoRedoCanvas] #Stores the the drawn stuff
undoList2 = [] #Keeps the stuff when the undo button is clicked
#clickedOnCanvas = False #Determines whether or not the mouse is on the canvas for the undo redo blit copy of the canvas.
                        #Eg. when you hold hold and drag off the canvas, it still blits a copy into the list.

#Logo
logo = image.load("Logo.jpg")
logo = transform.scale(logo,(180,100))
screen.blit(logo, (9,25))
easterEggRect = Rect(9,25,180,100) #Hidden feature when clicked

#Palette
palettePic = image.load("colour_palette.jpg")
palettePic = transform.scale(palettePic,(160,114)) 
palette = Rect (19,635,160,114)
#Border around palette changes to the selected colour.
#Basically the palette picture is drawn on top of a rectangle, it gives
#the appearance of a border that changes to match the selected colour
draw.rect(screen,colour,[9,625,180,134])
screen.blit(palettePic,(19,635))

#Effects, stamps box
#Draws a white rectangle with a black border that
#hides the gaps inbetween the buttons.
draw.rect(screen,BLACK,[206,638,404,122])
draw.rect(screen,WHITE,[208,640,400,118])
draw.line(screen,BLACK,[208,670],[607,670],2)
effectsStampsBoxRect = Rect (208,640,400,30)

backgroundTab = image.load("backgroundTextIdle.jpg")
backgroundTab = transform.scale(backgroundTab,(130,26))
screen.blit(backgroundTab,(220,642))
backgroundTabRect = Rect (220,642,130,26)

effectsTab = image.load("effectsTextIdle.jpg")
effectsTab = transform.scale(effectsTab,(65,22))
screen.blit(effectsTab,(360,645))
effectsTabRect = Rect (360,645,65,22)

stampsTab = image.load("stampsTextIdle.jpg")
stampsTab = transform.scale(stampsTab,(65,22))
screen.blit(stampsTab,(440,646))
stampsTabRect = Rect (440,646,65,22)

optionsTab = image.load("optionsTextIdle.jpg")
optionsTab = transform.scale(optionsTab,(65,25))
screen.blit(optionsTab,(515,645))
optionsTabRect = Rect (515,645,65,25)

#Music player, status box
#Draws a white rectangle with a black border that
#hides the gaps inbetween the buttons.
#The rest of the box is inside the loop since text and
#images are constantly being drawn on top of each other. 
draw.rect(screen,BLACK,[625,638,179,122])
statusBox = Rect(627,640,175,118)

#Save,Undo,Redo,Load box
#Draws a black rectangle that hides the gaps
#inbetween the buttons.
draw.rect(screen,BLACK,[821,638,187,122])
saveNewLoadRect = Rect (821,638,187,122)
#The buttons for this box are also inside the loop

#Tools box
#Draws a black rectangle that hides the gaps
#inbetween the tool icons.
draw.rect(screen,BLACK,[9,125,180,485])
toolbarRect = Rect (9,125,180,485)
#Below are the icons for the tools 

pencilPic = image.load("pencilIdle.png")
pencilPic = transform.scale(pencilPic,(65,50))
screen.blit(pencilPic,(29,140))
pencilRect = Rect (29,140,65,50)

eraserPic = image.load("eraserIdle.png")
eraserPic = transform.scale(eraserPic,(65,50))
screen.blit(eraserPic,(109,140))
eraserRect = Rect (109,140,65,50)

brushPic = image.load("brushIdle.png")
brushPic = transform.scale(brushPic,(65,50))
screen.blit(brushPic,(29,205))
brushRect = Rect (29,205,65,50)

sprayPic = image.load("sprayIdle.png")
sprayPic = transform.scale(sprayPic,(65,50))
screen.blit(sprayPic,(109,205))
sprayRect = Rect (109,205,65,50)

eyedropPic = image.load("eyedropIdle.png")
eyedropPic = transform.scale(eyedropPic,(65,50))
screen.blit(eyedropPic,(29,270))
eyedropRect = Rect (29,270,65,50)        

fillPic = image.load("fillIdle.png")
fillPic = transform.scale(fillPic,(65,50))
#Pointed in the same direction as all the other tools
fillPic = transform.flip(fillPic,True,False)
screen.blit(fillPic,(109,270))
fillRect = Rect (109,270,65,50)      

rectanglePic = image.load("rectangleIdle.png")
rectanglePic = transform.scale(rectanglePic,(65,50))
screen.blit(rectanglePic,(29,335))
rectangleRect = Rect (29,335,65,50)

elipsePic = image.load("elipseIdle.png")
elipsePic = transform.scale(elipsePic,(65,50))
screen.blit(elipsePic,(109,335))
elipseRect = Rect (109,335,65,50)

polygonPic = image.load("polygonIdle.png")
polygonPic = transform.scale(polygonPic,(65,50))
screen.blit(polygonPic,(29,400))
polygonRect = Rect (29,400,65,50)

linePic = image.load("lineIdle.png")
linePic = transform.scale(linePic,(65,50))
screen.blit(linePic,(109,400))
lineRect = Rect (109,400,65,50)

#Originally a layers tool, easier to leave the name unchanged.
layersPic = image.load("arcIdle.png") 
layersPic = transform.scale(layersPic,(65,60))
screen.blit(layersPic,(29,465))
layersRect = Rect (29,465,65,60)

textPic = image.load("textIdle.png")
textPic = transform.scale(textPic,(65,50))
screen.blit(textPic,(109,465))
textRect = Rect (109,465,65,50)

tilePic = image.load("tileIdle.png")
tilePic = transform.scale(tilePic,(65,50))
screen.blit(tilePic,(29,530))
tileRect = Rect (29,530,65,50)

fireworksPic = image.load("fireworksIdle.png")
fireworksPic = transform.scale(fireworksPic,(65,55))
screen.blit(fireworksPic,(109,530))
fireworksRect = Rect (109,530,65,55)

#Takes a blit of the toolbar and tabs without any highlights, used for later
#when different tools are to be highlighted/unhighlighted.
stampsToolbar = Rect(208,640,400,118) 
newStampsToolbar = screen.subsurface(stampsToolbar).copy() #Used to clear highlights in stamp tab
newToolbarRect = screen.subsurface(toolbarRect).copy()
neweffectsStampsBoxRect = screen.subsurface(effectsStampsBoxRect).copy() #Used to clear highlights in tab header

#Images to be loaded 
prevPic = image.load("prevIdle.png")
prevPic = transform.scale(prevPic,(50,50))

playPic = image.load("playIdle.jpg")
playPic = transform.scale(playPic,(50,50))

nextPic = image.load("nextIdle.png")
nextPic = transform.scale(nextPic,(50,50))

undoPic = image.load("undoIdle.png")
undoPic = transform.scale(undoPic,(70,40))

redoPic = image.load("redoIdle.png")
redoPic = transform.scale(redoPic,(70,40))

newPic = image.load("newIdle.jpg")
newPic = transform.scale(newPic,(120,25))

savePic = image.load("saveIdle.jpg")
savePic = transform.scale(savePic,(120,23))

loadPic = image.load("loadIdle.jpg")
loadPic = transform.scale(loadPic,(120,28))

pencilPicHighlight = image.load("pencilHighlight.png")
pencilPicHighlight = transform.scale(pencilPicHighlight,(65,50))

eraserPicHighlight = image.load("eraserHighlight.png")
eraserPicHighlight = transform.scale(eraserPicHighlight,(65,50))

brushPicHighlight = image.load("brushHighlight.png")
brushPicHighlight = transform.scale(brushPicHighlight,(65,50))

sprayPicHighlight = image.load("sprayHighlight.png")
sprayPicHighlight = transform.scale(sprayPicHighlight,(65,50))

eyedropPicHighlight = image.load("eyedropHighlight.png")
eyedropPicHighlight = transform.scale(eyedropPicHighlight,(65,50))

fillPicHighlight = image.load("fillHighlight.png")
fillPicHighlight = transform.scale(fillPicHighlight,(65,50))
#Pointed in the same direction as all the other tools
fillPicHighlight = transform.flip(fillPicHighlight,True,False)

rectanglePicHighlight = image.load("rectangleHighlight.png")
rectanglePicHighlight = transform.scale(rectanglePicHighlight,(65,50))

elipsePicHighlight = image.load("elipseHighlight.png")
elipsePicHighlight = transform.scale(elipsePicHighlight,(65,50))

polygonPicHighlight = image.load("polygonHighlight.png")
polygonPicHighlight = transform.scale(polygonPicHighlight,(65,50))

linePicHighlight = image.load("lineHighlight.png")
linePicHighlight = transform.scale(linePicHighlight,(65,50))

layersPicHighlight = image.load("arcHighlight.png")
layersPicHighlight = transform.scale(layersPicHighlight,(65,60))

textPicHighlight = image.load("textHighlight.png")
textPicHighlight = transform.scale(textPicHighlight,(65,50))

tilePicHighlight = image.load("tileHighlight.png")
tilePicHighlight = transform.scale(tilePicHighlight,(65,50))

fireworksPicHighlight = image.load("fireworksHighlight.png")
fireworksPicHighlight = transform.scale(fireworksPicHighlight,(65,55))

backgroundTabHighlight = image.load("backgroundTextHighlight.jpg")
backgroundTabHighlight = transform.scale(backgroundTabHighlight,(130,26))

background1 = image.load("pic1preview.jpg")
background1 = transform.scale(background1,(78,80))

background2 = image.load("pic2preview.jpg")
background2 = transform.scale(background2,(78,80))

background3 = image.load("pic3preview.jpg")
background3 = transform.scale(background3,(78,80))

background4 = image.load("pic4preview.jpg")
background4 = transform.scale(background4,(78,80))

background5 = image.load("pic5preview.jpg")
background5 = transform.scale(background5,(78,80))

effectsTabHighlight = image.load("effectsTextHighlight.jpg")
effectsTabHighlight = transform.scale(effectsTabHighlight,(65,22))

effects1 = image.load("effectPreview1.jpg")
effects1 = transform.scale(effects1,(78,80))

effects2 = image.load("effectPreview2.jpg")
effects2 = transform.scale(effects2,(78,80))

effects3 = image.load("effectPreview3.jpg")
effects3 = transform.scale(effects3,(78,80))

effects4 = image.load("effectPreview4.jpg")
effects4 = transform.scale(effects4,(78,80))

effects5 = image.load("effectPreview5.jpg")
effects5 = transform.scale(effects5,(78,80))

stampsTabHighlight = image.load("stampsTextHighlight.jpg")
stampsTabHighlight = transform.scale(stampsTabHighlight,(65,22))

stampsPreview1 = image.load("stamp1Preview.jpg")
stampsPreview1 = transform.scale(stampsPreview1,(40,40))
stampsPreview1Highlight = image.load("stamp1PreviewHighlight.jpg")
stampsPreview1Highlight = transform.scale(stampsPreview1Highlight,(40,40))

stampsPreview2 = image.load("stamp2Preview.jpg")
stampsPreview2 = transform.scale(stampsPreview2,(40,40))
stampsPreview2Highlight = image.load("stamp2PreviewHighlight.jpg")
stampsPreview2Highlight = transform.scale(stampsPreview2Highlight,(40,40))

stampsPreview3 = image.load("stamp3Preview.jpg")
stampsPreview3 = transform.scale(stampsPreview3,(80,80))
stampsPreview3Highlight = image.load("stamp3PreviewHighlight.jpg")
stampsPreview3Highlight = transform.scale(stampsPreview3Highlight,(80,80))

stampsPreview7 = image.load("stamp7Preview.jpg") #Warthog
stampsPreview7 = transform.scale(stampsPreview7,(40,40))
stampsPreview7Highlight = image.load("stamp7PreviewHighlight.jpg")
stampsPreview7Highlight = transform.scale(stampsPreview7Highlight,(40,40))

stampsPreview8 = image.load("stamp8Preview.jpg") #Ghost
stampsPreview8 = transform.scale(stampsPreview8,(40,40))
stampsPreview8Highlight = image.load("stamp8PreviewHighlight.jpg")
stampsPreview8Highlight = transform.scale(stampsPreview8Highlight,(40,40))

stampsPreview4 = image.load("stamp4Preview.jpg")
stampsPreview4 = transform.scale(stampsPreview4,(80,80))
stampsPreview4Highlight = image.load("stamp4PreviewHighlight.jpg")
stampsPreview4Highlight = transform.scale(stampsPreview4Highlight,(80,80))

stampsPreview5 = image.load("stamp5Preview.jpg")
stampsPreview5 = transform.scale(stampsPreview5,(40,40))
stampsPreview5Highlight = image.load("stamp5PreviewHighlight.jpg")
stampsPreview5Highlight = transform.scale(stampsPreview5Highlight,(40,40))

stampsPreview6 = image.load("stamp6Preview.jpg")
stampsPreview6 = transform.scale(stampsPreview6,(40,40))
stampsPreview6Highlight = image.load("stamp6PreviewHighlight.jpg")
stampsPreview6Highlight = transform.scale(stampsPreview6Highlight,(40,40))

optionsTabHighlight = image.load("optionsTextHighlight.jpg")
optionsTabHighlight = transform.scale(optionsTabHighlight,(65,25))

instructionsOption = image.load("instructionsOptions.jpg")
instructionsOption = transform.scale(instructionsOption,(70,15))

flipCanvasOption = image.load("flipCanvas.jpg")
flipCanvasOption = transform.scale(flipCanvasOption,(70,15))

rotateCanvasOption = image.load("rotateCanvas.jpg")
rotateCanvasOption = transform.scale(rotateCanvasOption,(120,16))

optionButton = image.load("optionButIdle.png")
optionButton = transform.scale(optionButton,(10,10))

optionButtonHighlight = image.load("optionButHighlight.png")
optionButtonHighlight = transform.scale(optionButtonHighlight,(10,10))

filledShapesOption = image.load("filledShapes.jpg")
filledShapesOption = transform.scale(filledShapesOption,(140,18))

thicknessOption = image.load("thickness.jpg")
thicknessOption = transform.scale(thicknessOption,(68,15))

thicknessThinOption = image.load("thin.jpg")
thicknessThinOption = transform.scale(thicknessThinOption,(28,12))

thicknessMediumOption = image.load("medium.jpg")
thicknessMediumOption = transform.scale(thicknessMediumOption,(55,12))

thicknessThickOption = image.load("thick.jpg")
thicknessThickOption = transform.scale(thicknessThickOption,(35,14))

snapOption = image.load("snapOnOff.jpg")
snapOption = transform.scale(snapOption,(90,22))

snapSmallOption = image.load("small.jpg")
snapSmallOption = transform.scale(snapSmallOption,(50,14))

snapMediumOption = image.load("medium.jpg")
snapMediumOption = transform.scale(snapMediumOption,(50,16))

snapLargeOption = image.load("large.jpg")
snapLargeOption = transform.scale(snapLargeOption,(48,16))

easterEgg = image.load("easterEgg.jpg")

pausePic = image.load("playIdle.jpg")
pausePic = transform.scale(pausePic,(50,50))

pausePic = image.load("playHighlight.jpg")
pausePic = transform.scale(pausePic,(50,50))

nextHighlightPic = image.load("nextHighlight.png")
nextHighlightPic = transform.scale(nextHighlightPic,(50,50))

nextHighlightPic = image.load("nextHighlight.png")
nextHighlightPic = transform.scale(nextHighlightPic,(50,50))

prevHighlightPic = image.load("prevHighlight.png")
prevHighlightPic = transform.scale(prevHighlightPic,(50,50))

prevHighlightPic = image.load("prevHighlight.png")
prevHighlightPic = transform.scale(prevHighlightPic,(50,50))

newHighlightPic = image.load("newHighlight.jpg")
newHighlightPic = transform.scale(newHighlightPic,(120,25))

saveHighlightPic = image.load("saveHighlight.jpg")
saveHighlightPic = transform.scale(saveHighlightPic,(120,23))

loadHighlightPic = image.load("loadHighlight.jpg")
loadHighlightPic = transform.scale(loadHighlightPic,(120,28))

undoHighlightPic = image.load("undoHighlight.png")
undoHighlightPic = transform.scale(undoHighlightPic,(70,40))

redoHighlightPic = image.load("redoHighlight.png")
redoHighlightPic = transform.scale(redoHighlightPic,(70,40))

stamp1 = image.load("stamp1.png")
stamp1 = transform.scale(stamp1,(200,200))

stamp2 = image.load("stamp2.png")
stamp2 = transform.scale(stamp2,(200,200))

stamp3 = image.load("stamp3.png")
stamp3 = transform.scale(stamp3,(300,300))

stamp4 = image.load("stamp4.png")
stamp4 = transform.scale(stamp4,(190,290))

stamp5 = image.load("stamp5.png")
stamp5 = transform.scale(stamp5,(180,330))

stamp6 = image.load("stamp6.png")
stamp6 = transform.scale(stamp6,(240,360))

stamp7 = image.load("stamp7.png")
stamp7 = transform.scale(stamp7,(450,335))

stamp8 = image.load("stamp8.png")
stamp8 = transform.scale(stamp8,(300,240))

backgroundPic1 = image.load("pic1.jpg")
backgroundPic1 = transform.scale(backgroundPic1,(800,600))

backgroundPic2 = image.load("pic2.jpg")
backgroundPic2 = transform.scale(backgroundPic2,(800,600))

backgroundPic3 = image.load("pic3.jpg")
backgroundPic3 = transform.scale(backgroundPic3,(800,600))

backgroundPic4 = image.load("pic4.jpg")
backgroundPic4 = transform.scale(backgroundPic4,(800,600))

backgroundPic5 = image.load("pic5.jpg")
backgroundPic5 = transform.scale(backgroundPic5,(800,600))

instructionsPic = image.load("instructions.jpg")
instructionsPic = transform.scale(instructionsPic,(800,600))

fancyFramePic = image.load("fancyFrame.png")
fancyFramePic = transform.scale(fancyFramePic,(800,600))

#The pencil is highlighted by default 
pencilPic = image.load("pencilHighlight.png")
pencilPic = transform.scale(pencilPic,(65,50))
screen.blit(pencilPic,(29,140))  

running = True
while running:

    mb = mouse.get_pressed()
    mx,my = mouse.get_pos()

    if snapStatus and snapSize != "" and canvas.collidepoint((mx,my)):
    #In order to activate the snap option, you must both click "On" and select a snap size.
        if snapSize == "Small":
            mx -= mx %20 #Binds the mouse coordinates to a certain threshold
            my -= my %20
        elif snapSize == "Medium":
            mx -= mx %35
            my -= my %35
        elif snapSize == "Large":
            mx -= mx %50
            my -= my %50
    
    for e in event.get():       
        if e.type == QUIT:     
            running = False
        if e.type == MOUSEBUTTONDOWN:
            #Used to hide unwanted images that are blit on screen or continuously drawn stuff
            #eg. stamps will not draw a trail if mb[0] is held down nor will the line tool create a trail when mb[0] held down.
            oldCanvas = screen.subsurface(canvas).copy()
            clicked = True #Later used for the tool selection, fixes a bug when mb[0]==1 is held down and moved around the tools would change
            if e.button == 1:
               lineStart = e.pos #The first point of the line starts at the point where clicked.
        if e.type == MOUSEBUTTONUP:
            clicked = False 
            undoRedoCanvas = screen.subsurface(canvas).copy() 
            undoList1.append(undoRedoCanvas) #When the mouse is lifted up, it takes a copy of the canvas for the undo list
        #The trail is only created while the pencil is the current tool.
        if e.type == MOUSEMOTION and mb[0]==1 and currentTool == "Pencil": 
            pencilTrail=pencilTrail+[e.pos]
        if e.type == MOUSEMOTION and mb[0]==0 and currentTool == "Pencil":
        #Prevents joining the line with the last coordinate in the trail once mb[0] is let go the list of points is emptied.
        #If the mouse is moving, but left click is not clicked, the pts in the trail are deleted so that the next time it is clicked,
        #The line starts fresh instead of joining to the last point.  
             pencilTrail=[]
        if e.type == KEYDOWN and currentTool == "Arc":
            #Use the number keys 1-4 to choose the angle of the arcs drawn by the arc tool.
            #Degree measurements in radians corresponding to the 4 quadrants on the winding function.
            if e.key == K_1:
                arcAngleStart = 0 
                arcAngleEnd = pi/2
            elif e.key == K_2:
                arcAngleStart = pi/2
                arcAngleEnd = pi
            elif e.key == K_3:
                arcAngleStart = pi 
                arcAngleEnd = 3*pi/2
            elif e.key == K_4:
                arcAngleStart = 3*pi/2 
                arcAngleEnd = 2*pi
        if e.type == KEYDOWN and currentTool == "Text":
            if e.key == K_BACKSPACE:
                #Deletes last letter, the unicode BACKSPACE draws a box with a question mark.
                endOfText = len(textToolText)
                textToolText = textToolText[0:endOfText-1] #Takes all but last chr when sliced
            else:
                #Adds whatever was typed unless backspace
                textToolText = textToolText + e.unicode
                             
    #Music player, status box (cont'd)
    #Draws a white rectangle with a black border that
    #hides the gaps inbetween the buttons.
    #This is inside the loop or else the text will be drawn on top
    #without erasing whatever was underneath it.
    draw.rect(screen,WHITE,[627,640,175,118])
    draw.line(screen,BLACK,[627,665],[802,665],2)
    draw.line(screen,BLACK,[627,695],[802,695],2)
    #Buttons for this box below

    screen.blit(prevPic,(629,705))
    prevSongRect = Rect (629,705,50,50)

    screen.blit(playPic,(689,705))
    playSongRect = Rect (689,705,50,50)

    screen.blit(nextPic,(749,705))
    nextSongRect = Rect (749,705,50,50)

    #Save,Undo,Redo,Load box (Cont'd)
    #Below are the buttons for this box
    #These are inside the loop so that the
    #buttons appear to flash when clicked
    #instead of keeping the highlighted image
    #since the idle image will be drawn on top immediatley.
    
    screen.blit(undoPic,(836,642))
    undoRect = Rect (836,642,70,40)

    screen.blit(redoPic,(916,642))
    redoRect = Rect (916,642,70,40)

    screen.blit(newPic,(868,682))
    newRect = Rect (868,682,120,25)

    screen.blit(savePic,(855,708))
    saveRect = Rect (855,708,120,23)

    screen.blit(loadPic,(854,730))
    loadRect = Rect (854,730,120,28)

    #The following is for the text that appears in the status box detailing the mouse location
    #and current tool. Tools that are obvious do not have instructions telling the user commands.
    if currentTool == "Polygon" and (mx<208 or my<25 or mx>1008 or my>625):
        posText="R. Click Closes Shape" #Tool-specific instructions
    elif currentTool == "Rect" and (mx<208 or my<25 or mx>1008 or my>625):
        posText="L. Click Then R. Click" #Tool-specific instructions
    elif currentTool == "Ellipse" and (mx<208 or my<25 or mx>1008 or my>625):
        posText="L. Click Then R. Click" #Tool-specific instructions
    elif currentTool == "Text" and (mx<208 or my<25 or mx>1008 or my>625):
        posText="L. Click, Type, R. Click" #Tool-specific instructions
    elif currentTool == "Arc" and (mx<208 or my<25 or mx>1008 or my>625):
        posText="L. Click, R. Click, 1-4" #Tool-specific instructions
    elif currentTool == "Text" and (mx<208 or my<25 or mx>1008 or my>625):
        posText="Type then L. Click" #Tool-specific instructions
    elif currentTool == "Magic" and (mx<208 or my<25 or mx>1008 or my>625):
        posText="Draws Magician Scarves" #Tool-specific instructions
    elif currentTool == "Firework" and (mx<208 or my<25 or mx>1008 or my>625):
        posText="Draws Explosions" #Tool-specific instructions
    elif mx<208 or my<25 or mx>1008 or my>625: #Outside boundaries
        posText="Mouse Not on canvas"
    else:
        pos1 = mx - 208 #Coordinates are relative to the canvas
        pos2 = my - 25
        posText = pos1,pos2
        posText = "Position: "+str(posText)

    #Displays whatever the current tool is and the mouse position in the music player widget box
    mouseLocation = statusFont.render((posText), True, BLACK)
    toolText = "Current Tool: "+currentTool 
    toolStatus = statusFont.render((toolText), True, BLACK)
    screen.blit(mouseLocation,(632,645))
    screen.blit(toolStatus,(632,670))
    
    #Below are the functions for each of the tools and how they react to being pressed.
    #The icons will highlight when they are CLICKED instead of hovered over.
    #clicked must be false, meaning that the user has to let go of the mouse in order to choose a different tool.
    if mb[0]==1 and pencilRect.collidepoint((mx,my)) and clicked == False:
        currentTool = "Pencil"
        #Clears all highlighted icons
        screen.blit(newToolbarRect,(9,125))
        screen.blit(neweffectsStampsBoxRect,(208,640))
        draw.rect(screen,WHITE,[208,675,400,82])
        #Icon turns blue to show it was clicked
        screen.blit(pencilPicHighlight,(29,140))

    elif mb[0]==1 and eraserRect.collidepoint((mx,my)) and clicked == False:
        currentTool = "Eraser"
        #Clears all highlighted icons
        screen.blit(newToolbarRect,(9,125))
        screen.blit(neweffectsStampsBoxRect,(208,640))
        draw.rect(screen,WHITE,[208,675,400,82])
        #Icon turns blue to show it was clicked
        screen.blit(eraserPicHighlight,(109,140))
        
    elif mb[0]==1 and brushRect.collidepoint((mx,my)) and clicked == False:
        currentTool = "Brush"
        #Clears all highlighted icons
        screen.blit(newToolbarRect,(9,125))
        screen.blit(neweffectsStampsBoxRect,(208,640))
        draw.rect(screen,WHITE,[208,675,400,82])
        #Icon turns blue to show it was clicked
        screen.blit(brushPicHighlight,(29,205))

    elif mb[0]==1 and sprayRect.collidepoint((mx,my)) and clicked == False:
        currentTool = "Spray"
        #Clears all highlighted icons
        screen.blit(newToolbarRect,(9,125))
        screen.blit(neweffectsStampsBoxRect,(208,640))
        draw.rect(screen,WHITE,[208,675,400,82])
        #Icon turns blue to show it was clicked
        screen.blit(sprayPicHighlight,(109,205))

    elif mb[0]==1 and eyedropRect.collidepoint((mx,my)) and clicked == False:
        currentTool = "Eyedrop"
        #Clears all highlighted icons
        screen.blit(newToolbarRect,(9,125))
        screen.blit(neweffectsStampsBoxRect,(208,640))
        draw.rect(screen,WHITE,[208,675,400,82])
        #Icon turns blue to show it was clicked
        screen.blit(eyedropPicHighlight,(29,270))
        
    elif mb[0]==1 and fillRect.collidepoint((mx,my)) and clicked == False:
        currentTool = "Fill"
        #Clears all highlighted icons
        screen.blit(newToolbarRect,(9,125))
        screen.blit(neweffectsStampsBoxRect,(208,640))
        draw.rect(screen,WHITE,[208,675,400,82])
        #Icon turns blue to show it was clicked
        screen.blit(fillPicHighlight,(109,270))

    elif mb[0]==1 and rectangleRect.collidepoint((mx,my)) and clicked == False:
        currentTool = "Rect" #"Rectangle" does not fit the space
        #Clears all highlighted icons
        screen.blit(newToolbarRect,(9,125))
        screen.blit(neweffectsStampsBoxRect,(208,640))
        draw.rect(screen,WHITE,[208,675,400,82])
        #Icon turns blue to show it was clicked
        screen.blit(rectanglePicHighlight,(29,335))

    elif mb[0]==1 and elipseRect.collidepoint((mx,my)) and clicked == False:
        currentTool = "Ellipse"
        #Clears all highlighted icons
        screen.blit(newToolbarRect,(9,125))
        screen.blit(neweffectsStampsBoxRect,(208,640))
        draw.rect(screen,WHITE,[208,675,400,82])
        #Icon turns blue to show it was clicked
        screen.blit(elipsePicHighlight,(109,335))

    elif mb[0]==1 and polygonRect.collidepoint((mx,my)) and clicked == False:
        currentTool = "Polygon"
        #Clears all highlighted icons
        screen.blit(newToolbarRect,(9,125))
        screen.blit(neweffectsStampsBoxRect,(208,640))
        draw.rect(screen,WHITE,[208,675,400,82])
        #Icon turns blue to show it was clicked
        screen.blit(polygonPicHighlight,(29,400))

    elif mb[0]==1 and lineRect.collidepoint((mx,my)) and clicked == False:
        currentTool = "Line"
        #Clears all highlighted icons
        screen.blit(newToolbarRect,(9,125))
        screen.blit(neweffectsStampsBoxRect,(208,640))
        draw.rect(screen,WHITE,[208,675,400,82])
        #Icon turns blue to show it was clicked
        screen.blit(linePicHighlight,(109,400))

    elif mb[0]==1 and layersRect.collidepoint((mx,my)) and clicked == False:
        currentTool = "Arc"
        #Clears all highlighted icons
        screen.blit(newToolbarRect,(9,125))
        screen.blit(neweffectsStampsBoxRect,(208,640))
        draw.rect(screen,WHITE,[208,675,400,82])
        #Icon turns blue to show it was clicked
        screen.blit(layersPicHighlight,(29,465))

    elif mb[0]==1 and textRect.collidepoint((mx,my)) and clicked == False:
        currentTool = "Text"
        #Clears all highlighted icons
        screen.blit(newToolbarRect,(9,125))
        screen.blit(neweffectsStampsBoxRect,(208,640))
        draw.rect(screen,WHITE,[208,675,400,82])
        #Icon turns blue to show it was clicked
        screen.blit(textPicHighlight,(109,465))

    elif mb[0]==1 and tileRect.collidepoint((mx,my)) and clicked == False:
        currentTool = "Magic"
        #Clears all highlighted icons
        screen.blit(newToolbarRect,(9,125))
        screen.blit(neweffectsStampsBoxRect,(208,640))
        draw.rect(screen,WHITE,[208,675,400,82])
        #Icon turns blue to show it was clicked
        screen.blit(tilePicHighlight,(29,530))

    elif mb[0]==1 and fireworksRect.collidepoint((mx,my)) and clicked == False:
        currentTool = "Firework"
        #Clears all highlighted icons
        screen.blit(newToolbarRect,(9,125))
        screen.blit(neweffectsStampsBoxRect,(208,640))
        draw.rect(screen,WHITE,[208,675,400,82])
        #Icon turns blue to show it was clicked
        screen.blit(fireworksPicHighlight,(109,530))

    elif mb[0]==1 and backgroundTabRect.collidepoint((mx,my)) and clicked == False:
        currentTool = "BG"
        screen.blit(newToolbarRect,(9,125)) #Clears any previous highlights
        draw.rect(screen,WHITE,[208,675,400,82])
        screen.blit(neweffectsStampsBoxRect,(208,640))
        screen.blit(backgroundTabHighlight,(220,642)) #Highlights BG tab text
        
        #Various previews for availible backgrounds.
        screen.blit(background1,(209,675))
        background1Rect = Rect (209,675,78,80)

        screen.blit(background2,(289,675))
        background2Rect = Rect (289,675,78,80)
        
        screen.blit(background3,(369,675))
        background3Rect = Rect (369,675,78,80)

        screen.blit(background4,(449,675))
        background4Rect = Rect (449,675,78,80)

        screen.blit(background5,(529,675))
        background5Rect = Rect (529,675,78,80) 

    elif mb[0]==1 and effectsTabRect.collidepoint((mx,my)) and clicked == False:
        currentTool = "Effects"
        screen.blit(newToolbarRect,(9,125)) 
        draw.rect(screen,WHITE,[208,675,400,82])
        #Clears any previous highlighted tabs
        screen.blit(neweffectsStampsBoxRect,(208,640))
        #Icon turns blue to show it was clicked
        screen.blit(effectsTabHighlight,(360,645))

        #Various previews for the frames availible.
        screen.blit(effects1,(209,675))
        effect1Rect = Rect (209,675,78,80)

        screen.blit(effects2,(289,675))
        effect2Rect = Rect (289,675,78,80)

        screen.blit(effects3,(369,675))
        effect3Rect = Rect (369,675,78,80)

        screen.blit(effects4,(449,675))
        effect4Rect = Rect (449,675,78,80)

        screen.blit(effects5,(529,675))
        effect5Rect = Rect (529,675,78,80)
        
    elif mb[0]==1 and stampsTabRect.collidepoint((mx,my)) and clicked == False:
        currentTool = "Stamps"
        screen.blit(newToolbarRect,(9,125)) 
        draw.rect(screen,WHITE,[208,675,400,82])
        #Clears any previous highlighted tabs
        screen.blit(neweffectsStampsBoxRect,(208,640))
        #Icon turns blue to show it was clicked
        screen.blit(stampsTabHighlight,(440,646))

        #Various previews for the stamps availible.
        screen.blit(stampsPreview1,(235,675))
        stampsPreview1Rect = Rect (235,675,40,40)

        screen.blit(stampsPreview2,(235,716))
        stampsPreview2Rect = Rect (235,716,40,40)

        screen.blit(stampsPreview3,(295,675))
        stampsPreview3Rect = Rect (295,675,80,80)

        screen.blit(stampsPreview7,(395,675))
        stampsPreview7Rect = Rect (395,675,40,40)

        screen.blit(stampsPreview8,(395,716))
        stampsPreview8Rect = Rect (395,716,40,40)

        screen.blit(stampsPreview4,(455,675))
        stampsPreview4Rect = Rect (455,675,80,80)

        screen.blit(stampsPreview5,(555,675))
        stampsPreview5Rect = Rect (555,675,40,40)

        screen.blit(stampsPreview6,(555,716))
        stampsPreview6Rect = Rect (555,716,40,40)

        #Takes a copy of the screen to be used to undo highlights when another stamp is clicked.
        newStampsToolbar = screen.subsurface(stampsToolbar).copy()

    #Other options (located beside the stamps tab)
    elif mb[0]==1 and optionsTabRect.collidepoint((mx,my)) and clicked == False: 
        currentTool = "Options"
        screen.blit(newToolbarRect,(9,125)) 
        draw.rect(screen,WHITE,[208,675,400,82])
        #Clears any previous highlighted tabs
        screen.blit(neweffectsStampsBoxRect,(208,640))
        #Icon turns blue to show it was clicked
        screen.blit(optionsTabHighlight,(515,645))

        screen.blit(instructionsOption,(220,678))
        instructionsOptionRect = Rect (220,678,70,15)

        screen.blit(flipCanvasOption,(220,695))
        flipCanvasOptionRect = Rect (220,695,70,15)

        screen.blit(rotateCanvasOption,(218,712))
        rotateCanvasOptionRect = Rect (218,712,120,16)

        screen.blit(optionButton,(220,735))

        screen.blit(filledShapesOption,(230,730))
        #The actual toggle for filled shapes is the text "(On/Off)"
        filledShapesOptionRectOn = Rect(320,730,25,18)
        filledShapesOptionRectOff = Rect(345,730,25,18)

        screen.blit(thicknessOption,(380,678))
        
        screen.blit(optionButton,(390,698))
        screen.blit(optionButton,(390,713))
        screen.blit(optionButton,(390,728))

        screen.blit(thicknessThinOption,(400,695))
        thicknessThinOptionRect = Rect(390,695,38,12)

        screen.blit(thicknessMediumOption,(400,710))
        thicknessMediumOptionRect = Rect(390,710,65,12)

        screen.blit(thicknessThickOption,(400,728))
        thicknessThickOptionRect = Rect(390,728,45,14)

        #Clears thickness button highlights
        thicknessMenuRect = (390,698,10,50)
        newThicknessMenuRect = screen.subsurface(thicknessMenuRect).copy() 

        screen.blit(optionButton,(480,682))
        screen.blit(optionButton,(488,702))
        screen.blit(optionButton,(488,720))
        screen.blit(optionButton,(488,738))
        
        screen.blit(snapOption,(490,675))
        #The actual toggle for snap is the text "(On/Off)"
        snapOptionRectOn = Rect(528,675,25,22)
        snapOptionRectOff = Rect(555,675,25,22)

        screen.blit(snapSmallOption,(500,700))
        snapSmallOptionRect = Rect(490,700,60,14)

        screen.blit(snapMediumOption,(500,715))
        snapMediumOptionRect = Rect(490,715,60,16)

        screen.blit(snapLargeOption,(500,733))
        snapLargeOptionRect = Rect(490,733,58,16)

        #Clears snap button highlights
        snapChoicesRect = Rect(490,675,90,75) 
        newSnapChoicesRectRect = screen.subsurface(snapChoicesRect).copy() 
        
    #Choosing colours on the palette    
    if mb[0]==1 and palette.collidepoint((mx,my)):
        mouse.set_cursor(*cursors.diamond) #Diamond cursor when choosing colours
        colour = screen.get_at((mx,my))
        #The rectangle matches the colour chosen and the palette is drawn again
        #on top, looks like a border.
        draw.rect(screen,colour,[9,625,180,134])
        screen.blit(palettePic,(19,635))
    else:
        #Returns to the original cursor when anything but the palette is clicked
        mouse.set_cursor(*cursors.tri_left)

    #An easter egg is displayed on the canvas if the logo is clicked and the mouse is held down.
    if mb[0]== 1 and easterEggRect.collidepoint((mx,my)) and clicked == False:
        screen.blit(easterEgg,(430,230))
        
    #Controls for the music player
    #Note: Please lightly tap on the button, do not hold down because it satisfies mb[0]==1, thus it
    #will play/pause very rapidly. Same for prev/next too.
    if mb[0]== 1 and playSongRect.collidepoint((mx,my)) and pauseStatus == False:
        mixer.music.pause()
        #Blits an alternate image that tells the user that the button was clicked
        screen.blit(pausePic,(689,705))
        pauseStatus = True #Reverses the flag so it will play next time
    elif mb[0]== 1 and playSongRect.collidepoint((mx,my)) and pauseStatus:
        mixer.music.unpause()
        #Blits an alternate image that tells the user that the button was clicked
        screen.blit(pausePic,(689,705))
        pauseStatus = False #Reverses the flag so it will pause next time

    #Next button on music player
    if mb[0]== 1 and nextSongRect.collidepoint((mx,my)):
        playlistCounter = playlistCounter + 1 #Goes to the next song in the list
        if playlistCounter>4: #Prevents list out of range
            playlistCounter = 0
        #The following fixes a bug where the music would not play if it was paused.
        if pauseStatus:
            #Blits a blue version of the button image, tells the user that it was pressed
            screen.blit(nextHighlightPic,(749,705))
            init()
            mixer.music.load(songPlaylist[playlistCounter])  
            mixer.music.play()
            pauseStatus = False
        elif pauseStatus==False:
            #Blits a blue version of the button image, tells the user that it was pressed
            screen.blit(nextHighlightPic,(749,705))
            init()
            mixer.music.load(songPlaylist[playlistCounter])  
            mixer.music.play()
            pauseStatus = False

    #Previous button on music player
    #Basically the same code as the Next button, just different coordinates and images 
    if mb[0]== 1 and prevSongRect.collidepoint((mx,my)):
        playlistCounter = playlistCounter - 1
        if playlistCounter<-4:
            playlistCounter = 0
        #The following fixes a bug where the music would not play if it was paused.
        if pauseStatus:
            screen.blit(prevHighlightPic,(629,705))
            init()
            mixer.music.load(songPlaylist[playlistCounter])  
            mixer.music.play()
            pauseStatus = False
        elif pauseStatus==False:
            screen.blit(prevHighlightPic,(629,705))
            init()
            mixer.music.load(songPlaylist[playlistCounter])  
            mixer.music.play()
            pauseStatus = False

    #New (clear canvas)
    if mb[0]== 1 and newRect.collidepoint((mx,my)):
        draw.rect(screen,WHITE,[208,25,800,600])
        #Blits a blue version of the button image, tells the user that it was pressed
        screen.blit(newHighlightPic,(868,682))
        #Allows frames to be applied again (see effects tab)
        frameApplied = False
        #Clears previously stored trails 
        polyTrail = [] 
        endpointX = [] 
        endpointY = []
        pencilTrail = []

    #Save
    if mb[0]== 1 and saveRect.collidepoint((mx,my)):
        #Blits a blue version of the button image, tells the user that it was pressed
        screen.blit(saveHighlightPic,(855,708))
        fileName = asksaveasfilename(parent=root,title="Save Image:")
        if fileName != "": #Avoids saving file with a blank name
            image.save(screen.subsurface(canvas),fileName+".jpg") 

    #Load
    if mb[0]== 1 and loadRect.collidepoint((mx,my)):
        #Blits a blue version of the button image, tells the user that it was pressed)
        screen.blit(loadHighlightPic,(854,730))
        fileName = askopenfilename(parent=root,title="Load Image:")
        if fileName != "": #SDL_RWFromFile(): No file or no mode specified
        #Fixes a crash if the load button is clicked and then the cancel button is clicked.
            loadImage = image.load(fileName) #Instead of fileName+".jpg", fixes .jpg.jpg error
            loadImage = transform.scale(loadImage,(800,600)) #for pictures bigger than the canvas
            screen.set_clip(canvas)
            screen.blit(loadImage,(208,25))            
            screen.set_clip(None)

    #Undo
    if mb[0]==1 and undoRect.collidepoint((mx,my)):
        undoClicked = True
        #Blits a blue version of the button image, tells the user that it was pressed
        screen.blit(undoHighlightPic,(836,642))
        if len(undoList1)!=0: #Can't undo if there is nothing to blit from that list.
            screen.blit(undoList1[-1],(208,25))
            #When undo is clicked, the last item goes to the redo list and it is deleted from the undo list
            undoList2.append(undoList1[-1])
            del undoList1[-1]
                    
    #Redo
    if mb[0]== 1 and redoRect.collidepoint((mx,my)):
        #Blits a blue version of the button image, tells the user that it was pressed
        screen.blit(redoHighlightPic,(916,642))
        if len(undoList2)!=0: #Can't redo if there is nothing to blit from that list.
            undoList1.append(undoList2[-1])
            screen.blit(undoList2[-1],(208,25))
            del undoList2[-1]
            
    #Drawing on the canvas

    #For brush and eraser, using the hypot method instead of drawing lines fixing the jagged edges
    dx,dy=lx-mx,ly-my
    dist = hypot (dx,dy) 

    #The polygon tool has its own if tree because of its right click functionality to close the shape
    #otherwise the user would have to hold down both buttons at once to use it. 
    if mb[0]==1 and canvas.collidepoint((mx,my)) and currentTool == "Polygon":
    #Click to set a vertex, the next click joins a line to that vertex, when
    #satisfied with number of vertices, close the shape with right click.
    #User is not suppose to drag the mouse, just click.
        for i in range (2): #Needs at least 2 pts 
          endx,endy = mouse.get_pos()
          endpointX = endpointX + [endx]
          endpointY = endpointY + [endy]
          pos = mouse.get_pos()
          polyTrail = polyTrail + [pos]
          firstX = endpointX[0]
          firstY = endpointY[0]
          last = len(endpointX)-1 #Fixes list out of range

        if thicknessThin:
            thickness = 1
        elif thicknessMed:
            thickness = 3
        elif thicknessThick:
            thickness = 5
            
        screen.set_clip(canvas)
        draw.lines(screen,colour, False,polyTrail,thickness)
        screen.set_clip(None) #Turns it off after drawing on canvas.
    #Right click closes the shape. Fixes crashing due to list out of range since a line cannot be drawn.
    if mb[2]==1 and canvas.collidepoint((mx,my)) and currentTool == "Polygon" and endpointX!=[]:
        #Closes the shape by joining the first and last point
        screen.set_clip(canvas)
        draw.line(screen,colour,[firstX,firstY],[endpointX[last],endpointY[last]],thickness)
        screen.set_clip(None)
        #These lists are emptied so that new lines drawn will not join to the old shape
        polyTrail = []
        endpointX = []
        endpointY = []

    if currentTool != "Polygon":
        #These lists are emptied so that changing the thickness does not redraw the old shape or when another tool is selected
        #fixes a bug when the thickness is changed.
        polyTrail = []
        endpointX = []
        endpointY = []
        
    if mb[0]==1 and canvas.collidepoint((mx,my)) and currentTool== "Pencil":
        for i in range (2): #Since lines must have at least 2 pts
            pos = mouse.get_pos()
            #Essentially collects points and draws lines joining them
            pencilTrail = pencilTrail + [pos]

        if thicknessThin:
            thickness = 1
        elif thicknessMed:
            thickness = 2
        elif thicknessThick:
            thickness = 3
            
        screen.set_clip(canvas)
        draw.lines(screen,colour, False,pencilTrail,thickness)
        screen.set_clip(None) #Turns it off after drawing on canvas.

    if canvas.collidepoint((mx,my)) and currentTool == "Rect":
        if thicknessThin:
            thickness = 2
        elif thicknessMed:
            thickness = 3
        elif thicknessThick:
            thickness = 4
        
        if mb[0]==1:
            rmx,rmy = mouse.get_pos()
        elif mb[2]==1:
            nmx, nmy = mouse.get_pos()
            screen.blit(oldCanvas,(208,25))
            #Left click to set one corner, right click for the other corner and let go to draw.
            screen.set_clip(canvas)
            if fillStatus:
                draw.rect(screen,colour,[rmx,rmy,nmx-rmx,nmy-rmy])
            else:
                draw.rect(screen,colour,[rmx,rmy,nmx-rmx,nmy-rmy],thickness)
            screen.set_clip(None)

    if currentTool == "Arc":
    #Note: Use the number keys 1-4 to choose the angle of the arcs drawn by the arc tool.
        if thicknessThin:
            thickness = 6
        elif thicknessMed:
            thickness = 8
        elif thicknessThick:
            thickness = 10
            
        #Arc uses a rect for its boundaries. Left click to set one corner, right click for the other corner.
        if mb[0]==1:
            rmx,rmy = mouse.get_pos()
        elif mb[2]==1:
            nmx, nmy = mouse.get_pos()
            screen.blit(oldCanvas,(208,25))
            ellipseLen = nmx-rmx
            ellipseWid = nmy-rmy
            arcRect = Rect(rmx,rmy,ellipseLen,ellipseWid)
            arcRect.normalize()
            #Fixes the error width is greater than ellipse radius. The arc is only drawn thickness is less than half the radii.
            #Based on the ellipse tool since both tools use the same rect parameters.
            if thickness < min(ellipseLen, ellipseWid)//2:
                screen.set_clip(canvas)
                draw.arc(screen,colour,arcRect,arcAngleStart,arcAngleEnd,thickness)
                screen.set_clip(None)

    if canvas.collidepoint((mx,my)) and currentTool == "Ellipse":
    #Refer to rect tool and arc tool
        if thicknessThin:
            thickness = 2
        elif thicknessMed:
            thickness = 3
        elif thicknessThick:
            thickness = 4
        #Left click to set one corner, right click for the other corner and let go to draw.
        if mb[0]==1:
            rmx,rmy = mouse.get_pos()
        elif mb[2]==1:
            nmx, nmy = mouse.get_pos()
            screen.blit(oldCanvas,(208,25))
            ellipseLen = nmx-rmx
            ellipseWid = nmy-rmy
            ellipseRect = Rect(rmx,rmy,ellipseLen,ellipseWid)
            ellipseRect.normalize()
            screen.set_clip(canvas)
            if fillStatus:
                draw.ellipse(screen,colour,ellipseRect)
            else:
                #The Arc tool uses the same parameters, the error when the width is greater than the radius is fixed
                #by dividing it by 2. The ellipse is onlt drawn when it is less than the argument.
                if thickness < min(ellipseLen, ellipseWid)//2:
                    draw.ellipse(screen,colour,ellipseRect,thickness)
            screen.set_clip(None)

    if canvas.collidepoint((mx,my)) and currentTool == "Text":
        #Text appears at cursor, left click to set text.
        screen.set_clip(canvas)
        #Refer to the event loop for "showTextToolText"
        showTextToolText = textFont.render((textToolText), True, colour)
        screen.blit(oldCanvas,(208,25))
        screen.blit(showTextToolText,(mx,my))
        screen.set_clip(None)

    if currentTool != "Text":
        #Clears any previous typed text so that it will not continue from where you left off
        textToolText = ""
        
    if mb[0]==1 and canvas.collidepoint((mx,my)):
        if currentTool == "Eyedrop":
            screen.set_clip(canvas)
            colour = screen.get_at((mx,my))
            screen.set_clip(None)
            draw.rect(screen,colour,[9,625,180,134]) #The colour pallette preview matches
            screen.blit(palettePic,(19,635))

        elif currentTool == "Brush":
            if thicknessThin:
                thickness = 5
            elif thicknessMed:
                thickness = 8
            elif thicknessThick:
                thickness = 12
            
            screen.set_clip(canvas)
            #mb[0] == 1 draws a dot when clicked, independent of MOUSEMOTION. This fixes a bug where
            #the brush does not draw if the user clicks, but does move the mouse.
            draw.circle(screen,colour,(mx,my), thickness)
            for i in range(int(dist)):
                #The brush draws circles instead of thick lines to reduce jagged edges, bug fix thanks to Aaron.
                #Draws circles on the hypot of 2 pts, each loop cycle it is scaled up by i, similar to similar triangles 
                draw.circle(screen, colour, (mx+int(i*dx/dist),my+int(i*dy/dist)), thickness)
            screen.set_clip(None)

        elif currentTool == "Eraser":
            #The same tool as the brush, the colour is just white.
            if thicknessThin:
                thickness = 5
            elif thicknessMed:
                thickness = 8
            elif thicknessThick:
                thickness = 12
            
            screen.set_clip(canvas)
            draw.circle(screen,WHITE,(mx,my), thickness)
            for i in range(int(dist)):
                draw.circle(screen, WHITE, (mx+int(i*dx/dist),my+int(i*dy/dist)), thickness)
            screen.set_clip(None)

        elif currentTool == "Magic":
            #Generates random colours
            r = randint (0,255) 
            g = randint (0,255)
            b = randint (0,254)
            colour = (r,g,b)

            if thicknessThin:
                thickness = 20
            elif thicknessMed:
                thickness = 25
            elif thicknessThick:
                thickness = 30
            
            screen.set_clip(canvas)
            dist = randint (-30,30) #Tiles change in size
            #Basically draw very thick lines that look like tiles with random colours
            draw.line (screen, colour, [mx,my],[mx+dist,my+dist],thickness) 
            screen.set_clip(None)
            #Colour palette matches the random colours
            draw.rect(screen,colour,[9,625,180,134])
            screen.blit(palettePic,(19,635))

        elif currentTool == "Spray":
            #In this case for this tool, "thickness" changes the spray radius.
            if thicknessThin:
                thickness = 45
            elif thicknessMed:
                thickness = 55
            elif thicknessThick:
                thickness = 75
            
            for i in range (5): #Faster
                x = randint (mx-thickness,mx+thickness) #Radius 
                y = randint (my-thickness,my+thickness) #Radius
                #Equation of a circle, if the dot is within, it gets drawn.
                if ((x-mx)**2)+((y-my)**2)<=thickness**2:
                    screen.set_clip(canvas)
                    draw.circle (screen,colour,[x,y],3)
                    screen.set_clip(None)

        elif currentTool == "Fill":
            #The fill tool first sets the selected pixel to the desired colour and then adds the coordinates of the 4 adjacent pixels to a list.
            #Those pixels are checked and deleted after they have been set to the same colour. The loops breaks after the list is empty. 
            screen.set_clip(canvas)
            fillColour = screen.get_at((mx,my)) #fillColour is the colour getting replaced
            fillList = [[mx, my]]
            if screen.get_at((mx,my)) != colour:
                while len(fillList) != 0: #continues until empty since 1 element is deleted each time
                    x,y = fillList.pop()
                    #if the colour at x,y is the colour getting replaced, it is replaced and its adjacent pixels are added to be checked too.
                    if x<=1008 and y<=625 and x>=208 and y>=25 and screen.get_at((x,y)) == fillColour:
                        screen.set_at((x,y), colour)
                        fillList.append([x+1, y])
                        fillList.append([x-1, y])
                        fillList.append([x, y+1])
                        fillList.append([x, y-1])
            screen.set_clip(None)

        elif currentTool == "Line":
            if thicknessThin:
                thickness = 6
            elif thicknessMed:
                thickness = 8
            elif thicknessThick:
                thickness = 10
                
            screen.set_clip(canvas)
            screen.blit(oldCanvas, (208,25)) #Masks previously drawn lines when mb[0] is held down.
            draw.line(screen, colour, lineStart,(mx,my), thickness)
            screen.set_clip(None)

        elif currentTool == "Firework":
        #Basically the same as the graphics exercise, draws lines of random length from mouse position. Looks like explosions.
            if thicknessThin:
                thickness = 2
            elif thicknessMed:
                thickness = 3
            elif thicknessThick:
                thickness = 4
            
            screen.set_clip(canvas)
            draw.line (screen,colour,[mx,my],[mx+randint (1,25),my+randint (1,25)],thickness)
            draw.line (screen,colour,[mx,my],[mx-randint (1,25),my-randint (1,25)],thickness)
            draw.line (screen,colour,[mx,my],[mx+randint (1,25),my-randint (1,25)],thickness)
            draw.line (screen,colour,[mx,my],[mx-randint (1,25),my+randint (1,25)],thickness)
            screen.set_clip(None)

        elif mb[0]==1 and currentTool == "Stamps" and drawStampStatus==1:
            if mb[2]==1 and flipped!=True: #Hold down right click to flip the stamp horizontally
                    stamp1Flipped = transform.flip(stamp1,True,False)
                    flipped = True #It will not continuously flip back and forth when right click is held down.
            screen.set_clip(canvas)
            if flipped:
                #Only 1 stamp is produced on the canvas from a single click, does not create a trail of stamps since the image of the old
                #canvas is being blitted too each time.
                screen.blit(oldCanvas, (208,25)) 
                screen.blit(stamp1Flipped,(mx-100,my-100))
                #Flag reversed, next left click will blit the original stamp as it satisfies the second if statement branch.
                flipped = False 
            else:
                screen.blit(oldCanvas, (208,25))
                screen.blit(stamp1,(mx-100,my-100))
            screen.set_clip(None)

        elif mb[0]==1 and currentTool == "Stamps" and drawStampStatus==2:
            if mb[2]==1 and flipped!=True: #Hold down right click to flip the stamp horizontally        
                stamp2Flipped = transform.flip(stamp2,True,False)
                flipped = True 
            screen.set_clip(canvas)
            if flipped:
                screen.blit(oldCanvas, (208,25))
                screen.blit(stamp2Flipped,(mx-100,my-100))
                flipped = False 
            else:
                screen.blit(oldCanvas, (208,25))
                screen.blit(stamp2,(mx-100,my-100))
            screen.set_clip(None)

        elif mb[0]==1 and currentTool == "Stamps" and drawStampStatus==3:
            if mb[2]==1 and flipped!=True: #Hold down right click to flip the stamp horizontally        
                stamp3Flipped = transform.flip(stamp3,True,False)
                flipped = True 
            screen.set_clip(canvas)
            if flipped:
                screen.blit(oldCanvas, (208,25))
                screen.blit(stamp3Flipped,(mx-150,my-150))
                flipped = False 
            else:
                screen.blit(oldCanvas, (208,25))
                screen.blit(stamp3,(mx-150,my-150))
            screen.set_clip(None)

        elif mb[0]==1 and currentTool == "Stamps" and drawStampStatus==4:
            if mb[2]==1 and flipped!=True: #Hold down right click to flip the stamp horizontally        
                stamp4Flipped = transform.flip(stamp4,True,False)
                flipped = True 
            screen.set_clip(canvas)
            if flipped:
                screen.blit(oldCanvas, (208,25))
                screen.blit(stamp4Flipped,(mx-95,my-100))
                flipped = False 
            else:
                screen.blit(oldCanvas, (208,25))
                screen.blit(stamp4,(mx-95,my-100))
            screen.set_clip(None)

        elif mb[0]==1 and currentTool == "Stamps" and drawStampStatus==5:
            if mb[2]==1 and flipped!=True: #Hold down right click to flip the stamp horizontally        
                stamp5Flipped = transform.flip(stamp5,True,False)
                flipped = True 
            screen.set_clip(canvas)
            if flipped:
                screen.blit(oldCanvas, (208,25))
                screen.blit(stamp5Flipped,(mx-80,my-100))
                flipped = False 
            else:
                screen.blit(oldCanvas, (208,25))
                screen.blit(stamp5,(mx-80,my-100))
            screen.set_clip(None)

        elif mb[0]==1 and currentTool == "Stamps" and drawStampStatus==6:
            if mb[2]==1 and flipped!=True: #Hold down right click to flip the stamp horizontally        
                stamp6Flipped = transform.flip(stamp6,True,False)
                flipped = True 
            screen.set_clip(canvas)
            if flipped:
                screen.blit(oldCanvas, (208,25))
                screen.blit(stamp6Flipped,(mx-120,my-100))
                flipped = False 
            else:
                screen.blit(oldCanvas, (208,25))
                screen.blit(stamp6,(mx-120,my-100))
            screen.set_clip(None)

        elif mb[0]==1 and currentTool == "Stamps" and drawStampStatus==7:
            if mb[2]==1 and flipped!=True: #Hold down right click to flip the stamp horizontally        
                stamp7Flipped = transform.flip(stamp7,True,False)
                flipped = True 
            screen.set_clip(canvas)
            if flipped:
                screen.blit(oldCanvas, (208,25))
                screen.blit(stamp7Flipped,(mx-180,my-150))
                flipped = False 
            else:
                screen.blit(oldCanvas, (208,25))
                screen.blit(stamp7,(mx-180,my-150))
            screen.set_clip(None)

        elif mb[0]==1 and currentTool == "Stamps" and drawStampStatus==8:
            if mb[2]==1 and flipped!=True: #Hold down right click to flip the stamp horizontally        
                stamp8Flipped = transform.flip(stamp8,True,False)
                flipped = True 
            screen.set_clip(canvas)
            if flipped:
                screen.blit(oldCanvas, (208,25))
                screen.blit(stamp8Flipped,(mx-120,my-100))
                flipped = False 
            else:
                screen.blit(oldCanvas, (208,25))
                screen.blit(stamp8,(mx-120,my-100))
            screen.set_clip(None)

    #Backgrounds
    if currentTool == "BG":
        #Just blits the selected background onto the canvas.
        if mb[0]==1 and background1Rect.collidepoint((mx,my)):
            screen.set_clip(canvas)
            screen.blit(backgroundPic1,(208,25))
            screen.set_clip(None)

        elif mb[0]==1 and background2Rect.collidepoint((mx,my)):
            screen.set_clip(canvas)
            screen.blit(backgroundPic2,(208,25))
            screen.set_clip(None)

        elif mb[0]==1 and background3Rect.collidepoint((mx,my)):
            screen.set_clip(canvas)
            screen.blit(backgroundPic3,(208,25))
            screen.set_clip(None)

        elif mb[0]==1 and background4Rect.collidepoint((mx,my)):
            screen.set_clip(canvas)
            screen.blit(backgroundPic4,(208,25))
            screen.set_clip(None)

        elif mb[0]==1 and background5Rect.collidepoint((mx,my)):
            screen.set_clip(canvas)
            screen.blit(backgroundPic5,(208,25))
            screen.set_clip(None)

    #Applying Frames (Effects)
    if currentTool == "Effects":
        if mb[0]==1 and effect1Rect.collidepoint((mx,my)) and frameApplied==False:
            #Simple black border frame, a black rectangle is drawn with the transformed canvas on top. 
            screen.set_clip(canvas)
            canvasFrame1 = screen.subsurface(canvas).copy()
            canvasFrame1 = transform.scale(canvasFrame1,(780,580))
            draw.rect(screen,BLACK,[208,25,800,600])
            screen.blit(canvasFrame1,(218,35))
            screen.set_clip(None)
            frameApplied = True #Prevents the frame from being applied continuously which would distort the image

        elif mb[0]==1 and effect2Rect.collidepoint((mx,my)) and frameApplied==False:
            #Simple white border frame, a white rectangle is drawn with the transformed canvas on top. 
            screen.set_clip(canvas)
            canvasFrame2 = screen.subsurface(canvas).copy()
            canvasFrame2 = transform.scale(canvasFrame2,(780,580))
            draw.rect(screen,WHITE,[208,25,800,600])
            screen.blit(canvasFrame2,(218,35))
            screen.set_clip(None)
            frameApplied = True

        elif mb[0]==1 and effect3Rect.collidepoint((mx,my)) and frameApplied==False:
            #An instant photo style (polaroid) frame
            screen.set_clip(canvas)
            canvasFrame3 = screen.subsurface(canvas).copy()
            canvasFrame3 = transform.scale(canvasFrame3,(726,544))
            draw.rect(screen,BLACK,[208,25,800,600])
            screen.blit(canvasFrame3,(245,53))
            #Avoid changing the aspect ratio, instead a black rectangle is drawn at the bottom
            draw.rect(screen,BLACK,[208,520,800,250])
            screen.set_clip(None)
            frameApplied = True

        elif mb[0]==1 and effect4Rect.collidepoint((mx,my)) and frameApplied==False:
            #A fancy museum-style frame
            screen.set_clip(canvas)
            canvasFrame4 = screen.subsurface(canvas).copy()
            canvasFrame4 = transform.scale(canvasFrame4,(534,401))
            draw.rect(screen,WHITE,[208,25,800,600]) #Masks anything behind since canvas is not scaled perfectly
            screen.blit(canvasFrame4,(341,125))
            screen.blit(fancyFramePic,(208,25))
            screen.set_clip(None)
            frameApplied = True

        elif mb[0]==1 and effect5Rect.collidepoint((mx,my)) and frameApplied==False:
            #A photo negative style frame
            screen.set_clip(canvas)
            #Avoid changing the aspect ratio, instead a black rectangles are drawn over instead of scaling the picture over a black canvas
            #The following chunk of code draws out the frame manually instead of blitting a pre-exisiting .png
            draw.rect(screen,BLACK,[208,25,800,50])
            draw.rect(screen,BLACK,[208,575,800,50])
            draw.line(screen,BLACK,[288,25],[288,625],12)
            draw.line(screen,BLACK,[928,25],[928,625],12)
            dotsTop = 248
            dotsBottom = 248
            for i in range (10):
                draw.circle (screen,WHITE,[dotsTop,50],10)
                dotsTop = dotsTop + 80
                draw.circle (screen,WHITE,[dotsBottom,600],10)
                dotsBottom = dotsBottom + 80
            screen.set_clip(None)
            frameApplied = True

    elif currentTool != "Effects":
        #When the user clicks to another tool, the flag is reversed allowing for another frame to be applied on top.
        #This is meant to deter the user from apply frames on top of frames, but still allows it if the user really wanted to.
        frameApplied = False
            
    #Selecting Stamps
    if currentTool == "Stamps":    
        if mb[0]==1 and stampsPreview1Rect.collidepoint((mx,my)):
            screen.blit(newStampsToolbar, (208,640)) 
            screen.blit(stampsPreview1Highlight, (235,675)) 
            drawStampStatus = 1 #represents "stamp1.png"
        elif drawStampStatus == 1:
            #As long as the stamp was selected, it remains highlighted even when another tab is clicked.
            screen.blit(stampsPreview1Highlight, (235,675))
            
        if mb[0]==1 and stampsPreview2Rect.collidepoint((mx,my)):
            screen.blit(newStampsToolbar, (208,640)) 
            screen.blit(stampsPreview2Highlight, (235,716)) 
            drawStampStatus = 2 #represents "stamp2.png"
        elif drawStampStatus == 2:
            #As long as the stamp was selected, it remains highlighted even when another tab is clicked.
            screen.blit(stampsPreview2Highlight, (235,716))

        if mb[0]==1 and stampsPreview3Rect.collidepoint((mx,my)):
            screen.blit(newStampsToolbar, (208,640)) 
            screen.blit(stampsPreview3Highlight, (295,675)) 
            drawStampStatus = 3 #represents "stamp3.png"
        elif drawStampStatus == 3:
            #As long as the stamp was selected, it remains highlighted even when another tab is clicked.
            screen.blit(stampsPreview3Highlight, (295,675))

        if mb[0]==1 and stampsPreview4Rect.collidepoint((mx,my)):
            screen.blit(newStampsToolbar, (208,640)) 
            screen.blit(stampsPreview4Highlight, (455,675)) 
            drawStampStatus = 6 #stamp 6 and 4 swapped places on the previews
        elif drawStampStatus == 6:
            #As long as the stamp was selected, it remains highlighted even when another tab is clicked.
            screen.blit(stampsPreview4Highlight, (455,675))

        if mb[0]==1 and stampsPreview5Rect.collidepoint((mx,my)):
            screen.blit(newStampsToolbar, (208,640)) 
            screen.blit(stampsPreview5Highlight, (555,675)) 
            drawStampStatus = 5 #represents "stamp5.png"
        elif drawStampStatus == 5:
            #As long as the stamp was selected, it remains highlighted even when another tab is clicked.
            screen.blit(stampsPreview5Highlight, (555,675))

        if mb[0]==1 and stampsPreview6Rect.collidepoint((mx,my)):
            screen.blit(newStampsToolbar, (208,640)) 
            screen.blit(stampsPreview6Highlight, (555,716)) 
            drawStampStatus = 4 #stamp 6 and 4 swapped places on the previews
        elif drawStampStatus == 4:
            #As long as the stamp was selected, it remains highlighted even when another tab is clicked.
            screen.blit(stampsPreview6Highlight, (555,716))

        if mb[0]==1 and stampsPreview7Rect.collidepoint((mx,my)):
            screen.blit(newStampsToolbar, (208,640)) 
            screen.blit(stampsPreview7Highlight, (395,675)) 
            drawStampStatus = 7 #represents "stamp7.png"
        elif drawStampStatus == 7:
            #As long as the stamp was selected, it remains highlighted even when another tab is clicked.
            screen.blit(stampsPreview7Highlight, (395,675))

        if mb[0]==1 and stampsPreview8Rect.collidepoint((mx,my)):
            screen.blit(newStampsToolbar, (208,640)) 
            screen.blit(stampsPreview8Highlight, (395,716)) 
            drawStampStatus = 8 #represents "stamp8.png"
        elif drawStampStatus == 8:
            #As long as the stamp was selected, it remains highlighted even when another tab is clicked.
            screen.blit(stampsPreview8Highlight, (395,716))

    #Seletcing Options
    if currentTool == "Options":
        #The following ensures that the highlights still remain even after switching to a
        #different tab. If false, not highlighted and vice-versa
        if fillStatus==False:
            screen.blit(optionButton,(220,735))
        elif fillStatus:
                screen.blit(optionButtonHighlight,(220,735))
        if snapStatus == False:
                screen.blit(optionButton,(480,682))
        elif snapStatus:
                screen.blit(optionButtonHighlight,(480,682))
                
        if snapSize == "Small":
            screen.blit(optionButtonHighlight,(488,702))
        elif snapSize == "Medium":
            screen.blit(optionButtonHighlight,(488,720))
        elif snapSize == "Large":
            screen.blit(optionButtonHighlight,(488,738))

        if fillStatus:
            screen.blit(optionButtonHighlight,(220,735))
        elif fillStatus == False:
            screen.blit(optionButton,(220,735))

        if thicknessThin:
            screen.blit(optionButtonHighlight,(390,698))
        elif thicknessMed:
            screen.blit(optionButtonHighlight,(390,713))
        elif thicknessThick:
            screen.blit(optionButtonHighlight,(390,728))

        if mb[0]==1 and instructionsOptionRect.collidepoint((mx,my)):
            screen.blit(instructionsPic,(208,25)) 

        elif mb[0]==1 and flipCanvasOptionRect.collidepoint((mx,my)):
            canvasScreen = transform.flip(oldCanvas,True,False) #Horizontal flip
            screen.blit(canvasScreen,(208,25))

        elif mb[0]==1 and rotateCanvasOptionRect.collidepoint((mx,my)):
            #Rotating 180 is the same as reflecting along the x-axis 
            canvasScreen = transform.flip(oldCanvas,False,True) 
            screen.blit(canvasScreen,(208,25))

        if mb[0]==1 and filledShapesOptionRectOn.collidepoint((mx,my)) and fillStatus==False:
            screen.blit(optionButtonHighlight,(220,735))
            fillStatus = True
        elif mb[0]==1 and filledShapesOptionRectOff.collidepoint((mx,my)) and fillStatus:
            screen.blit(optionButton,(220,735))
            fillStatus = False

        #The actual toggle for the snap on/off is the text itself, "(On/Off)"
        if mb[0]==1 and snapOptionRectOn.collidepoint((mx,my)) and snapStatus==False:
            screen.blit(optionButtonHighlight,(480,682))
            snapStatus = True
        elif mb[0]==1 and snapOptionRectOff.collidepoint((mx,my)) and snapStatus:
            screen.blit(optionButton,(480,682))
            snapStatus = False

        if mb[0]==1 and snapSmallOptionRect.collidepoint((mx,my)):
            screen.blit(newSnapChoicesRectRect,(490,675))
            snapSize = "Small"
            screen.blit(optionButtonHighlight,(488,702))

        elif mb[0]==1 and snapMediumOptionRect.collidepoint((mx,my)):
            screen.blit(newSnapChoicesRectRect,(490,675))
            snapSize = "Medium"
            screen.blit(optionButtonHighlight,(488,720))

        elif mb[0]==1 and snapLargeOptionRect.collidepoint((mx,my)):
            screen.blit(newSnapChoicesRectRect,(490,675))
            snapSize = "Large"
            screen.blit(optionButtonHighlight,(488,738))

        if mb[0]==1 and thicknessThinOptionRect.collidepoint((mx,my)):
            screen.blit(newThicknessMenuRect,(390,698))
            #When one option is clicked, the other flags are set to false since you cannot have 2 thickness sizes on at once.
            thicknessThin = True
            thicknessMed = False 
            thicknessThick = False 
            screen.blit(optionButtonHighlight,(390,698))

        elif mb[0]==1 and thicknessMediumOptionRect.collidepoint((mx,my)):
            screen.blit(newThicknessMenuRect,(390,698))
            thicknessThin = False 
            thicknessMed = True
            thicknessThick = False 
            screen.blit(optionButtonHighlight,(390,713))

        elif mb[0]==1 and thicknessThickOptionRect.collidepoint((mx,my)):
            screen.blit(newThicknessMenuRect,(390,698))            
            thicknessThin = False 
            thicknessMed = False 
            thicknessThick = True 
            screen.blit(optionButtonHighlight,(390,728))
            
    lx,ly = mx,my #for brush
    display.flip()
fontQuit #A function previously defined, fixes a random bug from tk import for some reason. Please refer to the very top.
del statusFont
del textFont
quit()
