#Burbujeo sin mejora

def swap(S,a,b):
  S[a],S[b] = S[b],S[a]


def burbujeo_by_scratch(secuencia, n):
    c = 0
    for i in range(0,n):                        # (0,n] == n-1     
        c += 1
        print("Pasada "+ str(c))
        for j in range(0,n-1):                  # (0,n-1] == n-2
            if secuencia[j]>secuencia[j+1]:     # 4 > 9 , make swaps using xor operator
                swap(secuencia,j,j+1)
            print(*secuencia)

    print(*secuencia)                           #Print secuencia , with beautiful output using the opt *



if __name__ == "__main__":
    secuencia = [10,9,8,7,6,5,4,3,2,1]
    size = len(secuencia)

    burbujeo_by_scratch(secuencia,size)         #Llamado de funcion burbujeo sin modificaciones
