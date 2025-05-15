#using head
# def func(sum,i,n):
#     if i>n:
#         print(sum)
#         return
#     func(sum+i,i+1,n)
# func(0,1,5)        


#using tail
def func(sum,i,n):
    if i>n:
        return
    func(sum+i,i+1,n)
    print(sum)
func(0,1,5)        