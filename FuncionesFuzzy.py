import matplotlib.pyplot as plt
import numpy as np
import math

def And(A,B):
    C=min(A,B)
    return(C)

def Or(A,B):
    C=max(A,B)
    return(C)

def AndV(A,B):
    C=np.minimum(A,B)
    return(C)

def OrV(A,B):
    C=np.maximum(A,B)
    return(C)

def defuzzificacion(AreaResultante,RangoSalida):
    Defu=(sum(AreaResultante*RangoSalida))/sum(AreaResultante)
    return Defu



#Funciones Base
def FPTriangular(X,A=40,B=50,C=60):
    X = np.asarray(X)
    X = X.astype(float)

    Y = np.piecewise(X,
                     [X < A, (X >= A) & (X < B), (X >= B) & (X < C), X >= C],
                     [0, lambda X: ((X - A) / (B - A)), lambda X: ((C - X) / (C - B)), 0])

    return Y

def FPTrapezoidal(X,A=40,B=50,C=60,D=70):
    X = np.asarray(X)
    X = X.astype(float)

    Y = np.piecewise(X,
                     [X < A, (X >= A) & (X < B), (X >= B) & (X < C),(X>=C) & (X<D) , X >= D],
                     [0, lambda X: ((X - A) / (B - A)), 1,lambda X: ((D - X) / (D - C)), 0])

    return Y

def FPGaussiana(X, A=0, B=20):
    X = np.asarray(X)
    X = X.astype(float)
    Y= np.exp(-(((X - A) / B) ** 2))

    return Y

def Graficar(A=0,B=0,C=0,D=0,Min=0,Max=100,Tipo="Triangular"):
    incremento = 0.01
    X = np.arange(Min, Max, incremento)
    if Tipo=="Triangular":
        Y=FPTriangular(X,A,B,C)
    elif Tipo=="Trapezoidal":
        Y=FPTrapezoidal(X,A,B,C,D)
    elif Tipo=="Gauss":
        Y=FPGaussiana(X,A,B)

    plt.plot(X,Y)
    return(Y)

#Funciones Usuario
def DefinirConjuntos(Tipos=["Triangular",
                            "Triangular",
                            "Triangular"],Min=0,Max=100,
                     As=[-10,40,90],
                     Bs=[0,50,100],
                     Cs=[10,60,110],
                     Ds=[0,0,0],
                     EjeX="Eje X",
                     variables=["Bajo", "Medio", "Alto"],
                     Titulo="Variable N",
                     ):
    Funciones=[]
    for i,j in enumerate(Tipos):
        Y=Graficar(As[i],Bs[i],Cs[i],Ds[i], Min,Max,Tipo=j)
        Funciones.append(Y)
    plt.xlabel(EjeX)
    plt.ylabel("Grado de Pertenencia")
    plt.legend(variables)
    plt.title(Titulo)

    return (plt, Funciones)


def EvaluarValores(VE,
        Tipos=["Triangular","Gauss","Trapezoidal"],
                 As=[0,50,70],
                 Bs=[30,20,80],
                 Cs=[40,0,110],
                 Ds=[0,0,120],
                Graficar="Si"):
    VPert=[]

    for i,j in enumerate(Tipos):
        if j=="Triangular":
            Y=FPTriangular(VE,As[i],Bs[i],Cs[i])
            if Graficar=="Si":
                plt.plot(VE,Y, marker="o")
        elif j=="Gauss":
            Y = FPGaussiana(VE, As[i], Bs[i])
            if Graficar=="Si":
                plt.plot(VE,Y, marker="o")

        elif j=="Trapezoidal":
            Y = FPTrapezoidal(VE, As[i], Bs[i], Cs[i], Ds[i])
            if Graficar=="Si":
                plt.plot(VE,Y, marker="o")

        VPert.append(Y)
    if Graficar=="Si":
        plt.plot(np.array([VE, VE]), np.array([0, 1]),
                 linestyle=":")



    return VPert


"""
#Prueba
#Variable Entrada1
Tipos1=["Triangular","Gauss","Trapezoidal"]
As1=[0,50,70]
Bs1=[30,20,80]
Cs1=[40,0,110]
Ds1=[0,0,120]

DefinirConjuntos(Tipos=Tipos1,As=As1,Bs=Bs1,Cs=Cs1,Ds=Ds1,
                 EjeX="Temperatura",
                 Titulo="Entrada 1: Temperatura del Cuarto")

VPert=EvaluarValores(38,Tipos=Tipos1,As=As1,Bs=Bs1,Cs=Cs1,Ds=Ds1,
                     Graficar="Si")
print(VPert)
plt.show()
"""