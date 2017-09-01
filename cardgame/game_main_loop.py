# -*- coding: utf-8 -*-
import pygame
import random
import time
import math
import servant_card
import threading
import os
import Tkinter
import speech
import ast
import magic_card
import copy
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

pygame.init()

black = (0,0,0)
white = (255,255,255)
blue = (0,128,255)
red=(238,238,0)
gold=(234,199,135)
green=(0,255,255)
MAX_CARD_NUMBER = 30
MIN_CARD_NUMBER = 20
card_dict = {1:{'name':'footman','cnname':'footman','attack':0,'attack_time':2,'hate_degree':3,'blood':10,'time':2.5,'attack_type':0,'img':'1.jpg','show_img':'1_show.jpg','card_type':0},
             2:{'name':'rider','cnname':'rider','attack':5,'attack_time':3,'hate_degree':3,'blood':2,'time':2.25,'attack_type':0,'img':'2.jpg','show_img':'2_show.jpg','card_type':0},
             3:{'name':'stone','cnname':'stone', 'attack':2,'attack_time':2,'hate_degree':3,'blood':5,'time':3.5,'attack_type':0,'img':'3.jpg','show_img':'3_show.jpg','card_type':0},
             4:{'name': 'IO', 'cnname':'IO','attack':2,'attack_time':2,'hate_degree':3,'blood':2,'time':1.5,'attack_type':0,'img':'4.jpg','show_img':'4_show.jpg','card_type':0},
             5:{'name':'taunt','cnname':'taunt','attack':2,'attack_time':2,'hate_degree':6,'blood':2,'time':2,'attack_type':4,'img':'5.jpg','show_img':'5_show.jpg','card_type':0},
             6:{'name':'vampire','cnname':'vampire','attack':2,'attack_time':2,'hate_degree':3,'blood':2,'time':1.5,'attack_type':2,'img':'6.jpg','show_img':'6_show.jpg','card_type':0},
             7:{'name':'Gladiator','cnname':'Gladiator','attack':1,'attack_time':2,'hate_degree':5,'blood':2,'time':1,'attack_type':1,'img':'7.jpg','show_img':'7_show.jpg','card_type':0},
             8:{'name':'witch','cnname':'witch','attack':1,'attack_time':2,'hate_degree':5,'blood':1,'time':1,'attack_type':5,'img':'8.jpg','show_img':'8_show.jpg','card_type':0},
             9:{'name':'marine','cnname':'marine','attack':2,'attack_time':1,'hate_degree':3,'blood':2,'time':2.5,'attack_type':0,'img':'9.jpg','show_img':'9_show.jpg','card_type':0},
             10:{'name':'coward','cnname':'coward','attack':20,'attack_time':3,'hate_degree':5,'blood':2,'time':3,'attack_type':3,'img':'10.jpg','show_img':'10_show.jpg','card_type':0},
             11:{'name':'assassin','cnname':'assassin','attack':2,'attack_time':2,'hate_degree':1,'blood':1,'time':1.5,'attack_type':6,'img':'11.jpg','show_img':'11_show.jpg','card_type':0},
             12:{'name':'m3','cnname':'blend one','self_servant':2,'self_blood':0,'enermy_servant':0,'enermy_blood':0,'time':2,'img':'m3.jpg','show_img':'m3.jpg','card_type':1},
             13:{'name':'m4','cnname':'blend two','self_servant':4,'self_blood':0,'enermy_servant':0,'enermy_blood':0,'time':3,'img':'m4.jpg','show_img':'m4.jpg','card_type':1},
             14:{'name':'m5','cnname':'snow ball','self_servant':0,'self_blood':0,'enermy_servant':0,'enermy_blood':5,'time':1,'img':'m5.jpg','show_img':'m5.jpg','card_type':1},
             15:{'name':'m6','cnname':'lighting','self_servant':0,'self_blood':0,'enermy_servant':0,'enermy_blood':10,'time':2,'img':'m6.jpg','show_img':'m6.jpg','card_type':1},
             16:{'name':'m7','cnname':'ice','self_servant':0,'self_blood':0,'enermy_servant':4,'enermy_blood':0,'time':4,'img':'m7.jpg','show_img':'m7.jpg','card_type':1},
             17:{'name':'m8','cnname':'fire','self_servant':0,'self_blood':0,'enermy_servant':2,'enermy_blood':0,'time':2,'img':'m8.jpg', 'show_img': 'm8.jpg', 'card_type': 1},
             18:{'name':'m9','cnname':'stop','card_type':2,'img': 'm9.jpg', 'show_img': 'm9.jpg','time':0}
             }
