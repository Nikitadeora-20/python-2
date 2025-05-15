def merge(num1,num2,m,n):
    m=len(num1)-1
    n=0
    while m>0 and n<len(num2):
        if num1[m] < num2[n]:
            m-=1
        else:
            num1[m] ,num2[n] = num2[n],num1[m]
            m -=1
            n +=1
    num1.sort()
    num2.sort()
if __name__ == "__main__":
    num1=[1,5,9,10,15,20]
    num2=[2,3,8,13]
    m=len(num1)
    n=len(num2)
    merge(num1,num2,m,n)
    for ele in num1:
        print(ele,end="")
    print()
    for ele in num2:
        print(ele,end="") 
    print()                       