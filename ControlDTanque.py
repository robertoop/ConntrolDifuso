from TanquedeAgua import *
import matplotlib.pyplot as plt
from celluloid import Camera


###Inicializacion
#Entradas
# Variable que controla que tan abierta esta la llave por donde se sale el agua
# 0 - 100 %
Desague=50
# Variable que controla que tan abierta esta la llaver por donde se llena el contenedor
# 0 - 100 %
Bomba=50
#
AlturadeAguaInicial=10



# Constantes
#CM
AlturaContenedor = 15
AnchuraContenedor = 15
LargoContenedor = 30

#ML/s
DesagueMaximo = 30
BombaMaxima = 30

#Tiempo S
Tiempo = 200



fig,ax= plt.subplots()

plt.xlim(0,50)
plt.ylim(0,30)
camera= Camera(fig)
# CorridaSimulador



VolumenActualML, VolumenTotalML, AlturaUltrasonico, AlturaActualCM = InicializarTanque (AlturadeAguaInicial)
Ultrasonico = AlturaUltrasonico - AlturaActualCM
GraficarTanque (LargoContenedor, AlturaContenedor, AlturaUltrasonico, Ultrasonico, fig, ax)


for i in range (Tiempo):

    # Control esta es la parte que deben cambiar por su control difuso
    AlturaActualCM = AlturaUltrasonico - Ultrasonico
    if AlturaActualCM < 10:
        Desague = Desague-1
        Bomba = Bomba+1


    else:
        Desague = Desague + 1
        Bomba = Bomba - 1

    #Limites fisicos de bomba y desague
    if Bomba>100:
        Bomba=100
    elif Bomba<0:
        Bomba=0

    if Desague>100:
        Desague=100
    elif Desague<0:
        Desague=0






    VolumenActualML, Ultrasonico = ContenedorCambiante (VolumenActualML, Bomba, Desague, i, VolumenTotalML,
                                                        AlturaUltrasonico)
    GraficarTanque (LargoContenedor, AlturaContenedor, AlturaUltrasonico, Ultrasonico, fig, ax)

    camera.snap()


animacion= camera.animate(interval=200)
animacion.save("Tanque2.gif", writer="imagemagick")










