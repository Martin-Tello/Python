from itertools import product
def solution(array):
    temp1 = False
    temp2 = False
    tem3 = False
    for i in range(4):
        for j in range(3):
            #print(array[i][j],end = " ")
            if array[i][j] == "y":
                x = j + 1
                print("TOPIC ",x)
                if x == 
            #elif array[i][j]
        print("")

    return 0



def main():
    array = [["y","n","n"],["n","y","n"],["y","y","n"],["y","n","y"]]
    solution(array)
main()


#m = 3
    #n = 3
    #matrix = [[".",".","."],["#","#","#"],[".",".","#"]]
    #image = [[".","#",".",".","."],[".","#",".",".","."],[".","#","#","#","."],[".",".",".",".","."]]
    ##print(matrix)
    #for i in range(m):
    #    for j in range(n):
    #        print(matrix[i][j],end = " ")
    #    print("\n")
    #for i in range(m):
    #    for j in range(n):
    #        print(matrix[i][j],end = " ")
    #    print("\n")
    #[".",".","."]]