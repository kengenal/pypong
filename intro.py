import pygame
import time
from pygame.locals import*
from single import*
from multi import*



class Intro():
    """game intro"""
    pygame.init()
    black = (0,0,0)
    white = (255,255,255)
    icolor = (210,210,210)
    clock = pygame.time.Clock()
    gameExit = False
    
    def __init__(self):
        self.main_loop()

    def game_quit(self):
        """game quit method"""
        pygame.quit()
        quit()
        
    def text_object(self,text, font):
        """font atribiutes mothod"""
        self.textSurface = font.render(text, True,self.black)
        return self.textSurface, self.textSurface.get_rect()

    def object(self, color, p_x, p_y, size_x, size_y,):
        """objiect"""
        pygame.draw.rect(self.introDisplay,color, (p_x,p_y,size_x,size_y))
        
    def hello(self, font_size,font_x, font_y):
        """Pypong Text"""
        self.text = pygame.font.SysFont("Arial", font_size)
        self.message = self.text.render("PYPONG",True, self.white)
        self.introDisplay.blit(self.message,(font_x, font_y))

    def display_frame(self):
        """white frame"""
        self.bot = self.object(self.white,0,710,1280,10)
        self.top = self.object(self.white,0,0,1280,10)
        self.left = self.object(self.white,0,0,10,710)
        self.right = self.object(self.white,1270,0,10,710)
        
    def button(self, msg ,x,y,w,h,ic,ac, action=None):
        """creation button with hover """
        self.mouse = pygame.mouse.get_pos()
        self.click = pygame.mouse.get_pressed()

        if x +w > self.mouse[0] >x and y + h > self.mouse[1] > y:
            self.object(ac, x,y,w,h)
            if self.click[0] == 1 and action != None:
               action()
        else:
            self.object(ic , x,y,w,h)

        self.smallText = pygame.font.SysFont("Arial" ,20)
        self.textSurf, self.textRect = self.text_object(msg, self.smallText)
        self.textRect.center = ((x + (w/2)), (y + (h/2)))
        self.introDisplay.blit(self.textSurf, self.textRect)
        
    def menu(self):
        """menu buttons"""
        self.button("Single Player" ,565,360,150,50,self.white,self.icolor,Single)
        self.button("Multi Player" ,565,460,150,50,self.white,self.icolor, Multi)
        self.button("Quit" ,565,560,150,50,self.white,self.icolor, self.game_quit)
        
        
    def main_loop(self):
        """intro main loop"""
        self.display_height = 720
        self.display_width = 1280
        self.introDisplay = pygame.display.set_mode((self.display_width,self.display_height))
        pygame.display.set_caption("PYPONG")

        while not self.gameExit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_quit()
                    
            self.menu()
            self.display_frame()          
            self.hello(115,400,100)
            pygame.display.update()
            self.clock.tick(60)
if __name__ == '__main__':
    Intro()

