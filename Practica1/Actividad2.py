#Burbujeo 'mejorado'

def swap(S,a,b):                                
    S[a],S[b] = S[b],S[a]

def burbujeo_modificado(secuencia, n):
    f = 1                                       #Bool to check if a swap is made
    c = 0                                       #Counter 
    while f==1 and c<n:                         
        f = 0                                   #Initialize f in 0 
        c+=1                            
        print("Pasada" + str(c))                
        for j in range(n-1,c-1,-1):             #To make a proper burble sort    
            if secuencia[j]<secuencia[j-1]:     
                swap(secuencia, j-1,j)
                f = 1                           #True
            print(*secuencia)

    print("\n\n Total de pasadas con algoritmo mejorado "+str(c)+"\n")
    print(*secuencia)                           #Print secuencia , with beautiful output using the opt *



if __name__ == "__main__":
    secuencia =  [10,9,8,7,6,5,4,3,2,1]
    size = len(secuencia)

    burbujeo_modificado(secuencia,size)         #Llamado de funcion burbujeo sin modificaciones
