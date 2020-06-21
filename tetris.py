import pygame as pg

BREITE, SPALTEN, ZEILEN = 400, 10, 20
ABSTAND = BREITE // SPALTEN
HOEHE = ABSTAND * ZEILEN
grid = [0] * SPALTEN * ZEILEN


pg.init()
screen = pg.display.set_mode([BREITE, HOEHE])

weitermachen = True

while weitermachen:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            weitermachen = False
    screen.fill[(0,0,0)]
    for n, farbe in enumerate(grid):
        if farbe > 0:
            x = n % SPALTEN * ABSTAND
            y = n // SPALTEN * ABSTAND
            screen.blit(bilder[farbe],(x,y))

pg.quit()