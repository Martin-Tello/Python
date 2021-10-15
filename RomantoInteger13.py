def solution(s):
    dic = {"I":1,"V":5,"IV":4,"IX":9,"XL":40,"XC":90,"CD":400,"CM":900,"X":10,"L":50,"C":100,"D":500,"M":1000}
    print(dic)
    #puntero1=0
    #puntero2=1
    res = 0
    iter=0
    #print(s[puntero1]+s[puntero2])
    while(iter<len(s)-1):
        if dic[s[iter]] < dic[s[iter+1]]:
            res += dic[s[iter]+s[iter+1]]
            iter += 2
        else:
            res += dic[s[iter]]
            iter += 1
        #print(res)
    #print(iter)
    if iter == len(s)-1:
        res += dic[s[len(s)-1]]
    #print("res ",res)
    return res



def main():
    s = "LVIII"
    solution(s)
main()