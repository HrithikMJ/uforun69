"https://github.com/HrithikMJ/uforun69"

import pgzrun
import random
import pygame
import os


TITLE = 'UFO RUN 69'
WIDTH = 400
HEIGHT = 708

GAP = 130
GRAVITY = 0.3
FLAP_STRENGTH = 6.5
SPEED = 3

ufo = Actor('ufo1', (75, 200))
ufo.dead = False
ufo.score = 0
ufo.vy = 0

def screen_clear():  #to clear screen
   # for mac and linux
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('cls')


def reset_pipes():
    pipe_gap_y = random.randint(200, HEIGHT - 200)
    pipe_top.pos = (WIDTH, pipe_gap_y - GAP // 2)
    pipe_bottom.pos = (WIDTH, pipe_gap_y + GAP // 2)


pipe_top = Actor('top', anchor=('left', 'bottom'))
pipe_bottom = Actor('bottom', anchor=('left', 'top'))
reset_pipes()  # Set initial pipe positions.


def update_pipes():
    pipe_top.left -= SPEED
    pipe_bottom.left -= SPEED
    if pipe_top.right < 0:
        reset_pipes()
        if not ufo.dead:
            ufo.score += 1




def update_ufo():
    uy = ufo.vy
    ufo.vy += GRAVITY
    ufo.y += (uy + ufo.vy) / 2
    ufo.x = 75

    if not ufo.dead:
        if ufo.vy < -3:
            ufo.image = 'ufo2'

        else:
            ufo.image = 'ufo1'


    if ufo.colliderect(pipe_top) or ufo.colliderect(pipe_bottom):
        ufo.dead = True
        ufo.image = 'ufo_die'
        music.stop()
        sounds.negative.play()
    

    if not 0 < ufo.y < 720:
        ufo.y = 200
        ufo.dead = False
        ufo.score = 0
        ufo.vy = 0
        reset_pipes()


def update():
    update_pipes()
    update_ufo()


def on_key_down():

      if not ufo.dead:
        ufo.vy = -FLAP_STRENGTH


def draw():
    pygame.mixer.init()
    if not music.is_playing('bgm') :
         music.play('bgm')
    screen.blit('background', (0, 0))
    pipe_top.draw()
    pipe_bottom.draw()
    ufo.draw()
    screen.draw.text(
        str(ufo.score),
        color='white',
        midtop=(WIDTH // 2, 10),
        fontsize=70,
        shadow=(1, 1)
    )
kint=input("press space bar to continue or anyother key to exit")
if kint==' ' or kint=='  ':
  pgzrun.go()
screen_clear()
print("\033[95m"+"\033[1m" + "\n\nCongratulations "+"\033[4m"+"\033[1m"+"\033[0m" +" on scoring "+"\033[0m"+"\033[4m"+"\033[1m"+str(ufo.score)+"\033[0m"  )
