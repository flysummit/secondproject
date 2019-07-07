def jump(arr):
    if arr == None or len(arr) == 0:
        return False
    jumpnum = 0
    cur = 0
    next = 0
    for r in range(len(arr)):
        if cur < r:
            jumpnum += 1
            cur = next
        next = max(r + arr[r], next)
    return jumpnum

if __name__ == "__main__":
    arr = [3, 4, 5, 6, 5,9,15,10,8,7, 5, 5, 9, 8, 1]
    print(jump(arr))
