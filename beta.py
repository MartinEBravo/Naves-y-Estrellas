import pyglet
from pyglet.window import Window, key
from pyglet.shapes import Triangle, Line, Star
from pyglet.app import run
from pyglet.graphics import Batch
import numpy as np
import random
import time

WIDTH = 1000
HEIGHT = 700
WINDOW_TITLE = 'Tarea 1 - Naves y Estrellas'
FULL_SCREEN = False
ventana = Window(WIDTH, HEIGHT, WINDOW_TITLE, resizable=True)
batch = Batch()
star = Batch()

estrellas = []

class Estrella:
    def __init__(self, x, y):
        self.body = Star(x , y, outer_radius= 2, inner_radius=1, 
                         num_spikes=5, color=(255, 255, 255), batch=star)
    def update(self):
        self.body.y -= 10

class Nave:
    def __init__(self, x, y):
        self.Cuerpo1 = Triangle(x-25, y-25, x+25, y-25, x, y+50,
                                color=(255, 255, 255, 255), batch=batch)
        self.Cuerpo2 = Triangle(x-25, y-25, x+25, y-25, x, y-50,
                                color=(255, 255, 255, 255), batch=batch)
        self.Linea = Line(x, y-50, x, y+49, width=2,
                          color=(0, 0, 0, 255), batch=batch)
        self.Ventana1 = Triangle(x-10, y-25, x+10, y-25, x, y,
                                 color=(255, 0, 0, 255), batch=batch)
        self.Ventana2 = Triangle(x-10, y-25, x+10, y-25, x, y-37,
                                 color=(255, 0, 0, 255), batch=batch)
        self.AlaIzquierda = Triangle(x+25, y-37, x+25, y-12, x+75, y-62,
                                     color=(255, 255, 255, 255), batch=batch)
        self.AlaDerecha = Triangle(x-25, y-37, x-25, y-12, x-75, y-62,
                                   color=(255, 255, 255, 255), batch=batch)
        self.PropulsorIzquierdo1 = Triangle(x-35, y-25, x-15, y-25, x-25, y+12,
                                            color=(0, 0, 255, 255), batch=batch)
        self.PropulsorIzquierdo2 = Triangle(x-35, y-25, x-15, y-25, x-25, y-37,
                                            color=(0, 0, 255, 255), batch=batch)
        self.PropulsorDerecho1 = Triangle(x+35, y-25, x+15, y-25, x+25, y+12,
                                          color=(0, 0, 255, 255), batch=batch)
        self.PropulsorDerecho2 = Triangle(x+35, y-25, x+15, y-25, x+25, y-37,
                                          color=(0, 0, 255, 255), batch=batch)


nave_lider = Nave(500, 300)
nave_derecha = Nave(300, 200)
nave_izquierda = Nave(700, 200)

@ventana.event
def on_draw():
    ventana.clear()
    estrellas.append(Estrella(random.randint(0, ventana.width), 700))
    for i in estrellas:
        i.update()
        star.draw()
        if i.body.y < 0:
            estrellas.remove(i)
    batch.draw()
    



run()
