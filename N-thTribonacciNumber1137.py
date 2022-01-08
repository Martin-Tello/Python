def solution(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 1
    array = [0,1,1]
    for i in range(3,n+1):
        #print(i)
        array.append(array[i-3]+array[i-2]+array[i-1])
    #print(array)
    return array[len(array)-1]



def main():
    n = 25
    solution(n)

main()