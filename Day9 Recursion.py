def factorial(n):
    if n==0:
        return 1
    elif n==1:
        return 1
    return n*factorial(n-1)
   

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = factorial(n)

    fptr.write(str(result) + '\n')

    fptr.close()

