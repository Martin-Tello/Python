from bisect import bisect_right
def solution(nums,target):
    print(bisect_right(nums,target))
    """if target in nums:
        print(bisect_right(nums,target)-1)
        return bisect_right(nums,target) -1
    else:
        print(bisect_right(nums,target))
        return bisect_right(nums,target)
    return 0"""



def main():#empieza desde index 0, si ya está en la lista, lo deja lo más derecha posible
    nums = [1,3,5,6]
    target = 6
    solution(nums,target)
main()