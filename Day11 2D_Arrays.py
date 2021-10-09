def hourGlassSum(arr):
    maxSum = -99

    for i in range (4):
        for j in range(4):
            top = sum(arr[i][j:j+3])
            middle = arr[i+1][j+1]
            bottom = sum(arr[i+2][j:j+3])
            hourGlassSum = top+middle+bottom
            maxSum = max(hourGlassSum, maxSum)

    return maxSum
            
            
if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
        
    res = hourGlassSum(arr)
    print(res)

