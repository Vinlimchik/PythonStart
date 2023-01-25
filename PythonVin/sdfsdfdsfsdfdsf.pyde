x = 0
y = 0
n = 0

v = 0

def setup():
    size(600,600)
    frameRate(69)
    
def draw():
    global x
    global y
    global n
    
    global v
    
    background(000,000,000)
    
    for step in range(10):
        fill(255,18,255)
        rotate(radians(2))
        ellipse(400,300,40,80)
        
        fill(224,255,0)
        rect(v,300,20,20)
        
        v = 300
        
        if keyPressed:
            if key == 'W' or key =='w':
                v = v + 1
                
            if key == 'S' or key == 's':
                v = v - 1
        
        fill(x,y,n)
        ellipse(400,400,40,40)
        x = 0
        y = 255
        n = 206
        
        if key:
            if key == 'B' or key == 'b':
                x = 255
                y = 255
                n = 255
            if key == 'N' or key == 'n':
                x = 0
                y = 255
                n = 206

    
