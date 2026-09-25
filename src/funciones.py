import numpy as np
#definimos la función media muestral hasta el lanzamiento n-esimo, que recibe un array y un natural y devuelve la media muestral tomando los primeros n datos
def media_muestral(n, x):
    return np.mean(x[:n])
#definimos la función varianza muestral hasta el lanzamiento n-esimo, que recibe un array y un natural y devuelve la varianza muestral tomando los primeros n datos
def varianza_muestral(n, x):
    return np.var(x[:n])