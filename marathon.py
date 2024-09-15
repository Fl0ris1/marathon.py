import pygame
import random
pygame.init()
WIDTH=800
HEIGHT=600
points=0
screen=pygame.display.set_mode((WIDTH,HEIGHT))
images=["paper.png","glass.png"]
  
class Recycable(pygame.sprite.Sprite):
  def __init__(self,img):
    super().__init__()
    self.image=pygame.image.load(img).convert_alpha()
    self.rect=self.image.get_rect()

class Non_Recycable(pygame.sprite.Sprite):
 def __init__(self):
    self.image=pygame.image.load("plastic.png").convert_alpha()
    self.rect=self.image.get_rect()

ritem_list=pygame.sprite.Group()
nitem_list=pygame.sprite.Group()

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

running=True
while running:
    ritem_list.draw(screen)
    nitem_list.draw(screen)
    for event in pygame.event.get():
      if event.type==pygame.QUIT:
        running=False
    pygame.display.update()