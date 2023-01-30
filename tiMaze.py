from ti_system import *
from ti_draw import *
from random import *
from time import *

def key():
  loop = True
  while loop:
    vkey = get_key()
    if vkey:
      loop = False
      return vkey

def mp(d, f):
  global pposx
  global pposy
  check=checkPPos()
  d = int(d)
  clear_rect(pposx,pposy,6,6)
  if d == 2:
    pposy += 5
    draw_rect(pposx,pposy,5,5)
  elif d == 8:
    if check:
      pposy -= 5
    draw_rect(pposx,pposy,5,5)
  elif d == 4:
    pposx -= 5
    draw_rect(pposx,pposy,5,5)
  elif d == 6:
    pposx += 5
    draw_rect(pposx,pposy,5,5)

def genmaze(dif):
  n = 0
  while dif > n:
    m = 211/dif
    draw_line(0,n*m,320,n*m)
    n += 1
  n = 0
  while dif > n:
    y = n*m
    x=randrange(0,300)
    clear_rect(x,y,20,2)
    r = randrange(1,3,1)
    if r == 1:
      x1 = x+ 20
    else:
      x1 = x
    draw_line(x1,y,x1,y+m)
    r1 = randint(0,round(dif/10))
    while r1 != 2:
      y = n*m
      x=randrange(0,300)
      clear_rect(x,y,20,2)
      r = randrange(1,3,1)
      if r == 1:
        x1 = x+ 20
      else:
        x1 = x
      draw_line(x1,y,x1,y+m)
      r1 = randint(0,round(dif/10))
    n += 1
  return

def checkPPos():
  global pposx
  global pposy
  if pposx <= 0:
    clear_rect(pposx,pposy,6,6)
    pposx = 310
    draw_rect(pposx,pposy,6,6)
    return True
  elif pposx >= 320:
    clear_rect(pposx,pposy,6,6)
    pposx = 1
    draw_rect(pposx,pposy,6,6)
    return True
  if pposy <= 2:
    return False
  elif pposy >= 211:
    start(True)
  else:
    return True

def start(w):
  clear()
  if w:
    draw_text(160,105,"You Won")
    sleep(5)
    clear()
  draw_text(160,105,"Difficulty:")
  lk = True
  dif = 0
  while lk:
    k1 = key()
    print("k1 "+"= "+k1)
    k2 =key()
    print("k2 "+"= "+k2)
    dif = int(k1+k2)
    lk = False
    print(dif)
  clear()
  global pposx
  global pposy
  pposx = 1
  pposy = 2
  draw_rect(pposx,pposy,5,5)
  genmaze(dif)
  print("gen done")

start(False)
while get_key() != "esc":
  k=key()
  mp(k,False)
