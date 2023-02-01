x = 0

def setup():
    size(600,600)
    frameRate(10)
    
def draw():
    global x
    
    background(000,000,000)
    
    for step in range(x):
        ellipse(20,80,30,30)
        translate(40,0)
        fill(255,18,255)
        x = 0
        
    if key == CODED:
        if keyCode == UP:
            x = x + 1
            
        if keyCode == DOWN:
            x = x - 1
