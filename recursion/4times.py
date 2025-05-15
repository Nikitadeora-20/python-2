# #print func() call outside the print statement (head recursion)  
# count = 0

# def func():
#     global count
#     if count == 4:
#         return
#     print("anirudh")
#     count += 1
#     func()

# func()

#print func() call inside the print statement (tail recursion)

count = 0
def func():
    global count
    if count==4:
        return
    count+=1
    func()
    print("a")    

func()