from itertools import product
def solution(digits):
    if len(digits) == 0:
        return []
    res = []
    if len(digits) == 0:
        return []
    dic = {"2":["a","b","c"],"3":["d","e","f"],"4":["g","h","i"],"5":["j","k","l"],"6":["m","n","o"],"7": ["p","q","r","s"],"8":["t","u","v"],"9":["w","x","y","z"]}
    
    temp = []
    res = []
    for i in digits:
        temp.append(dic[i])
    #print(temp)
    for item in product(*temp): 
        res.append(item)
        #print(item)
    #print(res)
    res2 = []
    for i in res:
        res2.append("".join(i))
    print(res2)
    return res



def main():
    digits = "8954"
    solution(digits)

main()