my_font = pygame.font.SysFont('arial',20)
hurt_font =pygame.font.SysFont('arial',50)
result_font = pygame.font.SysFont('arial', 160)
count_font = pygame.font.SysFont('arial', 30)
card_list_font = pygame.font.SysFont('comicsansms',40)
background_image_filename = '110031qmi1bbnkmwhuj5im.jpg'
background = pygame.image.load(background_image_filename)
player1_image_filename = 'player1.jpg'
player1_image = pygame.image.load(player1_image_filename)
player2_image_filename = 'player2.jpg'
player2_image = pygame.image.load(player2_image_filename)

phrase_temp="start"

#response = speech.input("Say something to start game, please.")  
speech.say("Game starts")  
def callback(phrase, listener):
    global phrase_temp
    if phrase == "goodbye":  
        listener.stoplistening()  
    speech.say(phrase)  
    phrase_temp=phrase.encode("utf-8")
listener = speech.listenforanything(callback)
player1_fight_area = []
player2_fight_area = []
player1_card_point = 4
player2_card_point = 4
player1_blood = 100
player2_blood = 100
current_card_prepare_magic_type_blood =0
player2_current_card_prepare_magic_type_blood=0
r = True
selected_card = None
enter_game =False
main_game = True
start_game = True
quit_game=False
reading = False
player2_reading = False
player1_card_list = []
player2_card_list = [2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10,11,12,12,13,14,15,16,17,18]
magic_effect_list = []
def main_game_initial():
 global player1_fight_area
 global player2_fight_area
 global player1_card_point
 global player2_card_point
 global player1_blood
 global current_card_prepare_magic_type_blood
 global player2_current_card_prepare_magic_type_blood
 global player2_blood
 global r
 global selected_card
 global enter_game
 global main_game
 global start_game
 global quit_game
 global reading
 global player2_reading
 global player1_card_list
 global player2_card_list
 player1_fight_area = []
 player2_fight_area = []
 player1_card_point = 4
 player2_card_point = 4
 player1_blood = 100
 player2_blood = 100
 current_card_prepare_magic_type_blood =0
 player2_current_card_prepare_magic_type_blood=0
 r = True
 selected_card = None
 enter_game =False
 main_game = True
 start_game = True
 quit_game=False
 reading = False
 player2_reading = False
 player1_card_list = []
 player2_card_list = [2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10,11,12,12,13,14,15,16,17,18]

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('card game')
screen.blit(background, (0,0))
clock = pygame.time.Clock()
def getFileList( p ):
        p = str( p )
        if p=="":
              return [ ]
        p = p.replace( "/","\\")
        if p[ -1] != "\\":
             p = p+"\\"
        a = os.listdir( p )
        b = [ x   for x in a if os.path.isfile( p + x ) ]
        return b

def on_click_card_name_save():
    x = card_name_txt.get()
    card_file = open('save_card//'+str(x)+'.txt','w')
    card_file.write(str(player1_card_list))
    card_file.close()
    root.destroy()




