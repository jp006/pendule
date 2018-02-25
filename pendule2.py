from tkinter import *
from numpy import cos, sin, pi
from time import sleep
from scipy.integrate import odeint
import numpy as np
        
#variables    
height = 400
width = 400
flag=1
lg=1
i=0
g = 9.8

def draw_line(x1,y1,x2,y2,color):
   can1.create_line(x1,y1,x2,y2,fill=color)
   can1.create_oval(x2-5,y2-5,x2+5,y2+5, outline=color, fill=color, width=2)

def stop():
    global flag 
    if flag == 0:    
      flag =1
    else:
      flag =0

def exit():
    quit()
    
def change_lg(event):
  global lg
  lg = float(eval(entree.get()))
    
    
    
def play(posx,posy,i):

   draw_line(width/2,0,posx,posy,'white')
   i=i+1
   posx = (width/2) - (x[i]* (width/2))
   posy = abs(y[i]*(height/2))
   draw_line(width/2,0,posx,posy,'black')
   if (i < len(x)-1) :
     fen1.after(100,play,posx,posy,i)
 
 
   
#   if i < 360 :
#       if flag==1:
#         i=i+4
#       #time.sleep(0.1)
#       fen1.after(int(200*sqrt(lg)),play,posx,posy,i)
#   else:
#       fen1.after(int(200*sqrt(lg)),play,posx,posy,0)
      

L = 1

def derivs(state, t):
    
    res = np.zeros_like(state) # theta omega
    
    res[0] = state[1] 
    res[1] = -g/L*sin(state[0])

    return res

###############################################################################

# Time range
dt = 0.033
t = np.arange(0.0, 100, dt)

# initial state
th = 90*pi/180
omega = 0
state = [th, omega]

# integration
res = odeint(derivs, state, t)
x, y = L*sin(res[:, 0]), -L*cos(res[:, 0])      
          
  
#programme "principal" 
fen1 = Tk()


can1 = Canvas(fen1, width =width, height =height, bg ='white')
can1.pack(side =TOP, padx =5, pady =5)
b2 = Button(fen1, text ='Pause', command =stop)
b3 = Button(fen1, text ='Exit', command =exit)

#b2.pack(side =LEFT, padx =3, pady =3)
b3.pack(side =LEFT, padx =3, pady =3)

entree = Entry(fen1)
entree.bind("<Return>", change_lg)
#entree.pack(side =RIGHT)
chaine = Label(fen1)
chaine.configure(text = "longueur de la corde (entre 0 et 1) :")
#chaine.pack(side =RIGHT)

can1.pack()
#draw_line(width/2,0,posx,posy)
  
posx=0
posy=0  
fen1.after(100,play,0,0,0)
fen1.mainloop()


