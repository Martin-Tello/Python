def solution(n,D,C,M,q):
    #print(q)
    RC = q.count("C")
    RD = q.count("D")
    if RD == 0:
        return "YES"
    #flagdog = True
    #flagcat = True
    iter = 1
    for i in q:
        #print(i)
        if i == "D":
            D -= 1
            #D += M
            C += M
            RD -= 1 
            #print("iter ",iter, "D-->",D)
            if D == 0 and RD >= 1:
                return "NO"
        elif C == 0 and RD >= 1:
                return "NO"
        elif C == 0 and RD == 0:
                return "YES"
        elif i == "C":
            C -= 1 
            #C += M
            RC -= 1
            #print("iter ",iter, "C-->",C)
            
        iter += 1

    return "YES"



def main():
    T = int(input())
    iter = 1
    for i in range(T):
        array=list(map(int,input().split()))
        N = array[0] #6 10 4 0
        D = array[1]
        C = array[2]
        M = array[3]
        s = input()
        q    = list(s)
        #print(q.count("C"))
        #print(q.count("D"))
        print("Case #{}: ".format(iter),solution(N,D,C,M,q))
        iter += 1
main()