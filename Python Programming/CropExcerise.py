import pygame,sys 

pygame.init()

def cropSurface(newWidth,newHeight,cropWidth,cropHeight,image):
       newSurf = pygame.Surface((newWidth , newHeight),
                                pygame.SRCALPHA,32)
       newSurf.blit(image,(0,0),(cropWidth,cropHeight,newWidth,newHeight))

       return newSurf       

def cropBody(newWidth,newHeight,cropWidth,cropHeight,image):
       newBody = pygame.Surface((newWidth , newHeight),
                                pygame.SRCALPHA,32)
       newBody.blit(image,(0,0),(cropWidth,cropHeight,newWidth,newHeight))

       return newBody


width = 900
height = 700

screenDim = (width, height)


screen = pygame.display.set_mode(screenDim)

pygame.display.set_caption("My First Game")

grassImage = pygame.image.load("grass.png").convert()
grassImage = pygame.transform.scale(grassImage,(width, height))
screen.blit(grassImage,(0,0))

rescale = 3
player = pygame.image.load("characterBody.png").convert_alpha()

playerWidth = player.get_rect().width

playerHeight = player.get_rect().height
player = pygame.transform.scale(player,
                                (playerWidth*rescale,
                                 playerHeight*rescale))
adjust = 12
player = cropBody(playerWidth/0.5,playerHeight/0.5,playerWidth -9,playerHeight-4,player)

player = pygame.transform.rotate(player,90)
screen.blit(player,(0,0))


finished = False
while finished == False:
      #processing all the events
       for event in pygame.event.get(): #event1, event2, event3...
              #do appropriate things with events
              if event.type == pygame.QUIT:
                     finished == True
                     pygame.quit()
                     sys.exit()
      
      #flip -updates the screen /load next frame
       pygame.display.flip()
       
#pygame.quit()
