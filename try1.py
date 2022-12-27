import pygame
from sys import exit

class Birds(pygame.sprite.Sprite):
    def __init__(self,pos_x,pos_y,vel) -> None:
        super().__init__()
        self.image = pygame.Surface((30,50))
        self.rect = self.image.get_rect()
        self.rect.midbottom = (pos_x,pos_y)
        self.vel = vel

    def bird_movement(self):
        self.rect.left += self.vel
        if self.rect.left <= 250:
            self.vel = 2
        elif self.rect.right >= 600:
            self.vel = -2

    # def collision(self):
    #     if pygame.sprite.spritecollide(bird,)

    def update(self):
        self.bird_movement()

class Player(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.Surface((40,60))
        self.image.fill((255,0,0)) # sorry
        self.rect = self.image.get_rect()
        self.rect.midbottom = (width/2,610)
    
    def player_movement_left(self):
        self.rect.left -= 5
        if self.rect.left <= 0:
            self.rect.left = 0
    
        
    def player_movement_right(self):
        self.rect.right += 5
        if self.rect.right >= 800:
            self.rect.right = 800
    

class GameStage():
    def __init__(self) -> None:
        self.state = 'main'

    def main_state(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
        
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            player.player_movement_left()

        if key[pygame.K_RIGHT]:
            player.player_movement_right()

        screen.fill('skyblue')
        screen.blit(ground,(0,610))

        pygame.draw.line(screen,'#1b1b1b',(0,100),(width,100),4)
        bird_grp.draw(screen)
        bird_grp.update()

        player_grp.draw(screen)
    
        pygame.draw.line(screen,'#1b1b1b',(0,200),(width,200),4)
        pygame.display.update()

pygame.init()
clock = pygame.time.Clock()

width,height = 800,690
screen = pygame.display.set_mode((width,height))

#ground
ground = pygame.image.load('ground.png').convert_alpha()

# sprites 
# birds
bird = Birds(width/2,100,2)
bird2 = Birds(450,200,-2)
bird_grp = pygame.sprite.Group()
bird_grp.add(bird)
bird_grp.add(bird2)

# player
player = Player()
player_grp = pygame.sprite.GroupSingle()
player_grp.add(player)

game_active = GameStage()

while True:
    game_active.main_state()
    clock.tick(60)    