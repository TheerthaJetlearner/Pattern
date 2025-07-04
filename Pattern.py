import pgzrun, random
TITLE = "pattern"
WIDTH = 300
HEIGHT = 300
def draw():
    screen.fill("black")
    w = WIDTH
    h = HEIGHT - 200
    r = 155
    g = random.randint(0,255)
    b = 200
    for i in range(20):
        rect = Rect((0,0),(w,h))
        rect.center = 150,150
        screen.draw.rect(rect,(r,g,b))
        w-= 10
        h+= 10
        b-= 5
        
pgzrun.go()
