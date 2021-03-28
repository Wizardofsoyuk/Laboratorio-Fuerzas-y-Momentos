import matplotlib.pyplot as plt
import numpy as np
"""

Esta parte del codigo son las cuerdas 3d

"""
beta = 30*(3.1415926535/180)


def Tcd(x):
    rad = x * (3.1415926535/180)
    f = (1.0806*9.8)/(np.sin(rad))
    return f

def Tcb (x):
    rad = x * (3.1415926535/180)
    tcd = Tcd(x)
    f = (-tcd*np.cos(rad))/(-2*np.cos(beta))
    return f
def Tac(x):
    f=Tcb(x)
    return(f)

rango = np.linspace(1,89,1000)
rango2 =[30,45,60,75]
tcd2=[22.19,17.43,13.93,10.51]

tcd = Tcd(rango)


plt.figure(1)
plt.plot(rango,tcd,"r",rango2,tcd2,"b")
plt.suptitle("Grados sexagesimales v. Fuerza[N] en la cadena CD")
plt.xlabel("Grados sexagesimales")
plt.ylabel("Fuerza de tensión en Tcd(N)")
plt.xlim([30,75])
plt.ylim([0,25])
plt.legend(["Datos teoricos","Datos experimentales"])
plt.show()

plt.figure(2)
plt.suptitle("Grados v. Fuerza[N] en la cadena CD (Teoricos)")
plt.xlabel("Grados sexagesimales")
plt.ylabel("Fuerza de tensión en Tcd(N)")
plt.plot(rango,tcd,"r")
plt.show()

"""
Esta parte del codigo son las cuerdas 2d
"""

def Tac2d(x):
    rad = x * (3.1415926535/180)
    f = (1.0806*9.8)/(np.sin(rad))
    return f

def Tab2d(x):
    rad = x * (3.1415926535/180)
    tac=Tac2d(x)
    f= tac * np.cos(rad)
    return f

def secante(x):
    rad = x * (3.1415926535/180)
    return (1/np.cos(rad))


resultado30= 20.13/(20.13*np.cos(np.deg2rad(30)))
resultado45= 14.52/(14.52*np.cos(np.deg2rad(45)))
resultado60= 12.12/(12.12*np.cos(np.deg2rad(60)))
resultado75= 10.54/(10.54*np.cos(np.deg2rad(75)))

tac = Tac2d(30)
tab= Tab2d(30)
resultado = tac/tab
print(resultado)
print(secante(30))

relacion = secante(rango)
result_exp=[resultado30,resultado45,resultado60,resultado75]


plt.figure(3)
plt.plot(rango,relacion)
plt.suptitle("Grados v. Relacion Tac/Tab (Teoricos)")
plt.xlabel("Grados sexagesimales")
plt.ylabel("Relacion Tac/Tab")
plt.show()

plt.figure(4)
plt.plot(rango,relacion,"r",rango2,result_exp,"b")
plt.suptitle("Grados v.  Relacion Tac/Tab")
plt.xlabel("Grados sexagesimales")
plt.ylabel("Fuerza de tensión en Tcd")
plt.xlim([30,75])
plt.ylim([0,10])
plt.legend(["Datos teoricos","Datos experimentales"])
plt.show()


