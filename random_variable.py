from random import random
from math import log
from statistics import pvariance

def generate(quantity):
    seed = random()
    lambdaNumber = 0.429
    generatedNumbers = []
    for i in range(quantity):
        seed = fixSeed(seed)
        print(type(seed))
        print(type(lambdaNumber))
        seed = ((-(log(1 - seed)))/lambdaNumber)
        seed= fixSeed(seed)
        generatedNumbers.append(seed)
    return generatedNumbers

def media(generatedNumbers):
    suma=0
    media=0
    i=0
    for i in range (len(generatedNumbers)):
        suma+=generatedNumbers[i]
    media=suma / len(generatedNumbers)
    return  media
    
def varianza(generatedNumbers):
    return  pvariance(generatedNumbers)


def fixSeed(seed):
    while seed >= 1:
        seed = seed/10
    return seed

#if int(quantity):
#    generatedNumbers = generar(seed, quantity, generatedNumbers)
#    print ("Numeros Generados", generatedNumbers)
#else:
#    print ("La cantidad ingresada no es un numero entero")
