from random import randint
import random
import math 
import matplotlib.pyplot as plt
import numpy as np


pesoPaquete1 = 1
pesoPaquete2 = 2
pesoPaquete3 = 3
pesoPaquete4 = 4
pesoPaquete5 = 5
initial_population=[]
aux=[]
packages=[]
paquetesElegidos=0
choosenPackages=[]
all_fitness=[]
mejorfit_gen=[]
peorfit_gen=[]
promfit_gen=[]
prob_wheel_roulette=[]
aux_fitness=[]
paquetes_a_enviar=[]

def seleccion(initial_population):
    global aux_fitness
    paquete_generacion=[]
    aux_fitness=[]
    retorno_gen=[]
    suma_fitness = 0
    prom_fitness= 0
    best_retorno=[]
    best2_retorno=[]
    evaluar_esto=[]
    z=0
    for x in initial_population:
        auxiliar= initial_population[z]
        sumaCostos=0
        for y in auxiliar:
            sumaCostos += y[0]
        z+=1
        aux_fitness.append(sumaCostos)
        evaluar_esto.append([x, sumaCostos])
    suma_fitness=sum(aux_fitness)
    prom_fitness=suma_fitness/(len(initial_population))
    print("suma fitness " ,suma_fitness)
    print("promedio fitness " , prom_fitness)
    print("maximo fitness " , max(aux_fitness))
    for y in aux_fitness:
        prob_individual = y/suma_fitness
        prob_wheel_roulette.append(prob_individual)

    paquete_generacion.append([aux_fitness, suma_fitness])

    maximo_gen=max(aux_fitness)
    minimo_gen=min(aux_fitness)
    mejorfit_gen.append(maximo_gen)
    peorfit_gen.append(minimo_gen)
    promfit_gen.append(prom_fitness)
    aux_fitness.sort()
    tamanio_auxfit = len(aux_fitness)
    best_retorno=aux_fitness[tamanio_auxfit-1]
    best2_retorno=aux_fitness[tamanio_auxfit-2]

    for pero in evaluar_esto:
        if pero[1] == best_retorno:
            best_retorno=pero[0]
            retorno_gen.append(best_retorno)
        if pero[1] == best2_retorno:
            best2_retorno=pero[0]
            retorno_gen.append(best2_retorno)
    paquetes_a_enviar.extend([best_retorno, best2_retorno])
    return retorno_gen

def crossover(datos):
    puntoCorte1=randint(1,len(datos[0])-1)
    puntoCorte2=randint(1,len(datos[1])-1)
    valor1 = datos[0]
    valor2 = datos[1]
    entran = datos
    mitaduno1 = valor1[:puntoCorte1]
    mitaduno2 = valor1[puntoCorte1:]

    mitadDos1 = valor2[:puntoCorte2]
    mitadDos2 = valor2[puntoCorte2:]

    print("partidos padre 1", mitaduno1, " - - - - - ", mitaduno2)
    print("partidos padre 2", mitadDos1, " - - - - - ", mitadDos2)
    hijo1=[]
    hijo2=[]
    hijitos=[]

    hijo1.extend(mitaduno1)
    hijo1.extend(mitadDos2)

    hijo2.extend(mitadDos1)
    hijo2.extend(mitaduno2)

    hijitos.append(hijo1)
    hijitos.append(hijo2)
    data_returned = validate_weight(hijitos, entran)
    print("padre 1 entro como: ",entran[0])
    print("padre 2 entro como: ",entran[1])
    print("hijo 1 salio como: ",data_returned[0])
    print("hijo 2 salio como: ",data_returned[1])

    return data_returned

def mutation(datos):
    aMutar=datos
    indice=0
    for a in datos:
        ans = bool(random.getrandbits(1))
        if ans:
            for y in range(len(a)):
                if bool(random.getrandbits(1)):
                    indexPackage = random.randint(1, 5)
                    newPackage = obtener_Paquete(indexPackage)
                    datos[indice][y] = newPackage   
                else:
                    print("no muto el gen")
        indice+=1
    validate_weight_mutation(datos, aMutar)
    return datos

def obtener_Paquete(indice):
    for i in packages:
        peso=i[1]
        if(indice == peso):
            requerido=i
            break
        else:
            print("")
    return requerido

