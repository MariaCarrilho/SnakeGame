import pygame 
import time
import random
# CONSTANTS:
WIDTH =600
HEIGHT = 600
BLACK = (0, 0, 0)
GREY = (160, 160, 160)
WHITE = (255,255,255)
blockSize = 30
start = 120
points = 0
nlevel=1
x = 135
y = 160
food = 0
gameOver = False
direction = 0

pygame.init()
dis = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption('Snake Game by MariaJosezinha')
clock = pygame.time.Clock()
image_snake = [pygame.image.load("Snake\\Left.jpg").convert(), pygame.image.load("Snake\\Down.jpg").convert(), pygame.image.load("Snake\\Right.jpg").convert(),pygame.image.load("Snake\\Up.jpg").convert() ]
fruit_images = [pygame.image.load("Fruits\\apple.jpg").convert(),pygame.image.load("Fruits\\cherry.jpg").convert(), pygame.image.load("Fruits\\kiwi.jpg").convert(), pygame.image.load("Fruits\\orange.jpg").convert(),pygame.image.load("Fruits\\strawberry.jpg").convert(),pygame.image.load("Fruits\\tomato.jpg").convert()]

while not gameOver:
    start -= 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT: gameOver=True
        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == ord('w'):
                if direction == 0 or direction == 2: direction = 3
            
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                if direction == 1 or direction == 3: direction = 0
            
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                if direction == 0 or direction == 2: direction = 1
            
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                if direction == 1 or direction ==3:  direction = 2
            print(direction)

    if start<=0: gameOver=True
    
    if direction == 0: 
        x-=blockSize
        finalSnake = pygame.transform.scale(image_snake[direction], (34,34))

    elif direction == 1: 
        y += blockSize
        finalSnake = pygame.transform.scale(image_snake[direction], (34,34))
    elif direction==2: 
        x+=blockSize
        finalSnake = pygame.transform.scale(image_snake[direction], (34,34))
    elif direction == 3: 
        y-=blockSize
        finalSnake = pygame.transform.scale(image_snake[direction], (34,34))

    dis.fill(BLACK)

    if food ==0:
      r1=random.randint(0,5)
      rLinha = random.randint(1,15)
      rCol = random.randint(1, 15)
      finalFruit = pygame.transform.scale(fruit_images[r1], (34, 34))
      food = 1

    posX = 45+30*rCol
    posY = 70+30*rLinha
    dis.blit(finalFruit, (posX, posY))
    dis.blit(finalSnake,(x, y))

    print("X "+ str(x))
    print("Y" + str(y))
    print("Fruta x" + str(posX))
    print("Fruta y" + str(posY))

    if x == posX and y == posY: 
        food = 0
        points +=blockSize
        start+=blockSize

    if x <= 50 or y <= 75 or y>=550 or x>=550: gameOver=True

    level = "Level " + str(nlevel)
    pygame.draw.rect(dis, WHITE, pygame.Rect(50, 10, 510,55),2)
    font = pygame.font.Font('Peach Days.ttf', 18)
    timer = font.render(str(start), True, WHITE, BLACK)
    timerRect = timer.get_rect()
    timerRect.center = (470, 25)
    dis.blit(timer, timerRect)

    text = font.render(level, True, WHITE, BLACK)
    textRect = text.get_rect()
    textRect.center = (85,25)
    dis.blit(text, textRect)

    score = "Score: " + str(points)
    Score = font.render(score, True, WHITE, BLACK)
    scoreRect = Score.get_rect()
    scoreRect.center = (90, 45)
    dis.blit(Score, scoreRect)
    
    for Gx in range(50, WIDTH-50, blockSize):
       for Gy in range(75, HEIGHT-50, blockSize):
           rect = pygame.Rect(Gx, Gy, blockSize, blockSize)
           pygame.draw.rect(dis, GREY, rect, 1)     

    pygame.display.update()
    clock.tick(1)
pygame.display.update()
time.sleep(2)
pygame.quit()