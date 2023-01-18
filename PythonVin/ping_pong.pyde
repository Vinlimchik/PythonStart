x = 0
m = 100
Xch = 0
n = 0
y = 0

def setup():
    size(600,600)
    frameRate(6900)
    
def draw():
    global x
    global Xch
    global n
    global y
    
    background(000,000,000)
    translate(300,300)
    
    #horseradish
    rect(x,100,m,8)
    
    #horseradish number 2
    ellipse(n,y,30,30)
    
    y = -5
    Xch = 1
    
    if y == x:
        Xch= -1
    
def keyPressed():
    global x
    if keyCode == LEFT:
       x = x - 5
       
    if keyCode == RIGHT:
       x = x + 5 
       

    
    
