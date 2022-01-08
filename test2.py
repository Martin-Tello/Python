# Python program to find a pair with the given difference

# The function assumes that the array is sorted

def find(arr,n):
    arr.sort()
    size = len(arr)
    i,j=0,1
    cont = 0
    while  i<size and j<size:
        if i != j and arr[j] - arr[i] == n:
            cont += 1
            return True
        elif  arr[j] - arr[i] < n:
            j+=1
        else:
            i+=1
    return False

# Driver function to test above function
arr = [1,5,3,4,2]
n = 2
print(find(arr, n))

# This code is contributed by Devesh Agrawal
