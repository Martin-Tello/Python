def solution(nums):
    dic = {}
    for i in nums:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    print(dic)
    max_key = max(dic, key=dic.get)
    print(max_key)
    return max_key



def main():
    nums = [2,2,1,2,2,2,5,5,5,5,5,5,5]
    solution(nums)
main()