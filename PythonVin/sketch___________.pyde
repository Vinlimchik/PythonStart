x = 0

def setup():
    size(300,300)
    frameRate(30)


def draw():
    global x
    background(000,000,000)
    translate(150,150)
    triangle(0,0,20,x,x,0)
    
    x = x + 1





    
    
