def missing(arr):
    n=len(arr)
    freq={}
    for i in range(0,n+1):
        freq[i]=0

    for arr in arr:
        freq[arr]=1

    for k,v in freq.items():
        if v ==  0:
            return k 


arr=[1,0,3,4]
result=missing(arr)
print(result)                    