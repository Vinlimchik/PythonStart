x = random(20,400)
y = random(20,400)
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
    
    #apple
    fill(245,20,20)
    ellipse(x,y,20,20)
    
    #green horseradish
    t = mouseX
    u = mouseY
    fill(20,245,100)
    ellipse(t,u,m,m) 
    m = 50
    
    if t and u == x and y:
      background(000,000,000)
      #fill(245,20,20)
      #ellipse(x,x,20,20)
      m = m + 20
      
    
