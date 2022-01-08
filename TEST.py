
def solution(k,arr):
    #print(k,arr)
    arr.sort()
    cont = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] == arr[j]:
                print("prueba ",arr[i],arr[j])
                continue
            else:
                if arr[j] - arr[i] == k:
                    cont += 1
                print(arr[j] - arr[i])
    #print(cont)
    return cont


def main():
    k = 1
    arr = [1, 2,3,4]
    solution(k,arr)
main()
