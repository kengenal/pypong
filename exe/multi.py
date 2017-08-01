import pygame
import time
import random
from intro import*


class Multi():
    """Multi player class"""
    #variable
    pygame.init()
    player_y = 360
    player_x = 0
    y_change = 0
    p2y_change = 0
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
    font_type = "Arial"
    pause = True
    icolor = (210,210,210)
    fps = 60
    player2x = 1270
    player2y = 360
    p1_points = 0
    p2_points = 0
    over = False
    display_width = 1280
    display_height = 720
    pong = pygame.mixer.Sound("sound/pong.wav")
    
    def __init__(self):
        self.game_loop()
        
    def ball(self,b_x, b_y):
        """Create boll"""
        pygame.draw.circle(self.gameDisplay, self.white,(b_x,b_y),self.ball_width)

    def text_object(self,text, font):
        """Font atribute method"""
        self.textSurface = font.render(text, True,self.black)
        return self.textSurface, self.textSurface.get_rect()

    def show_points(self):
        """show points"""

        if self.ballx > self.player2x:
            self.p1_points += 1
            self.ballx = 640
            self.bally = 360
            
        if self.ballx < self.player_x:
            self.p2_points += 1
            self.ballx = 640
            self.bally = 360

        
        self.text = pygame.font.SysFont(self.font_type, 30)
        self.message = self.text.render(str(self.p1_points), True, self.white)
        self.gameDisplay.blit(self.message ,(580,25))


        self.text = pygame.font.SysFont(self.font_type, 30)
        self.message = self.text.render(str(self.p2_points), True, self.white)
        self.gameDisplay.blit(self.message ,(680,25))
        

       
        self.game_over()

    def restart(self):
        """restart artibutes methond"""
        self.over = False
        self.points = 0
        self.ballx = 640
        self.bally = 360
        self.p1_points = 0
        self.p2_points = 0
        
    
    def game_over(self):
        """game over method"""
        if self.p1_points == 5:
            self.text = pygame.font.SysFont(self.font_type, 115)
            self.message = self.text.render("Game Over", True, self.white)
            self.gameDisplay.blit(self.message, (350,100))
            self.over = True

            self.text = pygame.font.SysFont(self.font_type, 55)
            self.message = self.text.render("Player 1 Winner: "+ str(self.p1_points)+":"+str(self.p2_points), True, self.white)
            self.gameDisplay.blit(self.message, (380,300))
            self.over = True
         
            while self.over:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.game_quit()

                
                self.button("Play Again",350,450,150,50, self.white, self.icolor,self.restart)
                self.button("Quit",750, 450, 150, 50, self.white, self.icolor, self.game_quit)

                pygame.display.update()
                self.clock.tick(self.fps)


        if self.p2_points == 5:
            self.text = pygame.font.SysFont(self.font_type, 115)
            self.message = self.text.render("Game Over", True, self.white)
            self.gameDisplay.blit(self.message, (350,100))
            self.over = True

            self.text = pygame.font.SysFont(self.font_type, 55)
            self.message = self.text.render("Player 2 Winner: "+ str(self.p2_points)+":" +str(self.p1_points), True, self.white)
            self.gameDisplay.blit(self.message, (380,300))
            self.over = True

            while self.over:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.game_quit()

                
                self.button("Play Again",350,450,150,50, self.white, self.icolor,self.restart)
                self.button("Quit",750, 450, 150, 50, self.white, self.icolor, self.game_quit)

                pygame.display.update()
                self.clock.tick(self.fps)
    

    def unpaused(self):
        """unpause game method"""
        self.pause = False

    def paused(self):
        """pause game method"""
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
        """close game method"""
        pygame.quit()
        quit()
    
    def button(self, msg ,x,y,w,h,ic,ac, action=None):
        """creaton button and hover button method"""
        
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
        
        
        self.gameDisplay = pygame.display.set_mode((self.display_width,self.display_height))
        pygame.display.set_caption("PYPONG")
        

    def object(self, p_x, p_y, size_x, size_y):
        """creation obiect method"""
        pygame.draw.rect(self.gameDisplay,self.white, (p_x,p_y,size_x,size_y))
      
    def player_update(self):
        """player movement method"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_quit()

            if event.type == pygame.KEYDOWN:
                    
                if event.key == pygame.K_w:
                    self.y_change = -10       

                if event.key == pygame.K_s:
                    self.y_change = 10

                if event.key == pygame.K_UP:
                    self.p2y_change = -10       

                if event.key == pygame.K_DOWN: 
                    self.p2y_change = 10
                    
                if event.key == pygame.K_ESCAPE:
                    self.pause= True
                    self.paused()
                    

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    self.p2y_change = 0
                    
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    self.y_change = 0
                       
        if self.player_y < 10:
                self.y_change = 0.5

        if self.player_y +100 > 710:
                self.y_change = -0.5
                
        if self.player2y < 10:
                self.p2y_change = 0.5

        if self.player2y +100 > 710:
                self.p2y_change = -0.5


        self.player_y += self.y_change
        self.player2y += self.p2y_change
        
    def board(self):
        """creation board method"""
        self.board_top = self.object(0,self.board_top_y,1280,10)
        self.board_bottom = self.object(0,self.board_bot_y,1280,10)
            
    def ball_update(self):
        """update ball x and y positions"""
        if self.bally +15 == self.board_bot_y:
            self.ball_ychange = -self.ball_change
            pygame.mixer.Sound.play(self.pong)

        if self.bally -15 == self.board_top_y:
            self.ball_ychange = self.ball_change 
            pygame.mixer.Sound.play(self.pong)

            
        if self.player_x +20 == self.ballx +self.ball_width and self.player_y < self.bally +self.ball_width and self.player_y +self.player_height > self.bally +self.ball_width:
            self.ball_xchange = self.ball_change
            pygame.mixer.Sound.play(self.pong)

        if self.player2x  == self.ballx + self.ball_width and self.player2y < self.bally +self.ball_width and self.player2y +self.player_height > self.bally +self.ball_width:
            self.ball_xchange = -self.ball_change
            pygame.mixer.Sound.play(self.pong)
        
        self.bally += self.ball_ychange
        self.ballx += self.ball_xchange 
        

    def game_loop(self):
        """main loop method"""
        self.window()

        while not self.gameExit:
            
            
            
            self.gameDisplay.fill(self.black)
            self.show_points()
            self.player_update()
            self.player1 = self.object(self.player_x,self.player_y,self.player_width,self.player_height)
            self.player2 = self.object(self.player2x, self.player2y ,self.player_width, self.player_height)
            self.ball_update()
            self.ball(self.ballx,self.bally)
            self.board()
            self.dotted_line()
            pygame.display.update()
            self.clock.tick(self.fps)

if __name__ == '__main__':
    Intro()

