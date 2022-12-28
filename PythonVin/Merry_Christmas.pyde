x = 0 

def setup():
    size(600,600)
    frameRate(8)
    
def draw():
    global x
    background(000,000,000)
    
    #snow
    for x in range(69):
      strokeWeight(random(0,16))
      stroke(255,255,255)
      point(random(10,600,),random(10,600))
    
    #M
    for x in range(69):
      strokeWeight(5)
      stroke(0,252,14) 
      point(random(10,30,),random(200,300))   
      point(random(10,110),random(180,200))
      point(random(50,70,),random(200,300))
      point(random(90,110,),random(200,300))
      
    #E
      stroke(252,0,0)
      point(random(130,150),random(180,300))
      point(random(150,190),random(180,200))
      point(random(150,190),random(230,250))
      point(random(150,190),random(280,300))
      
    #R 
      stroke(0,252,14)
      point(random(210,230),random(180,300))
      point(random(220,280),random(190,210))
      
    #R№2
      stroke(252,0,0,)
      point(random(300,320),random(180,300))
      point(random(310,370),random(190,210))
      
    #Y
    for x in range(69):
      stroke(0,252,14)
      point(random(390,410),random(180,260))
      point(random(390,470),random(240,260))
      point(random(450,470),random(180,310))
      point(random(390,470),random(280,300))
      
      
      
