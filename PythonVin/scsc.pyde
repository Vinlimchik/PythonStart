x = 0
xch = random(-2,2)
y = random(-101,101)
def setup():
    size(600,600)
    frameRate(20)

def draw():
    global x
    global y
    background(000,000,000)
    fill(random(0,255),random(0,255),random(0,255))
    translate(300,300)
    triangle(-y,y+1,x,x+1,y-1,x-1)
    x = x + 1
