def twosum(num,target):
    n=len(num)
    for i in range(0,n-1):
        for j in range(i+1,n):
            if num[i] + num[j] == target:
                return (num[i],num[j])
                return(i,j)# it return only index 
num=[2,7,11,15]
result=twosum(num,9)
print(result)                