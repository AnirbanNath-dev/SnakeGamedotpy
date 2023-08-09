import pygame 
import random
import os

pygame.mixer.init()


pygame.init()


white = (255,255,255)
red = (255,0,0)
black = (0,0,0)

game_width = 700
game_height = 600

pygame.display.set_caption('Snake Game')
gameWindow = pygame.display.set_mode((game_width, game_height))



clock = pygame.time.Clock()
font = pygame.font.SysFont(None , 45)
def text_screen(text , color , x, y):
    screen_text = font.render(text , True , color)
    gameWindow.blit(screen_text , [x, y])


def plot_snake(Window , color , list , size):
    for x, y in list:
        # print(list)
        pygame.draw.rect(Window , color , [x ,  y , size , size ]) 


def welcome_screen():
    exit_game = False
    while not exit_game:
        gameWindow.fill((223, 245, 237))
        text_screen('Welcome to Snake Game', (61, 100, 255) , 150,280)
        text_screen('Press space to continue', (61, 100, 255) , 160,330)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # pygame.mixer.music.load('')
                    # pygame.mixer.music.play()

                    gameloop()

        pygame.display.update()
        clock.tick(60)

def gameloop():

    if not os.path.exists('highscore.txt'):
        with open('highscore.txt' , 'w') as f:
            f.write('0')

    with open('highscore.txt', 'r') as f:
        highscore = f.read()
    score = 0
    exit_game = False
    game_over =False
    snake_x = 100
    snake_y = 100
    snake_size = 17
    move_x = 0
    move_y = 0
    fps = 20
    food_x = random.randint(20,game_width/2)
    food_y = random.randint(20,game_height/2)
    init_vel = 10
    velocity_x = 0
    velocity_y = 0
    snake_list = []
    snake_length = 1
    while not exit_game:

        if game_over:
            with open('highscore.txt', 'w') as f:
                f.write(str(highscore))
            gameWindow.fill(white)
            text_screen('Game Over! Press space to continue' ,red ,70,game_height/2 )
            

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        gameloop()
            
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if move_x == 0:
                        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                            velocity_x = init_vel
                            velocity_y = 0
                            move_x = 1
                            move_y = 0
                    
                        if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                            velocity_x = -init_vel
                            velocity_y = 0
                            move_x = 1
                            move_y = 0
                    if move_y == 0:
                        if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                            velocity_x = 0
                            velocity_y = init_vel
                            move_x = 0
                            move_y = 1
                        if event.key == pygame.K_UP or event.key == pygame.K_w:
                            velocity_x = 0
                            velocity_y = -init_vel
                            move_x = 0
                            move_y = 1

            if abs(snake_x - food_x) < 15 and abs(snake_y - food_y) <15:
                pygame.mixer.music.load('eat.mp3')
                pygame.mixer.music.play()


                score += 10
                food_x = random.randint(20,round(game_width/1.5))
                food_y = random.randint(20,round(game_height/1.5))
                snake_length +=3

                if int(highscore) < score:
                    highscore = score

                    

            snake_x +=  velocity_x
            snake_y += velocity_y


            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            if len(snake_list) > snake_length:
                del snake_list[0]

            if head in snake_list[:-1]:
                pygame.mixer.music.load('gameover.mp3')
                pygame.mixer.music.play()

                game_over = True
            



            gameWindow.fill(white)
            plot_snake(gameWindow , black ,snake_list , snake_size)
            pygame.draw.rect(gameWindow , red , [food_x ,  food_y , snake_size , snake_size ])
            text_screen(f'Score : {score} Highscore : {highscore}' , red , 5,5)

            if snake_x<0 or snake_x>game_width or snake_y<0 or snake_y>game_height:
                pygame.mixer.music.load('gameover.mp3')
                pygame.mixer.music.play()

                game_over = True

        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
welcome_screen()
