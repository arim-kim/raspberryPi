from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

#sense.show_message("hello")
sense.clear()


dt = 0.1
g  = 0.1

class bird(object):
  def __init__(self, r,g,b):
    self.acc = 0
    self.vy  = 0
    self.posY = 3
    self.posX = 2
    self.color = (r,g,b)

  def move_up(self,event):
    if(event.action == 'pressed'):
        self.acc = -0.5
    if(event.action == 'released'):
        self.acc = 0
        

  def move(self):
    #calc vy  vy = vy + (acc+g)*dt
    self.vy += (self.acc+g)*dt 
    #calc posY = posY + vy*dt
    self.posY += self.vy*dt
    
    if self.posY > 7 :
        self.posY =7
        self.vy*= -0.5
        
    if self.posY < 0 :
        self.posY =0
        self.vy*= -0.5
        
      
  def draw(self):
    sense.clear()
    sense.set_pixel(round(self.posX),round(self.posY), self.color)
      

coco = bird(100,100,0)
sense.stick.direction_up = coco.move_up



while True:
    coco.move()
    coco.draw()
    print(round(coco.vy,2), round(coco.posY,2))
    sleep(dt)
    
    


