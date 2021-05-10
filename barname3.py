import pygame
import time
import pyttsx3

pygame.init()

#music
Bio_musice = pygame.mixer.Sound('Sound_1.mp3')
pygame.mixer.music.load('ss.mp3')
pygame.mixer.music.load('musica.ogg')

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
bright_red = (255,0,0)
green = (0,200,0)
bright_green=(0,255,0)
Mycolor_a = (164, 168, 208)
Mycolor = (12,230,114)
Mycolor1 = (148,108,114)
blue = (0, 0, 180)
bright_blue = (0, 0, 255)
yellow = (255, 255, 0)
yellow_br = (255,200,0)
light_blue = (0, 255, 255)
light_blue_br = (0,200,255)
purple = (191, 0, 255)
purple_br = (191, 0 ,200)
Mycolor_sorati = (255, 0, 64)
Mycolor_sorati_br = (200 ,0 ,64)
Mycolor_x = (206, 209, 74)
Mycolor_x_br = (170, 209,74)
orange = (255, 64, 0)
orange_br = (200,64,0)
Mycolor_b = (255, 99, 229)
Mycolor_b_br = (200,99,229)
Mycolor_c = (0, 255, 141)
Mycolor_c_br =(0, 200, 141)
Mycolor_d = (200, 255, 92)
Mycolor_d_br = (200, 200, 92)
Mycolor_e = (255, 107, 255)
Mycolor_e_br = (200, 107, 255)
Mycolor_f = (117, 255, 25)
Mycolor_f_br = (117, 200, 25)

gameDisplay=pygame.display.set_mode((display_width,display_width))

iconimage = pygame.image.load("e.png")

pygame.display.set_icon(iconimage)

pygame.display.set_caption('Biology')

