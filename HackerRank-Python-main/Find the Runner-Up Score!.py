if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    first=arr[0]
    for item in arr:
        if first > item:
            print(item)
            break
