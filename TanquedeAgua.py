import matplotlib.pyplot as plt
import matplotlib.patches as patches


def InicializarTanque(AlturaAguaInicial,AlturaContenedor = 15, AnchuraContenedor = 15,LargoContenedor = 30,Offset = 5):

    AlturaUltrasonico = AlturaContenedor + Offset
    # Volumen
    VolumenTotalCM3 = AlturaContenedor * AnchuraContenedor * LargoContenedor
    VolumenTotalML = VolumenTotalCM3


    VolumenActualCM3 = AlturaAguaInicial/ (AnchuraContenedor * LargoContenedor)
    VolumenActualML = VolumenActualCM3
    AlturaActualCM= AlturaAguaInicial

    return(VolumenActualML,VolumenTotalML,AlturaUltrasonico,AlturaActualCM)

def ContenedorCambiante(VolumenActualML,Bomba,Desague,i,VolumenTotalML,AlturaUltrasonico,
                        DesagueMaximo = 30,BombaMaxima = 30,
                        AnchuraContenedor = 15 ,LargoContenedor = 30 ):
    LLenadoActual = BombaMaxima * Bomba
    DesagueActual = DesagueMaximo * Desague

    VolumenActualML = VolumenActualML + LLenadoActual - DesagueActual

    if VolumenActualML >= VolumenTotalML:
        VolumenActualML = VolumenTotalML
    elif VolumenActualML <= 0:
        VolumenActualML = 0

    VolumenActualCM3 = VolumenActualML

    AlturaActualCM = VolumenActualCM3 / (AnchuraContenedor * LargoContenedor)

    Ultrasonico = AlturaUltrasonico - AlturaActualCM

    print ("##########################################################################")
    print ("Timestep: ", i)
    print ("El volumen del contenedor es: ", VolumenActualML, " ml")
    print ("La medida del sensor ultrasonico es: ", Ultrasonico, "cm")

    return (VolumenActualML,Ultrasonico)

def GraficarTanque(LargoContenedor,AlturaContenedor,AlturaUltrasonico,Ultrasonico,fig,ax):

    B1X= (50/2) - (LargoContenedor/ 2)
    ax.add_patch(
        patches.Rectangle (
            (B1X,1),
            LargoContenedor,
            AlturaContenedor,
            edgecolor="red",
            fill=False,
            linewidth=2

        )
    )
    AlturaActualCM = AlturaUltrasonico - Ultrasonico
    ax.add_patch (
        patches.Rectangle (
            (B1X, 1),
            LargoContenedor,
            AlturaActualCM,
            edgecolor="blue",
            fill=True

        )
    )







    








