import pygame
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
class ServantCard:

    def __init__(self,dict):
        self.blood_up_line = dict['blood']
        self.current_blood = dict['blood']
        self.attack = dict['attack']
        self.last_hurt= 0
        self.attack_time = dict['attack_time']
        self.hate_degree = dict['hate_degree']
        self.attack_type = dict['attack_type']
        self.img = dict['img']
        self.last_hurted_time=0
        self.show_img = pygame.image.load(dict['show_img'])
        self.card_size = [120,80]
        self.last_attack_time = time.time()
        self.use_time = ''
        self.screen = ''
        self.type = ''
    def hurted_effect(self,current_time,screen,start_x, start_y):
        hurt_font =pygame.font.SysFont('arial',50)
        gold=(234,199,135)
        if current_time-self.last_hurted_time < 1:
          if self.last_hurt<0:
            hurt_text = hurt_font.render(str(self.last_hurt),True, gold)
            screen.blit(hurt_text, (start_x+20, start_y + 25))
            hurted_img = pygame.image.load('hurted.png')
            screen.blit(hurted_img, (start_x, start_y))
            
    def blood_decrease(self,u,current_time):
        self.current_blood = self.current_blood - u
        self.last_hurt = -1*u
        self.last_hurted_time=current_time
        if self.current_blood <= 0 :
            return True
        else:
            return False

    def blood_increase(self,u):
        self.current_blood = self.current_blood + u
        self.last_attacked = u

    def action_attack(self):
        # 0:default attack
        if self.attack_type ==0:
            return self.attack
        # 1:more attack 
        elif self.attack_type==1:
            self.attack+=1
            return self.attack
        # 2:bloodsuck
        elif self.attack_type==2:
            self.current_blood = self.current_blood + self.attack
            if self.current_blood>self.blood_up_line:
                self.current_blood = self.blood_up_line
            return self.attack
        # 3:half attack
        elif self.attack_type==3:
            self.attack=int(self.attack/2)
            return self.attack
        # 4:taunt
        elif self.attack_type==4:
            self.hate_degree+=1
            return self.attack
        # 5:AOE
        elif self.attack_type==5:
            return self.attack
        # 5:attack hero directly
        elif self.attack_type==6:
            return self.attack
            
# 1:{'name':'foot man','attack':2,'attack_time':1,'hate_degree':3,'blood':3,'time':2,'img':'1.png','show_img':'1_show.png'}
