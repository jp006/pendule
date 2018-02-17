from tkinter import *
from math import *
from time import sleep
        
#variables    
height = 400
width = 400
flag=1
lg=1
i=0

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
   posx = (width/2) - (cos(radians(i))* width*lg/2)
   posy = abs((sin(radians(i)))*(height*lg/2))
   draw_line(width/2,0,posx,posy,'black')
  
   
   if i < 360 :
       if flag==1:
         i=i+4
       #time.sleep(0.1)
       fen1.after(int(200*sqrt(lg)),play,posx,posy,i)
   else:
       fen1.after(int(200*sqrt(lg)),play,posx,posy,0)
      
    
          
  
#programme "principal" 
fen1 = Tk()


can1 = Canvas(fen1, width =width, height =height, bg ='white')
can1.pack(side =TOP, padx =5, pady =5)
b2 = Button(fen1, text ='Pause', command =stop)
b3 = Button(fen1, text ='Exit', command =exit)

b2.pack(side =LEFT, padx =3, pady =3)
b3.pack(side =LEFT, padx =3, pady =3)

entree = Entry(fen1)
entree.bind("<Return>", change_lg)
entree.pack(side =RIGHT)
chaine = Label(fen1)
chaine.configure(text = "longueur de la corde (entre 0 et 1) :")
chaine.pack(side =RIGHT)

can1.pack()
#draw_line(width/2,0,posx,posy)
  
posx=0
posy=0  
fen1.after(100,play,0,0,0)
fen1.mainloop()


