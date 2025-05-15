def rotate(arr,n,k):
    mod=k%n
    s=""
    for i in range(n):
        print(arr[(mod+i)%n])
    return
arr=[4,5,1,9,2,6]
n=len(arr)
k=3
rotate(arr,n,k)