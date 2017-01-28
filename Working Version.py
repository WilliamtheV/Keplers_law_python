import math
from math import *

G=6.673*10**(-11)
distance = 149600000000
mass2=5.972*10**24
s=1
import tkinter as tk

from tkinter import *

def period():
    period=((((4*(math.pi**2))/(G*((var.get()*1.989*(10**30))+mass2))) * distance**3)**(1/2))/(31540000)
    print(period)
    label.config(text=period)

def total_mass():
    mass_t=((4*(math.pi**2)/G) * ((var2.get()*1.496*(10**11)))**3)/((3.154*10**7)**2)/(1.99*(10**30))
    print(mass_t)
    label.config(text=mass_t)
    


kepler=tk.Tk()
root=kepler


var=tk.IntVar()
s=tk.Scale(kepler, from_=1, to=200, orient=HORIZONTAL, troughcolor='red', length=400, variable=var, label= 'Solar Masses',)
s.pack()
c = tk.Canvas()
c.output = tk.Label(c)
c.output.pack()
c.pack()
button = Button(root, text="The Orbital Period in Earth Years is:", command=period)
button.pack(anchor=CENTER)



var2=tk.IntVar()
s=tk.Scale(kepler, from_=1, to=200, orient=HORIZONTAL,troughcolor='yellow', length=400, variable=var2, label= 'Distance in Astronomical Units',)
s.pack()
d = tk.Canvas()
d.output = tk.Label(d)
d.output.pack()
d.pack()
button = Button(root, text="The total mass of the system (in solar masses) is", command=total_mass)
button.pack(anchor=CENTER)
label=Label(kepler)
label.pack()
kepler.mainloop()