def load_card(current_time):
    screen.fill(white)
    screen.blit(player1_image,(600,455) )
    screen.blit(player2_image, (25,45))
    pygame.draw.line(screen, green, (25, 35), (25 + player2_blood * 1, 35),15)
    pygame.draw.line(screen, red, (600, 565), (600 + player1_blood * 1, 565), 15)
    pygame.draw.line(screen, green, (0, 295), (800,285), 3)
    pygame.draw.line(screen, red, (0, 298), (800,290), 3)
    start_x = 465
    start_y = 10
    for card in player1_current_card_list:
        img = pygame.image.load(card_dict[card]['img'])
        screen.blit(img, (start_y, start_x))
        start_y = start_y + 100

    start_x = 15
    start_y = 210
    for card in player2_current_card_list:
        img = pygame.image.load('back.jpg')
        screen.blit(img, (start_y, start_x))
        start_y = start_y + 100

    start_x = 10
    start_y = 300

    for i in player1_fight_area:
        screen.blit(i.show_img, (start_x, start_y))
        text_surface = my_font.render('a:' + str(i.attack) + ' h:' + str(i.hate_degree) + ' b:' + str(i.current_blood),True, black)
        screen.blit(text_surface, (start_x, start_y + 100))
        i.hurted_effect(current_time,screen,start_x, start_y)
        start_x = start_x + 130

    start_x = 10
    start_y = 150

    for i in player2_fight_area:
        screen.blit(i.show_img, (start_x, start_y))
        text_surface = my_font.render('a:' + str(i.attack) + ' h:' + str(i.hate_degree) + ' b:' + str(i.current_blood),True, black)
        screen.blit(text_surface, (start_x, start_y + 100))
        i.hurted_effect(current_time,screen,start_x, start_y)
        start_x = start_x + 130
    if selected_card!= None:
        pygame.draw.rect(screen,blue,(selected_card*100+10,465,80,120),10)
    if reading:
        current_show_servant_time = readingTime - (current_time - prepare_time)
        if current_show_servant_time > 0 and current_show_servant_time < readingTime:
            pygame.draw.line(screen, blue, (600, 585), (600 + current_show_servant_time / readingTime * 100, 585), 15)
        
    if player2_reading:
        current_show_servant_time = player2_reading_time - (current_time - player2_prepare_time)
        if current_show_servant_time > 0 and current_show_servant_time < player2_reading_time:
            pygame.draw.line(screen, blue, (25, 15), (25 + current_show_servant_time / player2_reading_time * 100, 15),
                             15)
    for effect in magic_effect_list:
        effect.load_card(current_time,screen)

    player1_blood_word = my_font.render(str(player1_blood), True, black)
    player2_blood_word = my_font.render(str(player2_blood), True, black)
    screen.blit(player1_blood_word, (700, 475))
    screen.blit(player2_blood_word, (100, 25))


