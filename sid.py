 def search(arr,n,key):
     for i in range(n):
         if(arr[i]==key):
             return i
#     return -1

# if __name__ == "__main__":
#     arr=[1,4,8,6,2,9,10]
#     key=8
#     n=len(arr)

#     index = search(arr,n,key)
#     if index != -1:
#             print("element found",index+1)  
#     else:
#             print("element not found")
               




# def insert(arr,element):
#     arr.append(element)

# if __name__ == "__main__":
#     arr=[1,2,3,4]
#     key=5
#     n=len(arr)


#     print("before inserted")
#     print(arr)

#     insert(arr,key)
#     print("after inserted")
#     print(arr)

# def insert(arr,n,x,pos):
#     for i in range(n-1,pos-1,-1):
#         arr[i + 1 ] = arr[i]
#     arr[pos]=x

# if __name__=="__main__":
#     arr=[10,20,30,40,50,60,70,-1]
#     n=7
#     for i in range(0,n):
#         print(arr[i],end="")
#     print("\n")
#     x=35
#     pos=3
#     insert(arr,n,x,pos)
#     i+=1
#     for i in range(0,n):
#         print(arr[i],end="")
     
def delete(arr,n,key):
    arr.remove(key)
# if __name__ == "__main__":
#     arr=[1,2,3,4]
#     n=len(arr)
#     key=2
#     print(arr)


#     arr.remove(key)
#     print(arr)    