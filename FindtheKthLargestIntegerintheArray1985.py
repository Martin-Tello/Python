import heapq as h
def solution(nums,k):
    nums = list(map(int,nums))
    for i in range(len(nums)):
        nums[i] = nums[i]*-1
    #print(nums)
    h.heapify(nums)
    print(nums)
    for i in range(k):
        x = h.heappop(nums)
        x = x*-1
        x = str(x)

    return x



def main():
    nums = ["0","0"]
    k = 2

    print(solution(nums,k))
main()