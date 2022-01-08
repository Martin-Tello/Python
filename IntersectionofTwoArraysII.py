from collections import Counter
def solution(nums1,nums2):
    counter1 = Counter(nums1)
    counter2 = Counter(nums2)
    print(counter1)
    print(counter2)
    res = []
    temp = 0
    for i in counter1.keys():
        #print(i)
        if i in counter2.keys():
            #print("res ",counter2[i])
            res += [i] * min(counter1[i],counter2[i])
            print("temp ",temp)
            
    print(res)  
    return res



def main():
    nums1 = [4,9,9,5]
    nums2 = [9,4,9,8,4]
    solution(nums1, nums2)
main()