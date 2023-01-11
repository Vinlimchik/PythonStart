x = 10
y = 255
m = 255
n = 255
u = 1

def setup():
    size(600,400)
    frameRate(20)
    background(000,000,000)
    
    
def draw():
    
    global u
    stroke(255,255,255)
    textSize(44)
    text("60 - u",450,300)
    
    
    
    
    push()
    if mousePressed:
        stroke(y,m,n)
        strokeWeight(x)
        line(pmouseX,pmouseY,mouseX,mouseY)
    pop()
    
    
    #button №1
    fill(250,77,253)
    rect(40,20,90,50)
    fill(255)
    textSize(20)
    text("delete",60,50)
    
    #button №2
    fill(250,77,253)
    rect(140,20,90,50)
    fill(255)
    textSize(20)
    text("thinner",160,50)
    
    #button №3
    fill(250,77,253)
    rect(240,20,90,50)
    fill(255)
    textSize(20)
    text("thicker",260,50)
    
    #button №4
    fill(225,255,8)
    rect(340,20,90,50)
    
    #button №5
    fill(255,175,237)
    rect(440,20,90,50)

     
def mouseClicked():
    global x
    global y
    global m
    global n
    #button №1
    if mouseX > 40 and mouseX < 130 and mouseY > 20 and mouseY < 70:
      background(000,000,000)
      
    #button №2
    if mouseX > 140 and mouseX < 230 and mouseY > 20 and mouseY < 70:
      x = x - 10
      
    #button №3 
    if mouseX > 240 and mouseX < 330 and mouseY > 20 and mouseY < 70:
      x = x + 10
      
    #buttn №4
    if mouseX > 340 and mouseX < 430 and mouseY > 20 and mouseY < 70: 
      y = 225
      m = 255
      n = 8
      
    #button №5 
    if mouseX > 440 and mouseX < 530 and mouseY > 20 and mouseY < 70:
      y = 255
      m = 175
      n = 237
      
    
