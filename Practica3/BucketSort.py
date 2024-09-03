
#Uso de insertion sort
def insertion_sort(bucket):
    for i in range(1, len(bucket)):
        key = bucket[i]
        j = i - 1
        while j >= 0 and bucket[j] > key:
            bucket[j + 1] = bucket[j]
            j -= 1
        bucket[j + 1] = key

def bucket_sort(A):
    n = len(A)
    buckets = [[] for _ in range(n)]
    print("Buckets al inicio: ")
    print(buckets)

    # Put array elements in different buckets
    print("Ingresamos los datos a los buckets")
    for num in arr:
        i = int(n * num)
        buckets[i].append(num)
        print(buckets)

    # Sort individual buckets using insertion sort
    print("Ordenamos cada Bucket")
    for bucket in buckets:
        insertion_sort(bucket)
        print(bucket)

    # Concatenate all buckets into arr[]
    print("Buckets de regreso a la secuencia")
    i = 0
    for bucket in buckets:
        for num in bucket:
            A[i] = num
            i += 1
    print(A)
    

if __name__ == "__main__":
    arr = [0.78,0.17,.039,0.72,0.94,0.21,0.12,0.23,0.68]
    bucket_sort(arr)