while not quit_game:

 main_game_initial()
 while not enter_game:
    if phrase_temp !='':
        if phrase_temp =='select':
            start_game=False
            enter_game=True
        phrase_temp=''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            main_game = True
            start_game = True
            enter_game=True
            quit_game=True
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if mouse_x>=270 and mouse_x<500 and mouse_y>500 and mouse_y<600:
              start_game=False
              enter_game=True
            if mouse_x>=270 and mouse_x<500 and mouse_y>300 and mouse_y<400:
                player2_card_list = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
                player1_card_list = [2,2,3,3,4,4,5,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
                start_game = True
                enter_game = True
                main_game = False
    screen.blit(background, (0,0))
    title_txt = count_font.render('THE WORLD Card',True,red)
    screen.blit(title_txt,(270,100))
    train_mode_txt= count_font.render('train_mode',True,red)
    screen.blit(train_mode_txt,(270,300)) 
    choice_txt = count_font.render('choice your card',True,red)
    screen.blit(choice_txt,(270,500)) 
    pygame.display.flip()

 while not start_game:
    d = os.getcwd()
    file_list = getFileList(d + '//save_card')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            main_game = True
            start_game = True
            enter_game=True
            quit_game=True
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            for x in range(0,7):
                for y in range(0,4):
                    if mouse_x>100*x+65 and mouse_x<100*x+90 and mouse_y>y*150+125 and mouse_y<150*y +150 and player1_card_list.__len__()<30:
                        t = y * 7 + x + 1
                        if player1_card_list.count(t)<3:
                            player1_card_list.append(t)
            for x in range(0,7):
                for y in range(0,4):
                    if mouse_x>100*x+10 and mouse_x<100*x+35 and mouse_y>y*150+125 and mouse_y<150*y +150:
                        t = y*7+x+1
                        if player1_card_list.count(t)>0:
                            player1_card_list.remove(y*7+x+1)
            if mouse_x>700 and mouse_y>550:
                if player1_card_list.__len__()>=MIN_CARD_NUMBER:
                    start_game = True
                    main_game = False
                    enter_game = False
            if mouse_x<180 and mouse_y>500:
                    main_game = True
                    start_game = True
                    enter_game = False
            if mouse_x>=620 and mouse_x<700 and mouse_y>550 and mouse_y<600:
                root = Tkinter.Tk()
                root.title('input your card section name')
                root.geometry('300x100')
                l = Tkinter.Label(root,text ='Card Name:')
                l.pack()
                card_name_txt = Tkinter.StringVar()
                card_name = Tkinter.Entry(root,textvariable =card_name_txt)
                card_name.pack()
                b = Tkinter.Button(root,text='Press',command = on_click_card_name_save)
                b.pack()
                root.mainloop()
            for i in range(0,file_list.__len__()):
                if mouse_x>710 and mouse_x<800 and mouse_y>i*50 +10 and mouse_y<i*50 +60:
                    card_file = open('save_card//'+file_list[i],'r')
                    card_txt = card_file.read()
                    player1_card_list = ast.literal_eval(card_txt)
                    card_file.close()
    if phrase_temp !='':
        if phrase_temp=='return':
            main_game = True
            start_game = True
            enter_game = False
        elif phrase_temp=='fight':
           if player1_card_list.__len__()>=MIN_CARD_NUMBER:
            start_game = True
            main_game = False
            enter_game = False
        else:
           for i,u in card_dict.items():
            if u['cnname']== phrase_temp and player1_card_list.count(i)<3 and player1_card_list.__len__()<30:
              player1_card_list.append(i)
        phrase_temp=''
    screen.blit(background, (0,0))
    pygame.draw.line(screen,black,(700,0),(700,600),3)

    if player1_card_list.__len__()<20:
        start_img = pygame.image.load('not_start.jpg')
    else:
        start_img = pygame.image.load('start.jpg')


    screen.blit(start_img,(700,550))
    mean_time = 0
    save_txt = count_font.render('SAVE',True,red)
    screen.blit(save_txt,(620,550))
    back_txt = count_font.render('BACK',True,red)
    screen.blit(back_txt,(1 ,550))

    for f in file_list:
        a,b = os.path.split(f)
        c,d = os.path.splitext(b)
        if d == '.txt':
            txt = card_list_font.render(c,True, red)
            screen.blit(txt,(710,file_list.index(f)*50+10))
    for i,u in card_dict.items():
        y = (i-1)/7
        x = (i-1)%7
        img = pygame.image.load(u['img'])
        add_img = pygame.image.load('add.gif')
        decrease_img = pygame.image.load('decrease.gif')
        screen.blit(img, (x*100+10, y*150+5))
        screen.blit(decrease_img, (x * 100 + 10, y * 150 + 125))
        screen.blit(add_img, (x * 100 + 65, y * 150 + 125))
        mean_time = mean_time + player1_card_list.count(i)*u['time']
        text_surface = count_font.render(
            str(player1_card_list.count(i)),
            True, red)
        screen.blit(text_surface, (x * 100 + 40, y * 150 + 120))


    mean_time = mean_time/(player1_card_list.__len__()+1)
    text_surface = count_font.render(
        'M:' + str(mean_time),True, red)
    screen.blit(text_surface, (700, 500))
    pygame.display.flip()



 random.shuffle(player1_card_list)
 random.shuffle(player2_card_list)
 player1_current_card_list = player1_card_list[0:4]
 player2_current_card_list = player2_card_list[1:4]
 readingTime = 2.0
 player2_reading_time = card_dict[player2_current_card_list[int(0)]]['time']
 current_prepare_servant = None
 player2_current_card_prepare_type = 0
 current_card_prepare_type = 0
 player2_current_prepare_servant = None
 if card_dict[player2_current_card_list[int(0)]]['card_type'] == 0:
    player2_current_prepare_servant = servant_card.ServantCard(card_dict[player2_current_card_list[int(0)]])
    player2_current_card_prepare_type = 0
 elif card_dict[player2_current_card_list[int(0)]]['card_type'] == 1:
    player2_current_prepare_servant = magic_card.MagicCard(card_dict[player2_current_card_list[int(0)]])
    player2_current_card_prepare_type = 1
 elif card_dict[player2_current_card_list[int(0)]]['card_type'] == 2:
    i = 1
    while True:
        if card_dict[player2_current_card_list[i]]['card_type'] != 2:
            if card_dict[player2_current_card_list[int(0)]]['card_type'] == 0:
                player2_current_prepare_servant = servant_card.ServantCard(card_dict[player2_current_card_list[int(0)]])
                player2_current_card_prepare_type = 0
            elif card_dict[player2_current_card_list[int(0)]]['card_type'] == 1:
                player2_current_prepare_servant = magic_card.MagicCard(card_dict[player2_current_card_list[int(0)]])
                player2_current_card_prepare_type = 1
              
            break
        i = i+1

 reading = False
 player2_reading = True
 timer_event = pygame.USEREVENT + 1
 start_time = time.time()
 last_card_get_time = start_time
 current_read = 2.0
 prepare_time = time.time()
 player2_prepare_time = time.time()
 pygame.time.set_timer(timer_event,50)


 while not main_game:
    current_time = time.time()
    game_time = current_time - start_time
    current_card_get_time = current_time - last_card_get_time
    clock.tick(60)
   
    if phrase_temp !='' and selected_card == None:
        for i,u in card_dict.items():
           if u['cnname'] == phrase_temp:
               try:
                   selected_card=player1_current_card_list.index(i)
               except Exception:
                   selected_card=None
        if selected_card!=None and not reading:
            if card_dict[player1_current_card_list[int(selected_card)]]['card_type']==0:
                current_card_prepare_type = 0
                current_prepare_servant = servant_card.ServantCard(card_dict[player1_current_card_list[int(selected_card)]])
            elif card_dict[player1_current_card_list[int(selected_card)]]['card_type']==1:
                current_card_prepare_type = 1
                current_card_prepare_magic_type_blood = card_dict[player1_current_card_list[int(selected_card)]]['self_servant']
                current_prepare_servant = magic_card.MagicCard(card_dict[player1_current_card_list[int(selected_card)]])
            elif card_dict[player1_current_card_list[int(selected_card)]]['card_type']==2:
                current_prepare_servant = None
                player2_current_prepare_servant = None
                if player2_reading:
                    current_show_servant_time = player2_reading_time - (current_time - player2_prepare_time)
                    player2_reading = False
                    if player2_current_card_list != []:
                        if card_dict[player2_current_card_list[int(0)]]['card_type'] == 0:
                            player2_current_prepare_servant = servant_card.ServantCard(card_dict[player2_current_card_list[int(0)]])
                            player2_current_card_prepare_type = 0
                        elif card_dict[player2_current_card_list[int(0)]]['card_type'] == 1:
                            player2_current_prepare_servant = magic_card.MagicCard(card_dict[player2_current_card_list[int(0)]])
                            player2_current_card_prepare_type = 1

                        elif card_dict[player2_current_card_list[int(0)]]['card_type'] == 2:
                            current_prepare_servant = None
                            player2_current_prepare_servant = None
                            reading = False
                            player2_reading_time = card_dict[player2_current_card_list[int(0)]]['time']
                            player2_prepare_time = time.time()
                            del player2_current_card_list[0]
                            player2_reading = True
                            ##stop enermy magic
                        ## add other magic type
            readingTime = card_dict[player1_current_card_list[int(selected_card)]]['time']
            prepare_time = time.time()
            reading = True  
            del player1_current_card_list[int(selected_card)]
            selected_card = None
        phrase_temp=''
    
    for event in pygame.event.get():
        t = threading.Thread(load_card(current_time), args=(10,))
        t.start()
        if event.type == pygame.QUIT:
            main_game = True
            start_game = True
            enter_game=True
            quit_game=True
        if event.type == pygame.MOUSEBUTTONDOWN:
           ####################show card mode##################################
            mouse_y,mouse_x = pygame.mouse.get_pos()
            if event.button == 3:
                selected_card = None
            if not reading:
                if event.button == 1:
                    if mouse_x>450:
                        k = math.floor(mouse_y/100)
                        if k<= player1_current_card_list.__len__():
                            selected_card = k
                    if mouse_x>150 and mouse_x<450 and selected_card!=None and selected_card<player1_current_card_list.__len__():
                        if card_dict[player1_current_card_list[int(selected_card)]]['card_type']==0:
                            current_card_prepare_type = 0
                            current_prepare_servant = servant_card.ServantCard(card_dict[player1_current_card_list[int(selected_card)]])
                        elif card_dict[player1_current_card_list[int(selected_card)]]['card_type']==1:
                            current_card_prepare_type = 1
                            current_prepare_servant = magic_card.MagicCard(card_dict[player1_current_card_list[int(selected_card)]])
                            current_card_prepare_magic_type_blood = card_dict[player1_current_card_list[int(selected_card)]]['self_servant']
                        elif card_dict[player1_current_card_list[int(selected_card)]]['card_type']==2:
                            current_prepare_servant = None
                            player2_current_prepare_servant = None
                            if player2_reading:
                                current_show_servant_time = player2_reading_time - (current_time - player2_prepare_time)
                                player2_reading = False
                                if player2_current_card_list != []:
                                    if card_dict[player2_current_card_list[int(0)]]['card_type'] == 0:
                                        player2_current_prepare_servant = servant_card.ServantCard(
                                            card_dict[player2_current_card_list[int(0)]])
                                        player2_current_card_prepare_type = 0
                                        
                                    elif card_dict[player2_current_card_list[int(0)]]['card_type'] == 1:
                                        player2_current_prepare_servant = magic_card.MagicCard(
                                            card_dict[player2_current_card_list[int(0)]])
                                        player2_current_card_prepare_type = 1
                                       
                                    elif card_dict[player2_current_card_list[int(0)]]['card_type'] == 2:
                                        current_prepare_servant = None
                                        player2_current_prepare_servant = None
                                        reading = False

                                    player2_reading_time = card_dict[player2_current_card_list[int(0)]]['time']
                                    player2_prepare_time = time.time()
                                    del player2_current_card_list[0]
                                    player2_reading = True
                            ##stop enermy magic
                        ## add other magic type
                        readingTime = card_dict[player1_current_card_list[int(selected_card)]]['time']
                        prepare_time = time.time()
                        reading = True  
                        del player1_current_card_list[int(selected_card)]
                        selected_card = None
        elif event.type == timer_event:

        ########################read card and show#####################
         if reading:
             current_show_servant_time = readingTime - (current_time - prepare_time)

             if current_show_servant_time<=0:
                 if current_card_prepare_type == 0 and current_prepare_servant!=None:
                    player1_fight_area.append(current_prepare_servant)
                 elif current_card_prepare_type == 1 and current_prepare_servant!=None:
                     player1_blood,player2_blood,player1_fight_area,player2_fight_area = current_prepare_servant.use_card(player1_blood,player2_blood,player1_fight_area,player2_fight_area,0)
                     magic = copy.copy(current_prepare_servant)
                     magic_effect_list.append(magic)
                     #pygame.draw.line(screen, red, (600, 525), (600 + player1_blood * 1, 525), 15) 
                 reading = False

         if player2_reading:
             current_show_servant_time = player2_reading_time - (current_time - player2_prepare_time)

             if current_show_servant_time <= 0:

                 if player2_current_card_prepare_type == 0 and player2_current_prepare_servant!=None:
                    if r:
                        player2_fight_area.append(player2_current_prepare_servant)
                 elif player2_current_card_prepare_type == 1 and player2_current_prepare_servant!=None:
                     if r:
                        player2_blood,player1_blood,player2_fight_area,player1_fight_area = player2_current_prepare_servant.use_card(player2_blood,player1_blood,player2_fight_area,player1_fight_area,1)
                        magic = copy.copy(player2_current_prepare_servant)
                        magic_effect_list.append(magic)
                     #   pygame.draw.line(screen, red, (25, 50), (25 + player1_blood * 1,50),15)
                 if player2_current_card_list!=[]:      
                     r = True
                     player2_reading = False
                     if card_dict[player2_current_card_list[int(0)]]['card_type']==0:
                        player2_current_prepare_servant = servant_card.ServantCard(card_dict[player2_current_card_list[int(0)]])
                        player2_current_card_prepare_type = 0
                     elif card_dict[player2_current_card_list[int(0)]]['card_type']==1:
                         player2_current_prepare_servant = magic_card.MagicCard(card_dict[player2_current_card_list[int(0)]])
                         player2_current_card_prepare_type = 1
                         player2_current_card_prepare_magic_type_blood = card_dict[player2_current_card_list[int(0)]]['self_servant']
                     elif card_dict[player2_current_card_list[int(0)]]['card_type']==2:
                         current_prepare_servant = None
                         player2_current_prepare_servant = None
                         reading = False
                     player2_reading_time = card_dict[player2_current_card_list[int(0)]]['time']
                     player2_prepare_time = time.time()
                     del player2_current_card_list[0]
                     player2_reading = True
                     if player2_current_card_list == []:
                         r = False



          #############################get card mode###########################3

         if current_card_get_time >= 2:
             last_card_get_time = current_time
             if player1_current_card_list.__len__()<6:
                 if player1_card_point<player1_card_list.__len__():
                     player1_current_card_list.append(player1_card_list[player1_card_point])
                     player1_card_point = player1_card_point + 1

             if player2_current_card_list.__len__()<6:
                 if player2_card_point<player2_card_list.__len__():
                     player2_current_card_list.append(player2_card_list[player2_card_point])
                     player2_card_point = player2_card_point + 1


       ################## fight mode #############################
         for servant in player1_fight_area:
             dead_list = []
             if current_time-servant.last_attack_time>=servant.attack_time:
                 servant.last_attack_time = current_time
                 if player2_fight_area == []:
                     player2_blood = player2_blood - servant.action_attack()
                    # pygame.draw.line(screen, green, (25, 50), (25 + player2_blood * 1, 50),15)
                 else:
                     if servant.attack_type == 5:
                         for i in range(0, player2_fight_area.__len__()):
                             if player2_fight_area[i].blood_decrease(servant.action_attack(),current_time):
                                 dead_list.append(i)
                     elif servant.attack_type==6:
                         player2_blood = player2_blood - servant.action_attack()
                       #  pygame.draw.line(screen, green, (25, 50), (25 + player2_blood * 1, 50),15)
                     else:
                       hate_list = []
                       for enermy_servant in player2_fight_area:
                         hate_list.append(enermy_servant.hate_degree)
                       position = hate_list.index(max(hate_list))
                       if player2_fight_area[position].blood_decrease(servant.action_attack(),current_time):
                           dead_list.append(position)   
             dead_list.sort(reverse=True)
             for i in dead_list:
                del player2_fight_area[i]

         for servant in player2_fight_area:
                dead_list = []
                if current_time-servant.last_attack_time>=servant.attack_time:
                    servant.last_attack_time = current_time
                    if player1_fight_area == []:
                        player1_blood = player1_blood - servant.action_attack()
                     #   pygame.draw.line(screen, red, (600, 525), (600 + player1_blood * 1, 525), 15)
                    else:
                        if servant.attack_type == 5:
                            for i in range(0, player1_fight_area.__len__()):
                                if player1_fight_area[i].blood_decrease(servant.action_attack(),current_time):
                                    dead_list.append(i)
                        elif servant.attack_type==6:
                            player1_blood = player1_blood - servant.action_attack()
                         #   pygame.draw.line(screen, red, (600, 525), (600 + player1_blood* 1, 525), 15)
                        else:
                            hate_list = []
                            for enermy_servant in player1_fight_area:
                                hate_list.append(enermy_servant.hate_degree)
                            position = hate_list.index(max(hate_list))
                            if player1_fight_area[position].blood_decrease(servant.action_attack(),current_time):
                                dead_list.append(position)
                dead_list.sort(reverse=True)
                for i in dead_list:
                    del player1_fight_area[i]   

         if player1_blood<=0:
             screen.fill(white)
             text_surface = result_font.render(
                 'You Lose',
                 True, black)
             screen.blit(text_surface, (100, 100))
             screen.blit(player2_image,(350,300) )
             pygame.display.flip()
             pygame.time.delay(5000)
             main_game=True
             enter_game=False

         if player2_blood<=0:
             screen.fill(white)
             text_surface = result_font.render(
                 'You Win',
                 True, black)
             screen.blit(text_surface, (100, 100))
             screen.blit(player1_image,(350,300) )
             pygame.display.flip()
             pygame.time.wait(5000)
             main_game=True
             enter_game=False
    pygame.display.update()
