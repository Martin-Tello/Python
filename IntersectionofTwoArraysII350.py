import collections as d
def solution(a1,a2):
    x = d.Counter(a1) & d.Counter(a2)
    print(x)
    for x in x:
        print(x)
    return 0





def main():
    nums1 = [1,2,2,1,3]
    nums2 = [2,2,3]
    solution(nums1,nums2)

main()