import pyglet
from pyglet.window import Window, key
from pyglet.shapes import Triangle, Line, Star, Circle
from pyglet.app import run
from pyglet.graphics import Batch
import numpy as np
import random
import time
import sys

WIDTH = 1300
HEIGHT = 700
WINDOW_TITLE = 'Tarea 1 - Naves y Estrellas'
FULL_SCREEN = False
ventana = Window(WIDTH, HEIGHT, WINDOW_TITLE, resizable=True)
batch = Batch()
star = Batch()
meteoro = Batch()
estrellas = []
meteors = []

class Estrella:
    def __init__(self, x, y):
        self.random = random.randint(1,3)
        self.body = Star(x , y, outer_radius= self.random, inner_radius=self.random, 
                         num_spikes=5, color=(255, 255, 255), batch=star)
    def update(self):
        self.body.y -= self.random

#Definimos la clase Planeta
class Planeta:
    def __init__(self, x, y):
        self.body = Circle(x , y, radius= random.randint(0,200),
                          color=(random.randint(0,255), random.randint(0,255), random.randint(0,255),255), batch=star)
        self.vy = random.randint(3,10)
    def update(self):
        self.body.y -= self.vy

#Generamos unas estrellas iniciales
for i in range(300): 
        estrellas.append(Estrella(random.randint(0, WIDTH), random.randint(0, HEIGHT)))

#Definimos la clase meteorito
class Meteorito:
    def __init__(self, x, y):
        self.body = (Circle(x, y, radius=50, color=(90, 90, 90), batch=meteoro),
                     Circle(x+20, y-20, radius=15, color=(0,0,0,255), batch=meteoro),
                     Circle(x-20, y+20, radius=15, color=(0,0,0,255), batch=meteoro),
                     Circle(x-20, y-20, radius=10, color=(0,0,0,255), batch=meteoro),
                     Circle(x+20, y+20, radius=10, color=(0,0,0,255), batch=meteoro))
        self.vx = random.randint(-5,5)
        self.vy = random.randint(5,10)
    def update(self):
        for shape in self.body:
            shape.x += self.vx
            shape.y -= self.vy

class Nave:
    def __init__(self, x, y):
        self.body = (Triangle(x-25, y-25, x+25, y-25, x, y+50,
                            color=(255, 255, 255, 255), batch=batch),
                    Triangle(x-25, y-25, x+25, y-25, x, y-50,
                            color=(255, 255, 255, 255), batch=batch),
                    Line(x, y-50, x, y+49, width=1,
                            color=(0, 0, 0, 255), batch=batch),
                    Triangle(x-10, y-25, x+10, y-25, x, y,
                            color=(255, 0, 0, 255), batch=batch),
                    Triangle(x-10, y-25, x+10, y-25, x, y-37,
                            color=(255, 0, 0, 255), batch=batch),
                    Triangle(x+25, y-37, x+25, y-12, x+75, y-62,
                            color=(255, 255, 255, 255), batch=batch),
                    Triangle(x-25, y-37, x-25, y-12, x-75, y-62,
                            color=(255, 255, 255, 255), batch=batch),
                    Triangle(x-35, y-25, x-15, y-25, x-25, y+12,
                            color=(0, 0, 255, 255), batch=batch),
                    Triangle(x-35, y-25, x-15, y-25, x-25, y-37,
                            color=(0, 0, 255, 255), batch=batch),
                    Triangle(x+35, y-25, x+15, y-25, x+25, y+12,
                            color=(0, 0, 255, 255), batch=batch),
                    Triangle(x+35, y-25, x+15, y-25, x+25, y-37,
                            color=(0, 0, 255, 255), batch=batch))
        self.advance = 0
        self.rotate = 0
    def update(self):
        for shape in self.body:
            shape.x += 15*self.rotate
            shape.y += 10*self.advance

naves = [Nave(ventana.width // 2 - 200, ventana.height // 2 - 100), Nave(ventana.width // 2, ventana.height // 2), Nave(ventana.width // 2 + 200, ventana.height // 2 - 100)]

player = pyglet.media.Player()
music = pyglet.media.load('musica.mp3')
player.queue(music)
player.play()


@ventana.event
def on_key_press(symbol, modifiers):
    for i in naves:
        if symbol == pyglet.window.key.W:
            i.advance = 1
        elif symbol == pyglet.window.key.S:
            i.advance = -1
        elif symbol == pyglet.window.key.A:
            i.rotate = -1
        elif symbol == pyglet.window.key.D:
            i.rotate = 1

@ventana.event
def on_key_release(symbol, modifiers):
    for i in naves:
        if symbol == pyglet.window.key.W:
            i.advance = 0
        elif symbol == pyglet.window.key.S:
            i.advance = 0
        elif symbol == pyglet.window.key.A:
            i.rotate = 0
        elif symbol == pyglet.window.key.D:
            i.rotate = 0

count = 0
label = pyglet.text.Label("Count: " + str(count), font_name='Monocraft', font_size=20,
                          x=100, y=ventana.height - 100,
                          anchor_x='center', anchor_y='center',
                          color=(255,255,255,255))
label2 = pyglet.text.Label("Martín E. Bravo @UChile ", font_name='Monocraft', font_size=20,
                          x=ventana.width-250, y=ventana.height - 100,
                          anchor_x='center', anchor_y='center',
                          color=(255,255,255,255))
label3 = pyglet.text.Label("GAME OVER ", font_name='Monocraft', font_size=50,
                          x=ventana.width // 2, y=ventana.height // 2,
                          anchor_x='center', anchor_y='center',
                          color=(255,255,255,255))
last_meteor_time = time.time()
last_planet_time = time.time()

@ventana.event
def on_draw():
    global last_meteor_time
    global last_planet_time
    global count
    ventana.clear()
    estrellas.append(Estrella(random.randint(0, ventana.width), ventana.height+100))
    if time.time() - last_meteor_time > 0.2:
        meteors.append(Meteorito(random.randint(0, ventana.width), ventana.height+100))
        last_meteor_time = time.time()
    if time.time() - last_planet_time > 2.0:
        estrellas.append(Planeta(random.randint(0, ventana.width), ventana.height+200))
        last_planet_time = time.time()
    global count
    for i in estrellas:
        i.update()
        if i.body.y < -200:
            estrellas.remove(i)
    for i in meteors:
        i.update()
        for shape in i.body:
            if shape.y < -50 or shape.x < -50 or shape.x > WIDTH + 50:
                if i in meteors:
                    meteors.remove(i)
                    if len(naves) != 0:
                        count += 1
    for i in naves:
        i.update()
    for nave in naves:
        for shape in nave.body:
            for meteorito in meteors:
                for shape2 in meteorito.body:
                    if ((shape.x - shape2.x)**2) + ((shape.y - shape2.y)**2) <= 25**2:
                        if nave in naves:
                            naves.remove(nave)
                    if shape.x < -100 or shape.x > WIDTH + 100 or shape.y < -100 or shape.y > HEIGHT + 100:
                        if nave in naves:
                            naves.remove(nave)
    star.draw()
    batch.draw()
    meteoro.draw()
    label.text = "Count: " + str(count)
    label.draw()
    label2.text = "Martín E. Bravo @UCH "
    label2.draw()
    if len(naves) == 0:
        label3.text = "GAME OVER "
        label3.draw()

run()