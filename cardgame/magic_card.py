# 12:{'name':'m3','self_servant':2,'self_blood':0,'enermy_servant':0,'enermy_blood':0,'time':2,'img':'m3.jpg','show_img':'m3.jpg','card_type':1}
import pygame
import threading
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
class MagicCard:
    def __init__(self,dict):
        self.self_servant_effect = dict['self_servant']
        self.self_blood_effect = dict['self_blood']
        self.enermy_servant_effect = dict['enermy_servant']
        self.enermy_blood_effect = dict['enermy_blood']
        self.show_img = pygame.image.load(dict['show_img'])
        self.create_time = dict['time']
        self.use_time = ''
        self.screen = ''
        self.type = ''

    def load_card(self,current_time,screen):
        if current_time-self.use_time < 1:
            if self.type == 0:
                if self.enermy_servant_effect>0:
                    m7effect_img = pygame.image.load('m7effect.png')
                    screen.blit(m7effect_img, (0, 145))
                elif self.self_servant_effect>0:
                    m2effect_img = pygame.image.load('m2effect.png')
                    screen.blit(m2effect_img, (0, 300))
            elif self.type==1:
                if self.enermy_servant_effect>0:
                    m7effect_img = pygame.image.load('m7effect.png')
                    screen.blit(m7effect_img, (0, 300))
                elif self.self_servant_effect>0:
                    m2effect_img = pygame.image.load('m2effect.png')
                    screen.blit(m2effect_img, (0, 145))


    def use_card(self,self_blood,enermy_blood,self_servant_list,enermy_servant_list,type):
        self.use_time = time.time()
        new_self_blood = self_blood + self.self_blood_effect
        new_enermy_blood = enermy_blood - self.enermy_blood_effect
        new_self_servant_list = self_servant_list
        new_enermy_servant_list = enermy_servant_list
        for i in new_self_servant_list:
            i.blood_increase(self.self_servant_effect)
        dead_list = []

        for i in new_enermy_servant_list:
            if i.blood_decrease(self.enermy_servant_effect,self.use_time):
                dead_list.append(new_enermy_servant_list.index(i))

        dead_list.sort(reverse=True)
        for i in dead_list:
            del new_enermy_servant_list[i]
        self.type = type





        return new_self_blood,new_enermy_blood,new_self_servant_list,new_enermy_servant_list

