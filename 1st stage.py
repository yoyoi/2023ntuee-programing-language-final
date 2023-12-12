import sys
import pygame
import random

pygame.init()

width, height=600,600
screen=pygame.display.set_mode((width,height))

pygame.display.set_caption('1st stage')

black=(0,0,0)
white=(255,255,255)
red=(255,0,0)

font=pygame.font.Font(None,30)

target_width=30
target_height=30
def get_position_speed():
    p1=random.randint(target_width,width)
    p2=random.randint(target_height,height)
    if p1>=width//2 and p2<=height//2:
        return[p1,p2,(width//2+5-p1)//50,(height//2+15-p2)//50]
    elif p1<width//2 and p2>height//2:
        return[p1,p2,(width//2+25-p1)//50,(height//2+25-p2)//50]
    elif p1>=width//2 and p2>height//2:
        return[p1,p2,(width//2+5-p1)//50,(height//2+25-p2)//50]
    elif p1<width//2 and p2<=height//2:
        return[p1,p2,(width//2+25-p1)//50,(height//2+15-p2)//50]
position_speed=get_position_speed()

running=True
for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_s:
            waiting=False
            running=True

point=5

def reset_game():
    global point
    global position_speed
    position_speed=get_position_speed()
    point=5
    return False

game_over=reset_game()

operation_text=font.render('Press space to shoot',True,white)

while running:
    screen.fill(black)
    screen.blit(operation_text,(0,0))
    point_text=font.render(f'Point:{point}',True,white)
    
    pygame.draw.rect(screen,white,(width//2-25,height//2-25,50,50),1)
    
    pygame.draw.rect(screen,(0,0,255),(position_speed[0]-15,position_speed[1]-15,target_width,target_height),0)
    position_speed[0]+=position_speed[2]
    position_speed[1]+=position_speed[3]

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        
        elif event.type==pygame.KEYDOWN:
            if game_over and event.key==pygame.K_r:
                game_over=reset_game()
            
            elif not game_over:
                if event.key==pygame.K_SPACE:
                    if position_speed[0] >= width//2 - target_width and position_speed[0]<= width//2 +target_width and position_speed[1] <=height//2 + target_height and position_speed[1]>=height//2-target_height:
                        point+=1
                        if point==10:
                            position_speed[2], position_speed[3]=0, 0
                            game_over=True
                        else:
                            position_speed=get_position_speed()
                    else:
                        point-=1
                        if point<=0:
                            position_speed[2], position_speed[3]=0, 0
                            game_over=True
                        else:
                            position_speed=get_position_speed()
    
    if  position_speed[1]>=height or position_speed[1]<=0 or position_speed[0]>=width or position_speed[0]<=0:
        point-=1
        if point<=0:
            game_over=True
            position_speed[2], position_speed[3]=0, 0
        else:
            position_speed=get_position_speed()

    screen.blit(point_text,(width//1.5,0))

    if game_over and point==10:
        restart1_text = font.render('You Win! Press R to Restart', True,(0,255,0))
        screen.blit(restart1_text, (width //4, height //5))
        win_text= font.render('Good!',True,(0,255,0))
        screen.blit(win_text,(width//2.25,height/1.5))
    elif game_over and point<=0:
        point=0
        restart2_text = font.render('Game Over! Press R to Restart', True, red)
        screen.blit(restart2_text, (width //4, height //5))
        lose_text= font.render('Bad!',True,red)
        screen.blit(lose_text,(width//2.15,height/1.5))
        
     

    pygame.display.flip()

    pygame.time.Clock().tick(60)





pygame.quit()
sys.exit()