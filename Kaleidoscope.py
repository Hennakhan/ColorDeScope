import os,sys
import numpy as np
import pygame as pg #lazy but responsible (avoid namespace flooding)

class DragImage:
    def __init__(self,img_path):

        self.click = False
        self.image = pg.image.load(img_path)
        mysize = self.image.get_rect().size
        self.rect = pg.Rect(0,0,mysize[0],mysize[1])
        #pg.Surface(self.rect.size).convert()
       # self.image.fill((255,0,0))

    def update(self,surface):
        if self.click:
            print(np.subtract(pg.mouse.get_pos(), self.rect.center))

            self.rect.center += np.subtract(pg.mouse.get_pos(), self.prev_pos)
            self.prev_pos = pg.mouse.get_pos()
            #self.rect.center = pg.mouse.get_pos()
        surface.blit(self.image,self.rect)

def game_event_loop(Player):
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN:
            if Player.rect.collidepoint(event.pos):
                Player.click = True
                Player.prev_pos = event.pos
        elif event.type == pg.MOUSEBUTTONUP:
            Player.click = False
        elif event.type == pg.QUIT:
            pg.quit(); sys.exit()

def main(Surface,Player):
    game_event_loop(Player)
    Surface.fill(0)
    Player.update(Surface)

if __name__ == "__main__":
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pg.init()
    Screen = pg.display.set_mode((1000,600))
    MyClock = pg.time.Clock()
    MyPlayer = DragImage('graph.png')
    #MyPlayer.rect.center = Screen.get_rect().center
    while 1:
        main(Screen,MyPlayer)
        pg.display.update()
        MyClock.tick(30)