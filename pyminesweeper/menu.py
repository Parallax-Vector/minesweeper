MENU_BACKGROUND_COLOUR = color(200)
class Menu():
    def __init__(self):
        self.buttons = [] #Structure [[x=123, y=456, w=123, h=56, t='QUIT']]
        self.captions = []
        self.x = 0
        self.y = 0
        self.w = None
        self.h = None
        return
    
    def setDimensions(self, x, y, w=None, h=None):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        return
    
    def addButton(self,x,y,w,h,_text,func):
        self.buttons.append([x,y,w,h,_text,func])
        return
    
    def addCaption(self,x,y,w,h,_text):
        self.captions.append([x,y,w,h,_text])
        return
    
    def checkClick(self,mx, my):
        for b in self.buttons:
            if mx >= b[0] and mx <= b[0] + b[2]:
                if my >= b[1] and my <= b[1] + b[3]:
                    #that button is clicked
                    b[5]() #call the function
        return
    
    def display(self):
        pushMatrix()
        translate(self.x,self.y)
        if self.w and self.h:
            fill(MENU_BACKGROUND_COLOUR)
            rect(self.x,self.y,self.w,self.h)
        for c in self.captions:
            fill(255)
            rect(c[0],c[1],c[2],c[3])
            textSize(int(0.7*c[3]))
            fill(0)
            text(c[4],c[0]+c[2]/2,c[1]+c[3]/2)
        for b in self.buttons:
            fill(255)
            rect(b[0],b[1],b[2],b[3]) #x,y,w,h
            textSize(int(0.5*b[3]))
            fill(0)
            text(b[4],b[0]+b[2]/2,b[1]+b[3]/2) #b[4] = t <- the text for the button
        popMatrix()
        return