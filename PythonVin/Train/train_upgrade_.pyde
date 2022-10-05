#animation
def setup():
    size (600,400)
    frameRate (4)
    
def draw():
    background(random(0,255),random(0,255),random(0,255))
    translate (random(0,200),random(0,200))
    
    #line
    strokeWeight (2)
    line (100,120,470,120)
    
    #color rect 1
    fill (random(0,255),random(0,255),random(0,255))
    
    #rect1
    strokeWeight (1)
    rect (100,90,100,60)
    translate (120,0)
    fill (random(0,255),random(0,255),random(0,255))
    rect (100,90,100,60)
    translate (120,0)
    fill (random(0,255),random(0,255),random(0,255))
    rect (100,90,100,60)
    translate (120,0)
    fill (random(0,255),random(0,255),random(0,255))
    rect (100,90,100,60)
    
    #color ellipse
    fill (random(0,255),random(0,255),random(0,255))
    
    #ellipse
    translate (-300,0)
    fill (random(0,255),random(0,255),random(0,255))
    ellipse (60,165,30,30)
    translate (60,0)
    fill (random(0,255),random(0,255),random(0,255))
    ellipse (60,165,30,30)
    translate (60,0)
    fill (random(0,255),random(0,255),random(0,255))
    ellipse (60,165,30,30)
    translate (60,0)
    fill (random(0,255),random(0,255),random(0,255))
    ellipse (60,165,30,30)
    translate (60,0)
    fill (random(0,255),random(0,255),random(0,255))
    ellipse (60,165,30,30)
    translate (60,0)
    fill (random(0,255),random(0,255),random(0,255))
    ellipse (60,165,30,30)
    translate (60,0)
    fill (random(0,255),random(0,255),random(0,255))
    ellipse (60,165,30,30)
    translate (60,0)
    fill (random(0,255),random(0,255),random(0,255))
    ellipse (60,165,30,30)
    
    #color rect2
    fill (random(0,255),random(0,255),random(0,255))
    
    #rect2
    translate (-400,0)
    rect (80,50,40,40)
