import pgzrun, random
TITLE = "pattern"
WIDTH = 300
HEIGHT = 300
def draw():
    screen.fill("black")
    w = WIDTH
    h = HEIGHT - 200
    r = 155
    b = 200
    g = random.randint(0,255)
    rad = 50
    for i in range(20):
        screen.draw.circle((150,150),rad,(r,g,b))
        w-= 10
        h+= 10
        b-= 5
        rad+= 10
pgzrun.go()
