import pygame
import random
pygame.init()
WIDTH=800
HEIGHT=600
points=0
win=False
gameover=False
screen=pygame.display.set_mode((WIDTH,HEIGHT))
bg=pygame.image.load("forest.jpg")
bgscale=pygame.transform.scale(bg,(800,600))
#make plastic bag smaller
images=["paper.png","glass.png"]
  
class Recycable(pygame.sprite.Sprite):
  def __init__(self,img):
    super().__init__()
    self.image=pygame.image.load(img).convert_alpha()
    self.image=pygame.transform.scale(self.image,(40,40))
    self.rect=self.image.get_rect()

class Non_Recycable(pygame.sprite.Sprite):
 def __init__(self):
    super().__init__()
    self.image=pygame.image.load("plastic.png").convert_alpha()
    self.image=pygame.transform.scale(self.image,(40,40))
    self.rect=self.image.get_rect()
class Bin(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.image=pygame.image.load("bin.png").convert_alpha()
    self.image=pygame.transform.scale(self.image,(40,40))
    self.rect=self.image.get_rect()
all_sprites=pygame.sprite.Group()
ritem_list=pygame.sprite.Group()
nitem_list=pygame.sprite.Group()
bin_item=Bin()
all_sprites.add(bin_item)
for i in range(0,20):
  item=Recycable(random.choice(images))
  item.rect.x=random.randint(0,800)
  item.rect.y=random.randint(0,600)
  ritem_list.add(item)

for i in range(0,20):
  item=Non_Recycable()
  item.rect.x=random.randint(0,800)
  item.rect.y=random.randint(0,600)
  nitem_list.add(item)

if points<0:
  gameover=True
if points==20:
  screen.fill("Green")

running=True
while running:
    screen.blit(bgscale,(0,0))
    all_sprites.draw(screen)
    ritem_list.draw(screen)
    nitem_list.draw(screen)
    keys=pygame.key.get_pressed()
    if keys[pygame.K_d]:
      if bin_item.rect.x<800:
        bin_item.rect.x-=5
    if keys[pygame.K_s]:
      if bin_item.rect.y<600:
        bin_item.rect.y+=5
    if keys[pygame.K_a]:
      if bin_item.rect.x>0:
        bin_item.rect.x+=5
    if keys[pygame.K_w]:
      if bin_item.rect.y>0:
        bin_item.rect.y-=5
    for event in pygame.event.get():
      if event.type==pygame.QUIT:
        running=False
    pygame.display.update()
