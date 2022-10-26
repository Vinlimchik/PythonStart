x = 0
y = random(10,400)
def setup():
    size(400,400)
    fill(random(0,255),random(0,255),random(0,255))
    frameRate(15)
     
     
def draw():
    global x
    global y
    x = x + 1
    y = y + 1
    background(000,000,000)
    triangle(y,-y,y,y,0,-y)
