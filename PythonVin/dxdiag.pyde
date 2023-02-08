def setup():
    size(600,600)
    frameRate(6900)
    
def draw():
    global n
    global m
    
    background(000,000,000)
    translate(300,300)
    
    n = 199
    m = 199
    
    while n < 200 and m < 200:
        ellipse(0,0,n,m)
        n = n - 10
        m = m - 10
