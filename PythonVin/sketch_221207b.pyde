x = 0
x2 = 0
Xch = 4
y = random(0,200)
y2 = 0


#def setup
def setup():
    size(600,600)
    frameRate(100)


#def draw
def draw():
    global x
    global x2
    global Xch
    global y
    global y2
    
    imk = loadImage("Camp.jpg")
    image(imk,0,0,600,600)
    
    translate(300,300)
    
    imc = loadImage("Israel.jpg")
    image(imc,y,-300+y2,100,75)
    
    img = loadImage("KristofValts.jpg")
    image(img,x-300,-50,200+x2,150+x2)

#=
    x = x + Xch
    y2 = y2 + 5
    
#if
    if x > 400:
      Xch = -4
        
    if x == 0:
      Xch = 4
      
    if y2 > 600:
      y2 = 0
      y = random(-200,200)
      
#very hard

    if x == y2:
      x2 + 50
