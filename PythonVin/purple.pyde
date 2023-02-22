def setup():
    size(600,600)
    background(000,000,000)
    frameRate(5)
    
def draw():
    global x
    background(000,000,000)
    
    if keyPressed:
        x = 0
        if key == ENTER:
            stroke(255,255,255)
            strokeWeight(3)
            while x < 1500:
                point(300+x,300)
                x = x + 5
                #background(000,000,000)
                
                
        if key == BACKSPACE:
            stroke(255,255,255)
            strokeWeight(3)
            while x < 1500:
                point(300-x,300)
                x = x + 5
                #background(000,000,000)      
                
    #purple horseradish
    fill(255,18,255)
    ellipse(300,300,50,50)
                
