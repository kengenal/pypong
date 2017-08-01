import pygame
import time
from pygame.locals import*
from intro import*

class Single():
    """single player class"""
    #variable
    pygame.init()
    player_y = 360
    player_x = 0
    y_change = 0
    gameExit = False
    bally = 360
    ballx = 640
    ball_xchange = 5
    ball_ychange = 5
    board_top_y = 0
    board_bot_y = 710
    board_right_y = 0
    board_right_x = 1270 
    ball_change = 5
    player_height = 100
    player_width = 10
    ball_width = 15
    black = (0, 0, 0)
    white = (255, 255, 255)
    clock = pygame.time.Clock()
    points = 0
    font_type = "Arial"
    pause = True
    icolor = (210,210,210)
    fps = 60
    life_points = 3
    over = False
    pong = pygame.mixer.Sound("sound/pong.wav")
    #over = False
    
    def __init__(self):
        self.game_loop()

    def ball(self,b_x, b_y):
        """creation ball"""
        
        pygame.draw.circle(self.gameDisplay, self.white,(b_x,b_y),self.ball_width)

    def text_object(self,text, font):
        """font atribiutes"""
        self.textSurface = font.render(text, True,self.black)
        return self.textSurface, self.textSurface.get_rect()

    def unpaused(self):
        self.pause = False

    def paused(self):
        """paused game method"""
        self.text = pygame.font.SysFont(self.font_type, 115)
        self.message = self.text.render("P A U S E D", True, self.white)
        self.gameDisplay.blit(self.message, (330,200))

        while self.pause:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_quit()

            
            self.button("Continue",350,450,150,50, self.white, self.icolor, self.unpaused)
            self.button("Quit",750, 450, 150, 50, self.white, self.icolor, self.game_quit)

            pygame.display.update()
            self.clock.tick(self.fps)

            
   
    def game_quit(self):
        pygame.quit()
        quit()
    
    def button(self, msg ,x,y,w,h,ic,ac, action=None):
        """creation button"""
        self.mouse = pygame.mouse.get_pos()
        self.click = pygame.mouse.get_pressed()

        if x +w > self.mouse[0] >x and y + h > self.mouse[1] > y:
            pygame.draw.rect(self.gameDisplay, ac,(x,y,w,h))
            if self.click[0] == 1 and action != None:
               action()
        else:
            pygame.draw.rect(self.gameDisplay, ic,(x,y,w,h))

        self.smallText = pygame.font.SysFont(self.font_type ,20)
        self.textSurf, self.textRect = self.text_object(msg, self.smallText)
        self.textRect.center = ((x + (w/2)), (y + (h/2)))
        self.gameDisplay.blit(self.textSurf, self.textRect)

    def life(self):
        """player life"""
        self.text = pygame.font.SysFont(self.font_type, 20)
        self.message = self.text.render("life: "+str(self.life_points), True, self.white)
        self.gameDisplay.blit(self.message ,(1050,50))
        if self.ballx < self.player_x:
            self.life_points -= 1
            self.ballx = 640
            self.bally = 360
        self.game_over()

    def restart(self):
        """resart atribiutes"""
        self.over = False
        self.points = 0
        self.ballx = 640
        self.bally = 360
        self.life_points = 3
    
    def game_over(self):
        """game over method"""
        if self.life_points == 0:
            self.text = pygame.font.SysFont(self.font_type, 115)
            self.message = self.text.render("Game Over", True, self.white)
            self.gameDisplay.blit(self.message, (330,100))
            self.over = True

            self.text = pygame.font.SysFont(self.font_type, 55)
            self.message = self.text.render("Score: "+ str(self.points), True, self.white)
            self.gameDisplay.blit(self.message, (500,300))
            self.over = True
            while self.over:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.game_quit()

                
                self.button("Play Again",350,450,150,50, self.white, self.icolor,self.restart)
                self.button("Quit",750, 450, 150, 50, self.white, self.icolor, self.game_quit)

                pygame.display.update()
                self.clock.tick(self.fps)

    def score(self, count):
        """show score"""
        self.text = pygame.font.SysFont(self.font_type, 30)
        self.message = self.text.render("Score: "+str(count), True, self.white)
        self.gameDisplay.blit(self.message ,(1050,10))
        
    def dotted_line(self):
        """ Center board line"""
        pygame.draw.rect(self.gameDisplay,self.white, (635,30,10,50))
        pygame.draw.rect(self.gameDisplay,self.white, (635,130,10,50))
        pygame.draw.rect(self.gameDisplay,self.white, (635,230,10,50))
        pygame.draw.rect(self.gameDisplay,self.white, (635,320,10,50))
        pygame.draw.rect(self.gameDisplay,self.white, (635,430,10,50))
        pygame.draw.rect(self.gameDisplay,self.white, (635,530,10,50))
        pygame.draw.rect(self.gameDisplay,self.white, (635,630,10,50))

    def window(self):
        """window initialization"""
        self.display_width = 1280
        self.display_height = 720
        self.gameDisplay = pygame.display.set_mode((self.display_width,self.display_height))
        pygame.display.set_caption("PYPONG")

    def object(self, p_x, p_y, size_x, size_y):
        """object"""
        pygame.draw.rect(self.gameDisplay,self.white, (p_x,p_y,size_x,size_y))

    def player_update(self):
        """player move update"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_quit()
             #player move start

            if event.type == pygame.KEYDOWN:
                    
                if event.key == pygame.K_w:
                    self.y_change = -10       

                if event.key == pygame.K_s:
                    self.y_change = 10

                if event.key == pygame.K_ESCAPE:
                    self.pause= True
                    self.paused()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    self.y_change = 0
                       
        if self.player_y < 10:
                self.y_change = 0.5

        if self.player_y +100 > 710:
                self.y_change = -0.5

        self.player_y += self.y_change
        
    def board(self):
        """creations board"""
        self.board_top = self.object(0,self.board_top_y,1280,10)
        self.board_right = self.object(self.board_right_x,self.board_right_y,10,720)
        self.board_bottom = self.object(0,self.board_bot_y,1280,10)
            
    def ball_update(self):
        """"ball positions update"""
        if self.bally +15 == self.board_bot_y:
            self.ball_ychange = -self.ball_change
            self.points += 50
            pygame.mixer.Sound.play(self.pong)
        

        if self.bally -15 == self.board_top_y:
            self.ball_ychange = self.ball_change 
            self.points += 50
            pygame.mixer.Sound.play(self.pong)

        if self.ballx == self.board_right_x:
            self.ball_xchange = -self.ball_change
            self.points += 50
            pygame.mixer.Sound.play(self.pong)
            
        
        if self.player_x +20 == self.ballx +self.ball_width and self.player_y < self.bally +self.ball_width and self.player_y +self.player_height > self.bally +self.ball_width:
            self.ball_xchange = self.ball_change
            pygame.mixer.Sound.play(self.pong)
        
        self.bally += self.ball_ychange
        self.ballx += self.ball_xchange 
        
        

    def game_loop(self):
        """main game loop"""

        self.window()

        while not self.gameExit:
            
            
            self.player_update()
            self.ball_update()
            self.gameDisplay.fill(self.black)
            self.score(self.points)
            self.life()
            self.ball(self.ballx,self.bally)
            self.board()
            self.player = self.object(self.player_x,self.player_y,self.player_width,self.player_height)
            self.dotted_line()
            pygame.display.update()
            self.clock.tick(self.fps)

if __name__ == '__main__':
    Intro()
    

