x = 0
#y = 0

n = 0
v = 0
m = 0

t = 0
j = 0

def setup():
    size(600,600)
    frameRate(10)
    background(000,000,000)
    
def draw():
    global x 
    global y 
    
    global n
    global v
    global m
    
    global t
    global j

    y = 0
    while y < 600:
        x = 0
        #if t == 0:
            #fill(000,000,000)
            #t = 1
                
        #else:
            #fill(255,255,255)
            #t = 0
        while x < 600:
            #color
            #if t == 0:
                #fill(000,000,000)
                #t = 1
                
            #else:
                #fill(255,255,255)
                #t = 0
                
            fill(random(0,255),random(0,255),random(0,255))
            ellipse(x,y,30,30)
            x = x + 30
        y = y + 30
