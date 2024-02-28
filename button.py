import pygame

#button class
class ButtonImage():
  def __init__(self, x, y, image_normal, scale = 1):
    width = image_normal.get_width()
    height = image_normal.get_height()
    self.image_normal = pygame.transform.scale(image_normal, (int(width * scale), int(height * scale)))
    self.rect = self.image_normal.get_rect()
    self.rect.topleft = (x, y)
    self.clicked = False
  
  def draw(self, surface):
    #draw button on screen
    surface.blit(self.image_normal, (self.rect.x, self.rect.y))

    if self.clicked == True:
      self.clicked = False
      return True
    else: pass
  
  def isclicked (self, event):
    pos = pygame.mouse.get_pos()
    
    if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.FINGERDOWN:
      if event.button == 1:
        if self.rect.collidepoint(pos):
          self.clicked = True
        else: 
          self.clicked = False


#+------------------------------------------------------------------------------------------+



class ButtonStd():
  def __init__(self, colour, x, y, width, height, text =""):
    
    self.colour = colour
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.text = text
    self.clicked = False
    self.rect = pygame.Rect(x,y,width,height)
  
  def draw(self, surface, font, outline = None):
    ### Draws outline for Button
    if outline:
      pygame.draw.rect(surface,outline,(self.x-2,self.y-2,self.width+4, self.height +4),0)

    ###Draws the Button
    pygame.draw.rect(surface, self.colour, (self.x,self.y,self.width,self.height),0)

    ### Adds Text to Button
    if self.text != "":
      text = font.render(self.text, 1, (0,0,0))
      surface.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    if self.clicked == True:
      self.clicked = False
      return True
    else: pass
  
  def isclicked (self, event):
    pos = pygame.mouse.get_pos()
    
    if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.FINGERDOWN:
      if event.button == 1:
        if self.rect.collidepoint(pos):
          self.clicked = True
        else: 
          self.clicked = False

#+------------------------------------------------------------------------------------------+