clock = pygame.time.Clock()
#تابعی برای ساختن دکمه 
def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    #print(click)
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            #action()
            pygame.mixer.music.stop()
            pygame.mixer.Sound.play(Bio_musice)
            if action == "play":
                game_loop()
            elif action == "quit":
                pygame.mixer.music.stop()
                pygame.mixer.Sound.play(Bio_musice)
                pygame.quit()
            
                quit()    
            elif action =='digestive system':
                click_intro(1000,800,'a.jpg','imagegva.jpg',white,'freesansbold.ttf',70,20,'Back to Home',0,0,200,60,green,bright_green,'digestive system',800,600,400,400,0,60)
            
            elif action == 'Back to Home':
                game_loop()
            
            elif action == 'Mouth and Esophagus':
                 click_intro(1525,800,'a.jpg','mouse_c.png',white,'freesansbold.ttf',70,20,'Back to Home',0,0,200,60,green,bright_green,'Mouth and Esophagus',800,600,600,275,400,500)
            
            elif action == 'Respiratory System':
                click_intro(1000,800,'a.jpg','mouse_e.png',white,'freesansbold.ttf',70,20,'Back to Home',0,0,200,60,green,bright_green,'Respiratory System',800,600,600,700,400,0)
            
            elif action == 'Lymphatic system':
                click_intro(1000,800,'a.jpg','aksmatn.png',white,'freesansbold.ttf',70,20,'Back to Home',0,0,200,60,green,bright_green,'Lymphatic system',800,600,600,700,400,0)
            
            elif action == 'circulatory system':
                click_intro(1300,800,'a.jpg','matnegardesh.png',white,'freesansbold.ttf',70,20,'Back to Home',0,0,200,60,green,bright_green,'circulatory system',800,600,600,700,700,-1)
            
            elif action == 'Menu':
                click_intro(1500,800,'a.jpg','menu.jpg',white,'freesansbold.ttf',70,20,'Back to Home',0,0,200,60,green,bright_green,'Menu',800,600,600,700,200,80)
            
            elif action == 'mute':
                click_intro(1200,800,'a.jpg','mute.png',white,'freesansbold.ttf',70,20,'Back to Home',0,0,200,60,green,bright_green,'Menu',800,600,600,700,500,50)
            
            elif action == 'about us':
                click_intro(1525,800,'a.jpg','about.jpg',white,'freesansbold.ttf',70,20,'Back to Home',0,0,200,60,green,bright_green,'about us',800,600,300,350,980,430)
            
            elif action == 'Muscular device':
                click_intro(1000,800,'a.jpg','mahiche.jpg',white,'freesansbold.ttf',70,20,'Back to Home',0,0,200,60,green,bright_green,'Muscular device',800,500,580,650,400,0)
            
            elif action == 'reproductive system':
                click_intro(1000,800,'a.jpg','tanasoli.jpg',white,'freesansbold.ttf',70,20,'Back to Home',0,0,200,60,green,bright_green,'reproductive system',800,600,600,500,400,0)
            
            elif action == 'Skeletal device':
                click_intro(1000,800,'a.jpg','eskelet.jpg',white,'freesansbold.ttf',70,20,'Back to Home',0,0,200,60,green,bright_green,'Skeletal device',800,600,600,600,400,0)
            
            elif action == 'Immune system':
                click_intro(1000,800,'a.jpg','eimeni.jpg',white,'freesansbold.ttf',70,20,'Back to Home',0,0,200,60,green,bright_green,'Immune system',800,600,600,600,400,0)
            
            elif action == 'Integumentary system':
                click_intro(1000,800,'a.jpg','posheshi.jpg',white,'freesansbold.ttf',70,20,'Back to Home',0,0,200,60,green,bright_green,'Integumentary system',800,600,600,650,400,0)
            
            elif action == 'Nervous system':
                click_intro(1000,800,'a.jpg','asabi.jpg',white,'freesansbold.ttf',70,20,'Back to Home',0,0,200,60,green,bright_green,'Nervous system',800,600,600,650,400,0)
            
            elif action == 'The lungs':
                click_intro(1000,800,'a.jpg','shosh.jpg',white,'freesansbold.ttf',70,20,'Back to Home',0,0,200,60,green,bright_green,'The lungs',800,600,600,650,400,0)
            
            elif action == 'Stomach':
                click_intro(1525,800,'a.jpg','mede.jpg',white,'freesansbold.ttf',70,20,'Back to Home',0,0,200,60,green,bright_green,'Stomach',800,600,600,780,920,0)
            
            elif action == 'Endocrine system':
                click_intro(1000,800,'a.jpg','daron.jpg',white,'freesansbold.ttf',70,20,'Back to Home',0,0,200,60,green,bright_green,'Endocrine system',800,600,600,650,400,0)
            
            elif action == 'Urinary tract':
                click_intro(1000,800,'a.jpg','edr.jpg',white,'freesansbold.ttf',70,20,'Back to Home',0,0,200,60,green,bright_green,'Urinary tract',800,600,600,600,400,0)
  
    
    else:
        pygame.draw.rect(gameDisplay,ic,(x,y,w,h))

    smallText = pygame.font.Font("freesansbold.ttf",20)
    TextSurf,TextRect = text_objects(msg,smallText,black)
    TextRect.center = ((x+(w/2)),(y + (h/2)))
    gameDisplay.blit(TextSurf,TextRect)  

def welcom ():
    message_display('Welcom',"freesansbold.ttf")

