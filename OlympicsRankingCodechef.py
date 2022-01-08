def solution(k):
    team1=0
    team2 =0
    team1 += k[0]+k[1]+k[2]
    team2 += k[3]+k[4]+k[5]
    #team1 += 
    #print(k[:3:])
    #print(k[3::])
    if team1 > team2:
        return 1
    else:
        return 2
    return 0



def main():
    T = int(input())
    for i in range(T):
        k = list(map(int,input().split()))
        solution(k)
        

main()