def validate_weight(hijitos, datos):
    hijos_returned=[]
    valor1=hijitos[0]
    valor2=hijitos[1]
    sumValor1=0
    sumValor2=0
    for d in valor1:
        sumValor1+=d[1]
    for e in valor2:
        sumValor2+=e[1]
    if sumValor1 > tamanioContenedor:
        print("primero hijo cruzado no paso")
        while sumValor1 > tamanioContenedor:

            puntoCorte1=randint(1,len(datos[0])-1)
            puntoCorte2=randint(1,len(datos[1])-1)
            valor1 = datos[0]
            valor2 = datos[1]

            mitaduno1 = valor1[:puntoCorte1]
            mitaduno2 = valor1[puntoCorte1:]

            mitadDos1 = valor2[:puntoCorte2]
            mitadDos2 = valor2[puntoCorte2:]

            print("partido padre 1", mitaduno1, " - - - - - ", mitaduno2)
            print("partido padre 2", mitadDos1, " - - - - - ", mitadDos2)
            hijo1=[]
            hijo2=[]
            hijitos=[]

            hijo1.extend(mitaduno1)
            hijo1.extend(mitadDos2)

            hijo2.extend(mitadDos1)
            hijo2.extend(mitaduno2)

            auxvalor1=0
            auxvalor2=0
            for d in hijo1:
                auxvalor1+=d[1]
            for e in hijo2:
                auxvalor2+=e[1]
            if auxvalor1 <= tamanioContenedor:
                hijitos.append(hijo1)
                sumValor1=auxvalor1
                hijos_returned.append(hijo1)
            else: 
                print("peso hijo 1 > container")
                if auxvalor2 <= tamanioContenedor:
                    hijitos.append(hijo2)
                    sumValor1=auxvalor2
                    hijos_returned.append(hijo2)
                else:
                    print("peso hijo 2 > container")
    else:
        hijos_returned.append(valor1)

    if sumValor2 > tamanioContenedor:
        print("segundo hijo cruzado no paso")
        while sumValor2 > tamanioContenedor:

            puntoCorte1=randint(1,len(datos[0])-1)
            puntoCorte2=randint(1,len(datos[1])-1)
            valor1 = datos[0]
            valor2 = datos[1]

            mitaduno1 = valor1[:puntoCorte1]
            mitaduno2 = valor1[puntoCorte1:]

            mitadDos1 = valor2[:puntoCorte2]
            mitadDos2 = valor2[puntoCorte2:]

            print("partidos padres 1", mitaduno1, " - - - - - ", mitaduno2)
            print("partidos padres 2", mitadDos1, " - - - - - ", mitadDos2)

            hijo1=[]
            hijo2=[]

            hijo1.extend(mitaduno1)
            hijo1.extend(mitadDos2)

            hijo2.extend(mitadDos1)
            hijo2.extend(mitaduno2)

            auxvalor1=0
            auxvalor2=0
            for d in hijo1:
                auxvalor1+=d[1]
            for e in hijo2:
                auxvalor2+=e[1]
            if auxvalor1 <= tamanioContenedor:
                hijitos.append(hijo1)
                sumValor2=auxvalor1
                hijos_returned.append(hijo1)
            else: 
                print("peso hijo 1 > container")
                if auxvalor2 <= tamanioContenedor:
                    hijitos.append(hijo2)
                    sumValor2=auxvalor2
                    hijos_returned.append(hijo2)
                else:
                    print("peso hijo 2 > container")
        
    else:
        hijos_returned.append(valor2)
    return hijos_returned

def validate_weight_mutation(datos, aMutar):
    a_retornar=[]
    valor1=datos[0]
    valor2=datos[1]
    sumValor1=0
    sumValor2=0
    for d in valor1:
        sumValor1+=d[1]
    for e in valor2:
        sumValor2+=e[1]
    if sumValor1 > tamanioContenedor:
        intentos=0
        while sumValor1 > tamanioContenedor:
            mutados_returned=[]
            suma1=0
            suma2=0
            indice=0
            for a in aMutar:
                ans = bool(random.getrandbits(1))
                if ans:
                    for y in range(len(a)):
                        if bool(random.getrandbits(1)):
                            indexPackage = random.randint(1, 5)
                            newPackage = obtener_Paquete(indexPackage)
                            aMutar[indice][y] = newPackage
                        else:
                            print("no muto el gen")
                    mutados_returned.append(aMutar[indice])
                indice+=1
            print("se mutaron asi ",aMutar)
            aux = aMutar[0]
            aux2 = aMutar[1]
            for d in aux:
                suma1+=d[1]
            for e in aux2:
                suma2+=e[1]
            if suma1 <= tamanioContenedor:
                sumValor1=suma1
                a_retornar.append(aux)
            else:
                if suma2 <= tamanioContenedor:
                    sumValor1=suma2
                    a_retornar.append(aux2)
                else:
                    print("peso mutado 2 > container")   
            intentos+=1
    else:
        a_retornar.append(valor1)

    if sumValor2 > tamanioContenedor:
        while sumValor2 > tamanioContenedor:
            mutados_returned=[]
            suma1=0
            suma2=0
            indice=0
            for a in aMutar:
                ans = bool(random.getrandbits(1))
                if ans:
                    for y in range(len(a)):
                        if bool(random.getrandbits(1)):
                            indexPackage = random.randint(1, 5)
                            newPackage = obtener_Paquete(indexPackage)
                            aMutar[indice][y] = newPackage
                        else:
                            print("no muto el gen")
                    mutados_returned.append(aMutar[indice])
                indice+=1
            print("se mutaron asi ",aMutar)
            print(aMutar)
            aux = aMutar[0]
            aux2 = aMutar[1]
            for d in aux:
                suma1+=d[1]
            for e in aux2:
                suma2+=e[1]
            if suma1 <= tamanioContenedor:
                sumValor1=suma1
                a_retornar.append(aux)
            else:
                if suma2 <= tamanioContenedor:
                    sumValor1=suma2
                    a_retornar.append(aux2)
                else:
                    print("peso mutado 2 > container")
    else:
        a_retornar.append(valor2)
    return a_retornar
    