def click_intro(x,y,image,image_back,color,font,size,text_size,button_text,button_x,button_y,button_h,button_w,actcolor,inactcolor,string,TextRect_h,TextRect_w,image_x,image_y,image_h,image_w,text_1 = None):
    pygame.mixer.music.load('musica.ogg')
    pygame.mixer.music.play(-1)
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        game_Display = pygame.display.set_mode((x,y))
        game_Display.fill(color)
        iconimage = pygame.image.load(image)
        load_image(image_back,image_x,image_y,image_h,image_w)

        if string == 'digestive system':
            load_image('IMG.jpg',400,350,0,460)
            load_image('govaresh.png',600,700,400,0)
            button('Mouth and Esophagus',400,700,300,55,purple_br,purple,'Mouth and Esophagus')
            button('Stomach',700,700,300,55,yellow_br,yellow,'Stomach')

        elif string == 'Mouth and Esophagus':
            load_image('dahan.jpg',600,800,925,0)
            load_image('dahana.jpg',525,525,400,0)
            load_image('mouse_d.png',340,400,0,460)  
            load_image('dahanb.jpg',400,400,0,60)

        elif string == 'Respiratory System':
            load_image('tanafous.jpg',400,385,0,415)
            load_image('tannafos.jpg',400,355,0,60)
            button('The lungs',550,700,300,55,purple_br,purple,'The lungs')
            
        elif string == 'Lymphatic system':
            load_image('xx.jpg',400,385,0,415)
            load_image('ww.jpg',400,355,0,60) 
            
        elif string == 'circulatory system':
            load_image('gardesh_a.jpg',800,800,-100,0)
            
        elif string == 'Menu':
            button('digestive system',90,370,200,50,red,bright_red,'digestive system')
            button('Muscular device',110,520,200,50,Mycolor_sorati_br,Mycolor_sorati,'Muscular device')
            button('Lymphatic system',90,270,200,50,Mycolor_x_br,Mycolor_x,'Lymphatic system')
            button('Respiratory System',145,170,200,50,yellow_br,yellow,'Respiratory System')
            button('Integumentary order',110,670,200,50,Mycolor_b_br,Mycolor_b,'Integumentary system')
            button('circulatory system',770,290,200,50,light_blue_br,light_blue,'circulatory system')
            button('Urinary tract',770,400,200,50,Mycolor_c_br,Mycolor_c,'Urinary tract')
            button('reproductive system',770,450,200,50,Mycolor_f_br,Mycolor_f,'reproductive system')
            button('Skeletal device',770,575,200,50,orange_br,orange,'Skeletal device')
            button('Nervous system',680,55,200,50,purple_br,purple,'Nervous system')
            load_image('eme.jpg',299,168,1500-299,0)
            button('Immune system',1500-200,168,200,60,Mycolor_d_br,Mycolor_d,'Immune system')
            load_image('ho.jpg',301,196,1199,800-196)
            button('Endocrine system',1300,800-256,200,60,Mycolor_e_br,Mycolor_e,'Endocrine system')
        elif string == 'about us':
            load_image('about_a.jpg',500,400,920,10)
            load_image('mmm.png',800,600,10,80)
        elif string == 'Muscular device':
            load_image('mahichea.jpg',400,400,0,60)
            load_image('muscleq.jpg',400,350,0,460)
            
        elif string == 'Immune system':
            load_image('wq.png',400,400,0,60)
            load_image('er.jpg',400,350,0,460)
            
        elif string == 'Integumentary system':
            load_image('post.jpg',400,400,0,60)
            load_image('poost.jpg',400,350,0,460)
            
        elif string == 'Nervous system':
            load_image('assabi.jpg',400,400,0,60)
            load_image('asaabi.jpg',400,350,0,460)
            
        elif string == 'Skeletal device':
            load_image('eskel.jpg',400,340,0,460)
            load_image('eeskle.jpg',400,400,0,60)
            
        elif string == 'reproductive system':
            load_image('taanasol.jpg',400,400,0,60)
            load_image('tanaso.jpg',400,340,0,460)
            
        elif string == 'Stomach':
            load_image('medea.jpg',530,300,400,0)
            load_image('meede.jpg',400,370,0,60)
            load_image('mmede.jpg',400,370,0,460)
            load_image('meedee.jpg',530,300,400,300)
            load_image('ess.jpg',265,200,400,600)
            load_image('es.jpg',265,200,665,600)
        elif string == 'Endocrine system':
            load_image('darron.jpg',400,400,0,60)
            load_image('daaaron.jpg',400,340,0,460)
            
        elif string == 'Urinary tract':
            load_image('edra.jpg',400,400,0,60)
            load_image('edraaa.jpg',400,340,0,460)
            
        elif string == 'The lungs':
            load_image('re.jpg',400,400,0,60)
            load_image('ree.jpg',400,340,0,460)

        pygame.display.set_icon(iconimage)
        pygame.display.set_caption(string)
        button(button_text,button_x,button_y,button_h,button_w,actcolor,inactcolor,button_text)
        button('Quit',200,0,200,60,red,bright_red,'quit')
        largeText = pygame.font.Font(font,size)
        TextSurf, TextRect = text_objects(text_1,largeText,black)
        TextRect.center = ((TextRect_h/2),TextRect_w/2)
        message_display_intro(text_1,font,text_size,0,470,black)
        pygame.display.update()
        gameDisplay.blit(TextSurf,TextRect)  
