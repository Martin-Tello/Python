def solution(n,trust):
    incoming = [0] * n
    outcoming = [0] * n
    for a, b in trust:
        outcoming[a - 1] += 1
        incoming[b - 1] += 1
    #print(outcoming)
    #print(incoming)
    judge = []
    for i in range(n):
        if incoming[i] == n - 1 and outcoming[i] == 0:
           judge.append(i + 1)
    #print(judge)
    if len(judge) != 1:
            return -1
        
    return judge[0]



def main():
    n = 3
    trust = [[1,3],[2,3]]
    solution(n,trust)

main()