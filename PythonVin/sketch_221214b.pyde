x = 0
Xch = 5
y = random(0,200)
y2 = 0



#def setup
def setup():
    size(600,600)
    frameRate(100)


#def draw
def draw():
    global x
    global Xch
    global y
    global y2
    global img
    
    
#background
    background(000,000,000)
    #imk = loadImage("Camp.jpg")
    #image(imk,0,0,600,600)
    
    
#foundation
    translate(300,300)
    
    
    imc = loadImage("Israel.jpg")
    image(imc,y,-300+y2,100,75)
    
    
    img = loadImage("KristofValts.jpg")
    image(img,x-300,-50,200,150)


#x=
    x = x + Xch
    y2 = y2 + 5
    
    
#cruth
    if x > 400:
      Xch = -5
        
        
    if x == 0:
      Xch = 5
      
      
    if y2 > 200 and x >= 1 and x <= 400:
      y2 = -150
      y = random(-200,100)
      
      
    if y2 >= 600 and x >= 450 and x <= 500:
      y2 = -150
      y = random(-200,100)