def text_objects(text,font,color):
    textSurface = font.render(text,True,color)
    return textSurface, textSurface.get_rect()

def message_display(text,font,size,x,y):
    largeText = pygame.font.Font(font,size)
    TextSurf, TextRect = text_objects(text,largeText,black)
    TextRect.center = (x,y)
    gameDisplay.blit(TextSurf,TextRect)
    pygame.display.update()
    time.sleep(2)
    game_loop()
    return()

def message_display_intro(text,font,size,x,y,color):
    largeText = pygame.font.Font(font,size)
    TextSurf, TextRect = text_objects(text,largeText,color)
    TextRect.center = (x,y)
    gameDisplay.blit(TextSurf,TextRect)
    pygame.display.update()
    return()

def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(Mycolor)
        load_image('aa.jpg',800,800,0,0)
        largeText = pygame.font.Font('freesansbold.ttf',50)
        TextSurf, TextRect = text_objects('Welcome to the Biology App',largeText,black)
        TextRect.center = ((display_width/2),display_height/2)
        gameDisplay.blit(TextSurf,TextRect)
        button('Start',150,450,100,50,green,bright_green,'play')
        button('Quit',550,450,100,50,red,bright_red,'quit')
        button('about us',250,550,100,50,yellow_br,yellow,'about us')
        button('Help',450,550,100,50,blue,bright_blue,'Help')
        pygame.display.update()
        
def sound (text):
    sound = pyttsx3.init()
    sound.setProperty('rate' , 110)
    sound.say(text)
    sound.runAndWait()
    return ()

def load_image(img,x,y,h,w):
    bioImage = pygame.image.load(img)
    BioImage = pygame.transform.scale(bioImage,(x,y))
    gameDisplay.blit(BioImage,(h,w))
    return()

def game_loop():
    x=(display_height*0.45)
    y=(display_height*0.6)
    gameDisplay = pygame.display.set_mode((display_width,display_width))
    pygame.mixer.music.load('ss.mp3')
    pygame.mixer.music.play(-1)
    
    exit = False

    while not exit:
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                exit = True
        gameDisplay.fill(white)
        load_image('badan.jpg',600,720,200,80)

        button('Menu',0,0,100,80,blue,bright_blue,'Menu')
        button('digestive system',0,80,200,60,green,bright_green,'digestive system')
        button('Respiratory System',0,140,200,60,yellow_br,yellow,'Respiratory System')
        button('Nervous system',0,200,200,60,purple_br,purple,'Nervous system')
        button('circulatory system',0,260,200,60,light_blue_br,light_blue,'circulatory system')
        button('Muscular device',0,320,200,60,Mycolor_sorati_br,Mycolor_sorati,'Muscular device')
        button('Lymphatic system',0,380,200,60,Mycolor_x_br,Mycolor_x,'Lymphatic system')
        button('Skeletal device',0,440,200,60,orange_br,orange,'Skeletal device')
        button('Integumentary order',0,500,200,60,Mycolor_b_br,Mycolor_b,'Integumentary system')
        button('Urinary tract',0,560,200,60,Mycolor_c_br,Mycolor_c,'Urinary tract')
        button('Immune system',0,620,200,60,Mycolor_d_br,Mycolor_d,'Immune system')
        button('Endocrine system',0,680,200,60,Mycolor_e_br,Mycolor_e,'Endocrine system')
        button('Genreproductive',0,740,200,60,Mycolor_f_br,Mycolor_f,'reproductive system')
        button('Quit',700,0,100,80,red,bright_red,'quit')

        pygame.display.update()
        clock.tick(120)
game_intro()
game_loop()

pygame.quit()
quit()

