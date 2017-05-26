class Board():
    def __init__(self,x,y,w,h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.c = 0
        self.r = 0
        self.cw = 0
        self.ch = 0
        self.cells = None
        self.num_mines = None
        self.revealed = None
        return
    
    def generate(self,_columns,_rows, _mines):
        self.cells = [[0 for y in range(_rows)] for x in range(_columns)]
        self.revealed = [[False for y in range(_rows)] for x in range(_columns)]
        self.c = _columns; self.r = _rows
        self.cw = self.w/self.c #cell width
        self.ch = self.h/self.r #cell height
        self.num_mines = _mines
        for m in range(_mines):
            mx = int(random(_columns)); my = int(random(_rows))
            while self.cells[mx][my] < 0: #Negative value is a mine, find a cell that is not a mine
                mx = int(random(_columns)); my = int(random(_rows))
            for x in range(-1,2):
                for y in range(-1,2):
                    if x == 0 and y == 0: #center point, the intended location of the mine
                        self.cells[mx][my] = -_mines #cannot be raised by neighbour count to above 0 (not mine)
                    else:
                        if mx + x < _columns and my + y < _rows: #check overflow
                            if mx + x >= 0 and my + y >= 0: #check underflow
                                self.cells[mx + x][my + y] += 1 #add 1 to neighbouring cells                    
        return self.cells
    
    def checkWin(self):
        c = 0 #count number of remaining hidden cells
        for x in self.revealed: 
            for r in x:
                if not r: 
                    c += 1
        return c == self.num_mines
    
    def display(self):
        pushMatrix()
        translate(self.x, self.y)
        for x in range(len(self.cells)):
            for y in range(len(self.cells[x])):
                stroke(255)
                fill(0)
                rect(self.cw*x,self.ch*y,self.cw,self.ch)
                fill(255)
                if self.revealed[x][y]:
                    textSize(int(0.5*self.ch))
                    n = self.cells[x][y]
                    t = str(n)
                    fill(255)
                    if n < 0: #a mine
                        fill(255,0,0)
                        t = 'X'
                    text(str(t),self.cw*x+self.cw/2,self.ch*y+self.ch/2)
        popMatrix()
        return
    
    def revealAll(self):
        for x in range(self.c):
            for y in range(self.r):
                self.revealed[x][y] = True
        return
    def checkClick(self,mx,my):
        mx -= self.x; my -= self.y
        #check if click is on the board
        if mx < 0 or my < 0 or mx > self.cw * self.c or my > self.ch * self.r: return None, None
        #calculate cell clicked
        x, y = int(mx/self.cw), int(my/self.ch)
        if self.cells[x][y] < 0: #check if cell is a mine
            self.revealAll()
            print('Gameover')
            return 'mine','mine'
        return x, y        
    
    def revealFrom(self, _x, _y):
        self.revealed[_x][_y] = True
        if self.cells[_x][_y] == 0:
            for x in range(-1,2):
                for y in range(-1,2):
                    if _x + x < self.c and _y + y < self.r:
                        if _x + x >= 0 and _y + y >= 0:
                            if not self.revealed[_x+x][_y+y]: #if cell not already revealed
                                        self.revealFrom(_x+x,_y+y)
        return