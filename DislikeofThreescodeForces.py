def solution(s):
    array = []
    #print(l[(len(l)-1)])
    for i in range(1,1002):
        #print(i)
        temp = str(i)
        if i%3 == 0 or int(temp[len(temp)-1]) == 3:
            continue
        else:
            array.append(i)
    #print(array)
    return array[s]



def main():
    T = int(input())
    for i in range(T):
        s = int(input())
        print("sol ",solution(s))
    
main()