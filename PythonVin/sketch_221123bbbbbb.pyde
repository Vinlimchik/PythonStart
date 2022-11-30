x = 300
y = 90

def setup():
    size(600,400)
    frameRate(100)
    
def draw():
    global x
    global y
    
    translate(300,200)
    background(000,000,000)
    
    jmk = loadImage("Red Apple.jpeg")
    image(jmk, 0, -x, 70, 70)
    
    jmg = loadImage("Da.jpg")
    image(jmg, 0, -50, 30+y, 50+y)
    
    x = x - 10
    
    if x == 100:
        y = y + 30
        x = x = 300
        
    if y == 100:
        noLoop()
