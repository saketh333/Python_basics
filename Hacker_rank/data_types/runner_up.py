# given a list of scores and number of teams find the runner up score


if __name__ == '__main__':
    n = int(raw_input())
    arr = (map(int, raw_input().split()))
    arr = list(arr)
    arr.sort()
    max = arr[-1]
    for i in range(n):
        if arr[-(i + 1)] < max:
            print arr[-(i+ 1)]  
            break            
