
import pygame,time,random
pygame.init()
#setting screen size
screen=pygame.display.set_mode((1000,900))
background=pygame.image.load('background.jpg')
pygame.display.set_caption('Bounce Simulation')
class emoji:
    emoji_image=pygame.image.load('emoji.png')
    g=1
    def __init__(self):
        self.velocityX=4
        self.velocityY=4
        self.X=random.randint(0,768)
        self.Y=random.randint(0,350)
    def render_emoji(self):
        screen.blit(emoji.emoji_image, (self.X,self.Y))
    def move_emoji(self):
        #changing y component of velocity due to downward acceleration
        self.velocityY+=emoji.g
        #changing position based on velocity
        self.X+=self.velocityX
        self.Y+=self.velocityY
        #collission with the walls lead to change in velocity
        if self.X<0 or self.X>768:
            self.velocityX*=-1
        if self.Y<0 and self.velocityY<0:
            self.velocityY*=-1
            self.Y=0
        if self.Y>568 and self.velocityY>0:
            self.velocityY*=-1
            self.Y=568        
#list of emojis created as objects
emoji_List=[emoji(),emoji(),emoji()]
#The main program loop
running=True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
    
    time.sleep(0.02)
    screen.blit(background, (0,0))
    for emoji_item in emoji_List:
        emoji_item.render_emoji()
        emoji_item.move_emoji()
    pygame.display.update()