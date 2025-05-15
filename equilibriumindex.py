def equilibrium(arr):
    left = 0
    right = 0
    for i in range(len(arr)):
        leftsum = sum(arr[:i])
        rightsum = sum(arr[i+1:])
        if leftsum == rightsum:
            return i 
    return -1

if __name__ == "__main__":
    arr=[1,2,3,9,2,0,4]
    print("equilibrium index of given array:",equilibrium(arr))