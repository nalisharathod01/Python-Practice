import pygame,sys 

pygame.init()

def cropSurface(newWidth,newHeight,cropWidth,cropHeight,image):
       newSurf = pygame.Surface((newWidth , newHeight),
                                pygame.SRCALPHA,32)
       newSurf.blit(image,(0,0),(cropWidth,cropHeight,newWidth,newHeight))

       return newSurf       

def movePlayer(direction,radius,absRot):
       yChange = 5
       deltaTheta = int(90/(radius/yChange))
       if direction == "Left":
              deltaTheta

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

player = pygame.transform.rotate(player,90)
playerStart = player
currentRotation = 0


foot = pygame.image.load("characterFoot.png").convert_alpha()
footWidth = foot.get_rect().width
footHeight = foot.get_rect().height
foot = pygame.transform.scale(foot,(footWidth*rescale,footHeight*rescale))
foot = pygame.transform.rotate(foot,90)
footStart = foot


rescaleBall = 2
ball = pygame.image.load("ball.png").convert_alpha()
ballWidth = ball.get_rect().width
ballHeight = ball.get_rect().height
ball = pygame.transform.scale(ball,(ballWidth*rescaleBall,ballHeight*rescaleBall))


goalLeft = pygame.image.load("goalLeft.png").convert_alpha()
goalLeft= pygame.transform.scale(goalLeft,(250,270))
goalLeftWidth = goalLeft.get_rect().width
goalLeftHeight = goalLeft.get_rect().height
adjust = 12
goalLeft = cropSurface(goalLeftWidth /2 + adjust,
                       goalLeftHeight/2+adjust,
                       goalLeftWidth/2 -adjust,
                       goalLeftHeight/2 - adjust,
                       goalLeft)


goalMiddle = pygame.image.load("goalMiddle.png").convert_alpha()
goalMiddle= pygame.transform.scale(goalMiddle,(250,270))
goalMiddleWidth = goalMiddle.get_rect().width
goalMiddleHeight = goalMiddle.get_rect().height
goalMiddle = cropSurface(goalMiddleWidth,
                         goalMiddleHeight/2+adjust,
                         0,
                         goalMiddleHeight/2-adjust,
                         goalMiddle)



goalRight = pygame.image.load("goalRight.png").convert_alpha()
goalRight= pygame.transform.scale(goalRight,(250,270))
goalRightWidth = goalRight.get_rect().width
goalRightHeight = goalRight.get_rect().height
goalRight = cropSurface(goalRightWidth/2+adjust,
                        goalRightHeight/2+adjust,
                        0,
                        goalRightHeight/2 - adjust,
                        goalRight)

goalStart = (width-goalLeft.get_rect().width-
             goalMiddle.get_rect().width-
             goalLeft.get_rect().width)/2

screen.blit(goalLeft,(goalStart,0))
screen.blit(goalMiddle,(goalStart+goalLeft.get_rect().width,0))
screen.blit(goalRight,(goalStart+goalMiddle.get_rect().width+ goalLeft.get_rect().width,0))


playerX = width/2

playerY = 530

playerXOriginal = playerX
playerYOriginal = playerY

ballX = width/2
ballY = 450

radius = playerY - ballY
screen.blit(player,(playerX - player.get_rect().width/2,playerY-player.get_rect().height/2))
#screen.blit(foot,(0,0))
screen.blit(ball,(ballX-ball.get_rect().width/2,ballY-ball.get_rect().height/2))

frame = pygame.time.Clock()

finished = False
while finished == False:
      #processing all the events
       for event in pygame.event.get(): #event1, event2, event3...
              #do appropriate things with events
              if event.type == pygame.QUIT:
                     finished == True
                     pygame.quit()
                     sys.exit()

       pressedKeys = pygame.key.get_pressed()
       print(pygame.K_LEFT,pressedKeys[pygame.K_LEFT])
       if pressedKeys[pygame.K_LEFT] == 1:
          pass
       elif pressedKeys[pygame.K_RIGHT] == 1:
          pass
       elif pressedKeys[pygame.K_SPACE] == 1:
              pass
       
      #flip -updates the screen /load next frame
       pygame.display.flip()
       frame.tick(30)
#pygame.quit()
