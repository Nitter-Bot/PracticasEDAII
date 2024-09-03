#Graficar
import matplotlib.pyplot as plt
import timeit
import random

def graficas():
    plt.ylabel("Tiempo")
    plt.xlabel("Cantidad de elementos")
    nD = [k*100 for k in range(1,31)]
    
    #Heap Sort
    THeapSort = []
    nD = [k*100 for k in range(1,31)]
    for k in nD:
        datosM = random.sample(range(1,1000000000),k)
        t0 = timeit.default_timer()
        OrdenacionHeapSort(datosM,len(datosM)-1)
        THeapSort.append(timeit.default_timer()-t0)
    plt.plot(nD,THeapSort,color = "r",label = "Heap Sort")
    
    #Bubble Sort
    
    TBubbleSort = []
    
    for k in nD:
        datosM = random.sample(range(1,1000000000),k)
        t0 = timeit.default_timer()
        burbujeo_modificado(datosM,len(datosM)-1)
        TBubbleSort.append(timeit.default_timer()-t0)
        t0 = timeit.default_timer()
    plt.plot(nD,TBubbleSort,color = "b")
   
    #Insertion Sort
    TInsertion = []
    
    for k in nD:
        datosM = random.sample(range(1,1000000000),k)
        t0 = timeit.default_timer()
        insertionSort(datosM,len(datosM)-1)
        TInsertion.append(timeit.default_timer()-t0)
        t0 = timeit.default_timer()
    plt.plot(nD,TInsertion,color = "g")
    #Selection Sort
    TSelection = []
   
    for k in nD:
        datosM = random.sample(range(1,1000000000),k)
        t0 = timeit.default_timer()
        selectionSort(datosM)
        TSelection.append(timeit.default_timer()-t0)
        t0 = timeit.default_timer()
    plt.plot(nD,TSelection,color = "black")
    

    #QuickSort
    TQuickSort = []
    for k in nD:
        datosM = random.sample(range(1,1000000000),k)
        t0 = timeit.default_timer()
        QuickSort(datosM,0,len(datosM)-1)
        TQuickSort.append(timeit.default_timer()-t0)
    plt.plot(nD,TQuickSort,color = "y",label = "Quick Sort")

    #Merge Sort
    TMergeSort = []
    for k in nD:
        datosM = random.sample(range(1,1000000000),k)
        t0 = timeit.default_timer()
        mergeSort(datosM,0,len(datosM)-1)
        TMergeSort.append(timeit.default_timer()-t0)
    plt.plot(nD,TMergeSort,color = "orange",label = "Merge Sort")

    plt.show()
    
graficas()
