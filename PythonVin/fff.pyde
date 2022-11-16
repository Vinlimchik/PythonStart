x = 0
Xch = 1

def setup():
    size(600,600)
    frameRate(69)
    fill(255,93,234)
    
def draw():
    global x 
    global Xch
    background(000,000,000)
    ellipse(x+300,x,30,30)
    
    x = x + Xch
    
    if x == 300:
      x = -x+x
      Xch = -1
      
    if x == -300:
      x = x
      Xch == 1
      


      
