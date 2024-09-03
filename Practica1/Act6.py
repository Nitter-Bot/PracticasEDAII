#Graficar
import matplotlib.pyplot as plt
import timeit
import random

def graficas():
    plt.ylabel("Tiempo")
    plt.xlabel("Cantidad de elementos")
    #Bubble Sort
    
    TBubbleSort = []
    nD = [k*100 for k in range(1,31)]
    for k in nD:
        datosM = random.sample(range(1,1000000000),k)
        t0 = timeit.default_timer()
        burbujeo_modificado(datosM,len(datosM)-1)
        TBubbleSort.append(timeit.default_timer()-t0)
        t0 = timeit.default_timer()
    plt.plot(nD,TBubbleSort,color = "b")
   
    #Insertion Sort
    TInsertion = []
    nD = [k*100 for k in range(1,31)]
    for k in nD:
        datosM = random.sample(range(1,1000000000),k)
        t0 = timeit.default_timer()
        insertionSort(datosM,len(datosM)-1)
        TInsertion.append(timeit.default_timer()-t0)
        t0 = timeit.default_timer()
    plt.plot(nD,TInsertion,color = "g")
    #Selection Sort
    TSelection = []
    nD = [k*100 for k in range(1,31)]
    for k in nD:
        datosM = random.sample(range(1,1000000000),k)
        t0 = timeit.default_timer()
        selectionSort(datosM)
        TSelection.append(timeit.default_timer()-t0)
        t0 = timeit.default_timer()
    plt.plot(nD,TSelection,color = "black")
    plt.show()
    
graficas()
