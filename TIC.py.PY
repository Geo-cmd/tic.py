import pygame
pygame.init()
""" turn 1 is o, turn 2 is x"""
dow = pygame.display.set_mode((600,600))
pygame.display.set_caption("Tik Tac Toe")
"     x        y      "
"turple index is check is written as x[2]"
box1=(50,200,50,200)
box2=(200,350,50,200)
box3=(350,500,50,200)
box4=(50,200,200,350)
box5=(200,350,200,350)
box6=(350,500,200,350)
box7=(50,200,350,500)
box8=(200,350,350,500)
box9=(350,500,350,500)
#places[0] is turn counter now
places=[1,0,0,0,0,0,0,0,0,0]
spawn=1
#print(type(box2))
s=True
while s:
  if places[1]==1:
    x=pygame.draw.circle(dow, (255,0,0), (125,125), (75), (15))
    pygame.display.update()
  if places[1]==2:
    pygame.draw.line(dow, (0,0,255), (50,50), (200,200), 10)
    pygame.draw.line(dow, (0,0,255), (50,200), (200,50), 10)
    pygame.display.update()
  if places[2]==1:
    x=pygame.draw.circle(dow, (255,0,0), (275,125), (75), (15))
    pygame.display.update()
  if places[2]==2:
    pygame.draw.line(dow, (0,0,255), (200,200), (350,50), 10)
    pygame.draw.line(dow, (0,0,255), (200,50), (350,200), 10)
    pygame.display.update()
  if places[3]==1:
    x=pygame.draw.circle(dow, (255,0,0), (425,125), (75), (15))
    pygame.display.update()
  if places[3]==2:
    pygame.draw.line(dow, (0,0,255), (350,200), (500,50), 10)
    pygame.draw.line(dow, (0,0,255), (350,50), (500,200), 10)
    pygame.display.update()
  if places[4]==1:
    x=pygame.draw.circle(dow, (255,0,0), (125,275), (75), (15))
    pygame.display.update()
  if places[4]==2:
    pygame.draw.line(dow, (0,0,255), (50,200), (200,350), 10)
    pygame.draw.line(dow, (0,0,255), (50,350), (200,200), 10)
    pygame.display.update()
  if places[5]==1:
    x=pygame.draw.circle(dow, (255,0,0), (275,275), (75), (15))
    pygame.display.update()
  if places[5]==2:
    pygame.draw.line(dow, (0,0,255), (200,200), (350,350), 10)
    pygame.draw.line(dow, (0,0,255), (350,200), (200,350), 10)
    pygame.display.update()
  if places[6]==1:
    x=pygame.draw.circle(dow, (255,0,0), (425,275), (75), (15))
    pygame.display.update()
  if places[6]==2:
    pygame.draw.line(dow, (0,0,255), (350,350), (500,200), 10)
    pygame.draw.line(dow, (0,0,255), (350,200), (500,350), 10)
    pygame.display.update()
  if places[7]==1:
    x=pygame.draw.circle(dow, (255,0,0), (125,425), (75), (15))
    pygame.display.update()
  if places[7]==2:
    pygame.draw.line(dow, (0,0,255), (50,350), (200,500), 10)
    pygame.draw.line(dow, (0,0,255), (50,500), (200,350), 10)
    pygame.display.update()
  if places[8]==1:
    x=pygame.draw.circle(dow, (255,0,0), (275,425), (75), (15))
    pygame.display.update()
  if places[8]==2:
    pygame.draw.line(dow, (0,0,255), (200,350), (350,500), 10)
    pygame.draw.line(dow, (0,0,255), (200,500), (350,350), 10)
    pygame.display.update()
  if places[9]==1:
    x=pygame.draw.circle(dow, (255,0,0), (425,425), (75), (15))
    pygame.display.update()
  if places[9]==2:
    pygame.draw.line(dow, (0,0,255), (350,350), (500,500), 10)
    pygame.draw.line(dow, (0,0,255), (350,500), (500,350), 10)
    pygame.display.update()
  if places[1]==places[4]==places[7] and places[1]>0:
    s=False
  if places[1]==places[5]==places[9] and places[1]>0:
    s=False
  if places[2]==places[5]==places[8] and places[2]>0:
    s=False
  if places[3]==places[6]==places[9] and places[3]>0:
    s=False
  if places[3]==places[5]==places[7] and places[3]>0:
    s=False
  if places[4]==places[5]==places[6] and places[4]>0:
    s=False
  if places[7]==places[8]==places[9] and places[7]>0:
    s=False
  if places[1]==places[2]==places[3] and places[1]>0:
    s=False

  for event in pygame.event.get():
    if event.type == pygame.MOUSEBUTTONDOWN:
      posx,posy = pygame.mouse.get_pos()
      if posx > box1[0] and posx < box1[1]:
        if posy > box1[2] and posy < box1[3]:
          if places[1] == 0:
            if places[0]==1:
              places[1]=1
              places[0]=2
              break
            if places[0]==2:
              places[1]=2
              places[0]=1
              break
      if posx > box2[0] and posx < box2[1]:
        if posy > box2[2] and posy < box2[3]:
          if places[2] == 0:
            if places[0]==1:
              places[2]=1
              places[0]=2
              break
            if places[0]==2:
              places[2]=2
              places[0]=1
              break
      if posx > box3[0] and posx < box3[1]:
        if posy > box3[2] and posy < box3[3]:
          if places[3] == 0:
              if places[0]==1:
                places[3]=1
                places[0]=2
                break
              if places[0]==2:
                places[3]=2
                places[0]=1
                break
      if posx > box4[0] and posx < box4[1]:
        if posy > box4[2] and posy < box4[3]:
          if places[4] == 0:
            if places[0]==1:
              places[4]=1
              places[0]=2
              break
            if places[0]==2:
              places[4]=2
              places[0]=1
              break
      if posx > box5[0] and posx < box5[1]:
        if posy > box5[2] and posy < box5[3]:
          if places[5] == 0:
            if places[0]==1:
              places[5]=1
              places[0]=2
              break
            if places[0]==2:
              places[5]=2
              places[0]=1
              break
      if posx > box6[0] and posx < box6[1]:
        if posy > box6[2] and posy < box6[3]:
         if places[6] == 0:
            if places[0]==1:
              places[6]=1
              places[0]=2
              break
            if places[0]==2:
              places[6]=2
              places[0]=1
              break
      if posx > box7[0] and posx < box7[1]:
        if posy > box7[2] and posy < box7[3]:
          if places[7] == 0:
            if places[0]==1:
              places[7]=1
              places[0]=2
              break
            if places[0]==2:
              places[7]=2
              places[0]=1
              break
      if posx > box8[0] and posx < box8[1]:
        if posy > box8[2] and posy < box8[3]:
         if places[8] == 0:
            if places[0]==1:
              places[8]=1
              places[0]=2
              break
            if places[0]==2:
              places[8]=2
              places[0]=1
              break
      if posx > box9[0] and posx < box9[1]:
        if posy > box9[2] and posy < box9[3]:
          if places[9] == 0:
            if places[0]==1:
              places[9]=1
              places[0]=2
              break
            if places[0]==2:
              places[9]=2
              places[0]=1
              break
                
                      
    if event.type == pygame.QUIT:
      s=False
  pygame.draw.line(dow,(60,60,60), (50, 200), (500, 200))
  pygame.draw.line(dow,(60,60,60), (50, 350), (500, 350))
  pygame.draw.line(dow,(60,60,60), (200, 50), (200, 500))
  pygame.draw.line(dow,(60,60,60), (350, 50), (350, 500))   
  pygame.display.update()
pygame.quit()