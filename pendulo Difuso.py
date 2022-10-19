import gym
import time
import numpy as np
from ControlDifuso2 import *

AcelGrav=0

env=gym.make('Pendulum-v1', g=AcelGrav)
observaciones=env.reset()
print(observaciones)

env.render()

def CalAngulo(observaciones):
    PX=observaciones[0]
    PY=observaciones[1]
    AnguloX=np.arccos(PX)*(180/3.1416)
    AnguloY=np.arcsin(PY)*(180/3.1416)

    if AnguloX>90 and AnguloY>0:
        AR=-AnguloY+90+90+90
    elif AnguloX>90 and AnguloY<=0:
        AR=abs(AnguloY)+180+90
    elif AnguloX<=90 and AnguloY>0:
        AR=AnguloY+90
    elif AnguloX<=90 and AnguloY<=0:
        AR=AnguloY+90

    if AnguloY>0:
        Region="izquierda"
    else:
        Region="derecha"

    return(AR, Region)

for i in range(5000):

    Ar, Region=CalAngulo(observaciones)
    AnguloDeseado=90
    Error=AnguloDeseado-Ar
    print("######################################")
    print("Angulo Deseado:", AnguloDeseado)
    print("Angulo Actual: ",Ar)
    print("Error Actual: ", Error)
    print("Velocidad Angular", -observaciones[2])
    if Error>180:
        Error= Error-360

    if Error<-180:
        Error = Error + 360
    Velocidad=-observaciones[2]

    SentidoGravedad=1
    print(Region)
    if Region=="derecha":
        if Velocidad>0:
            SentidoGravedad=1
            print("Gravedad a Favor")
            print("Caso1")
        else:
            SentidoGravedad=-1
            print("Gravedad en Contra")
    else:
        print("###################")
        print("Esta a la izquierda")
        print(Velocidad)
        if Velocidad>0:
            SentidoGravedad=-1
            print("Gravedad a contra")
        else:
            SentidoGravedad=1
            print("Gravedad a favor")
            print("Caso2")

    Gravedad=SentidoGravedad*AcelGrav

    #Fuzzificacion
    ErrorPosDifuso,VelocidadGiroDifuso,GravedadDifusa=EvaluarFunciones(Error,Velocidad,Gravedad)
    #Evaluar reglas y hacer inferencia
    MuyNegativo,Negativo,Neutro,Positivo,MuyPositivo=EvaluarReglas(ErrorPosDifuso, VelocidadGiroDifuso, GravedadDifusa)
    #Defuzzificacion
    Accion=-Deccicion(Tipos4, As4, Bs4, Cs4, Ds4, MuyNegativo, Negativo, Neutro, Positivo, MuyPositivo)


    print("Accion a tomar" , Accion)

    observaciones, reward, done, info = env.step(np.asarray([Accion]))
    time.sleep(0.1)
    env.render()
