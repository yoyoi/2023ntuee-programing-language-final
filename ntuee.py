import sys
import random
import pygame

pygame.init()

width, height = 640, 480
screen = pygame.display.set_mode((width, height))

pygame.display.set_caption('ntuee')

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

font = pygame.font.Font(None, 74)

def get_random_letter():
    return chr(random.randint(65, 90))

def random_position_and_speed():
    return [random.randint(50, width-50), random.randint(50, height-50), random.randint(-2, 2), random.randint(-2, 2)]

num_letters = 10  
letters = [[get_random_letter(), random_position_and_speed()] for _ in range(num_letters)]

def reset_game():
    global letters
    letters = [[get_random_letter(), random_position_and_speed()] for _ in range(num_letters)]
    return False, False

game_over, waiting_for_restart = reset_game()

point=0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if game_over and event.key == pygame.K_SPACE:
                point=0
                game_over, waiting_for_restart = reset_game()
            elif not game_over:
                pressed_letter = event.unicode.upper()
                for i, (l, _) in enumerate(letters):
                    if l == pressed_letter:
                        letters[i] = [get_random_letter(), random_position_and_speed()]
                        point+=1
                        break
                else:
                    game_over = True

    screen.fill(black)
    
    point_text=font.render(f'Point:{point}',True,white)

    screen.blit(point_text,(0,0))

    for letter in letters:
        text = font.render(letter[0], True, white)
        screen.blit(text, (letter[1][0], letter[1][1]))

        letter[1][0] += letter[1][2]
        letter[1][1] += letter[1][3]

        if letter[1][0] <= 0 or letter[1][0] >= width - text.get_width():
            letter[1][2] *= -1
        if letter[1][1] <= 0 or letter[1][1] >= height - text.get_height():
            letter[1][3] *= -1

    if game_over:
        restart_text = font.render('Game Over! Press Space to Restart', True, red)
        screen.blit(restart_text, (width // 2 - restart_text.get_width() // 2, height // 4))

    pygame.display.flip()

    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()
