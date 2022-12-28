x = 300
y = 200
m = 0

def setup():
    size(600,400)
    frameRate(15)
    
def draw():
    global x
    global y  
    global m
    global t
    global u
    
    background(000,000,000)
    
    #red horseradish
    fill(245,20,20)
    ellipse(x,y,80,80)
    
    #green horseradish
    t = mouseX
    u = mouseY
    fill(20,245,100)
    ellipse(t,u,m,m) 
    m = 50
    
    if t >= 235 and t <=365 and y >= 135 and y <= 265:
      m = m + 20 
      
    
      
    
