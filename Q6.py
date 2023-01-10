def pattern(n):
    for i in range(1,n+1):
        print('*'*i + ' '*(2*(n-i)) + '*'*i)
n = int(input("Enter the length of the pattern : "))
pattern(n)