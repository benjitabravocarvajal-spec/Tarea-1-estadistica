import numpy as np
#definimos la función media muestral hasta el lanzamiento n-esimo, que recibe un array y un natural y devuelve la media muestral tomando los primeros n datos
def media_muestral(n, x):
    return np.mean(x[:n])
#definimos la función varianza muestral hasta el lanzamiento n-esimo, que recibe un array y un natural y devuelve la varianza muestral tomando los primeros n datos
def varianza_muestral(n, x):
    return np.var(x[:n])








##PARTE 3

#Modelo logístico 
def logist(x,alpha, beta):
    e = np.exp(alpha + beta*x)
    return e/(1+e)

#Modelo logístico-complementario
def log_com(x, alpha, beta):
    return 1 - np.exp(-np.exp(alpha + beta*x))

#función log-verosimilitud modelo logistico
def l_vtilde(alpha, beta):
    AUX = alpha + beta * concentracion

    Comb = comb(N, Z)
    coordenada = np.log(Comb) + Z*AUX - N*(np.log(1+np.exp(AUX)))

    return np.sum(coordenada)

#funcion log-verosimilitud modelo logistico complementario
def l_vbar(alpha, beta):
    AUX = alpha + beta * concentracion
    Comb = comb(N, Z)
    coordenada = np.log(Comb) + Z*np.log(1 - np.exp(- np.exp(AUX))) - (N - Z)*np.exp(AUX)

    return np.sum(coordenada)


#FUNCIONES AUXILIARES PARA OPTIMIZAR CON SPICY.MINIMIZE
def funcion_objetivo1(vars):
    x_0, y_0 = vars
    return -l_vtilde(x_0,y_0)

def funcion_objetivo2(vars):
    x_0, y_0 = vars
    return -l_vbar(x_0,y_0)