def generate_population(paquetesIniciales):
    while len(initial_population) < paquetesIniciales:
        seleccionado=[]
        suma=0
        while suma < tamanioContenedor:
            randomPackage= random.randint(0,4)
            n = packages[randomPackage]
            suma += n[1]
            seleccionado.append(n)
        if suma > tamanioContenedor:
            print("peso > contenedor")
        else:
            initial_population.extend([seleccionado])
        
def generate_packages():
    while len(aux) < 5:
        i=0
        indice = random.randint(1, 10)
        if len(aux) == 0:
            aux.extend([indice])
        else:
            if indice in aux:
                print("numero repetido")
            else:
                aux.extend([indice])
    aux.sort()
    for i in range(len(aux)):
        packages.extend([[aux[i], i+1]])

def mostrar_Poblacion():
    f=0
    costos=0
    for i in initial_population:
        costos = initial_population[f] 
        sumaCostos=0
        sumaPeso=0
        for x in costos:
            sumaCostos += x[0]
            sumaPeso += x[1]
        f+=1
        print("individuo",f,".-", i, "pesa = ", sumaPeso," ---- suma de costos= ", sumaCostos)

def mostrar_Paquetes_a_enviar():
    f=0
    costos=0
    for i in paquetes_a_enviar:
        costos = paquetes_a_enviar[f] 
        sumaCostos=0
        sumaPeso=0
        for x in costos:
            sumaCostos += x[0]
            sumaPeso += x[1]
        f+=1
        print("individuo a enviar ",f,".-", i, "pesa = ", sumaPeso," ---- suma de costos= ", sumaCostos)

def generateGraphic(x,y,z):
   plt.plot(x, label = "Mejor Caso")   # Dibuja el gráfico
   plt.xlabel("abscisa")   # Inserta el título del eje X
   plt.ylabel("ordenada")   # Inserta el título del eje Y
   plt.ioff()   # Desactiva modo interactivo de dibujo
   plt.ion()   # Activa modo interactivo de dibujo
   plt.plot(y, label = "Peor Caso")   # Dibuja datos de lista2 sin borrar datos de lista1
   plt.ioff()   # Desactiva modo interactivo
   plt.ion()   # Activa modo interactivo de dibujo
   plt.plot(z, label = "Caso promedio")   # Dibuja datos de lista2 sin borrar datos de lista1
   plt.ioff()   # Desactiva modo interactivo
   # plt.plot(lista3)   # No dibuja datos de lista3
   plt.legend()
   plt.show()   # Fuerza dibujo de datos de lista3

if __name__ == "__main__":
    tamanioContenedor = int (input("Tamano del contenedor: "))
    numPaquetes = int (input("Numero de paquetes a enviar: "))
    paquetesIniciales = int (input("Numero de paquetes iniciales: "))
    generate_packages()
    print("PAQUETES GENERADOS: ",packages)
    generate_population(paquetesIniciales)
    mostrar_Poblacion()
    poblation = initial_population
    i=0
    while paquetesElegidos < numPaquetes:
        i+=1
        print("Generacion no. ",i)
        poblation = seleccion(poblation)
        paquetesElegidos+=2
        crossover_data=crossover(poblation)
        mutation_data=mutation(crossover_data)
        poblation.extend(mutation_data)
    mostrar_Paquetes_a_enviar()
    generateGraphic(mejorfit_gen, peorfit_gen, promfit_gen)

        