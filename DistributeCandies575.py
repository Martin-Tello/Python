from collections import defaultdict
def solution(array):
    #print(len(array)) 
    e = len(array)//2
    temp = set(array)
    #print(temp," ",e)
    eat = min(len(temp),e)
    #print(min(len(temp),e))
    return eat





def main():
    candyType = [1,1,2,3]
    solution(candyType)

main()