x = 1
Xch = -1
def setup():
    size(600,600)
    frameRate(55)
    fill(231,40,234)
    
def draw():
    global x
    global Xch
    background(000,000,000)
    translate(300,300)
    ellipse(0,x,30,30)
    x = x + 1
    if x == 300:
      x = x - Xch

    
    
