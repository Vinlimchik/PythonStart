x = 0
x2 = 0
x3 = 0
y = 0
y2 = 0
y3 = 0

Xch = 0
X2ch = 0
X3ch = 0
Ych = 0
Y2ch = 0
Y3ch = 0


def setup():
    global x, x2, x3, Xch, X2ch, X3ch
    global y, y2, y3, Ych, Y2ch, Y3ch 
    
    size(600,600)
    frameRate(15)
    fill(random(0,255),random(0,255),random(0,255))
    
    x = random(0,500)
    x2 = random(0,500)
    x3 = random(0,500)
    y = random(0,500)
    y2 = random(0,500)
    y3 = random(0,500)
    
    Xch = random(-2,2)
    X2ch = random(-2,2)
    X3ch = random(-2,2)
    Ych = random(-2,2)
    Y2ch = random(-2,2)
    Y3ch = random(-2,2)
    
    
def draw():
    global x, x2, x3, Xch, X2ch, X3ch
    global y, y2, y3, Ych, Y2ch, Y3ch 
    
    background(000,000,000)
    #translate(300,300)
    triangle(x,y,x2,y2,x3,y3)
    
    x = x + Xch 
    x2 = x2 + X2ch 
    x3 = x3 + X3ch 
    y = y + Ych 
    y2 = y2 + Y2ch 
    y3 = y3 + Y3ch 
