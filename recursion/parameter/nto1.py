#using tail
# def func(i,n):
#     if i>n:
#         return
#     func(i+1,n)
#     print(i)    
# func(0,5)    

#using head
def func(i,n):
    if n==0:
        print(i)
        return 
    func(i+1,n-1)
func(0,5)

