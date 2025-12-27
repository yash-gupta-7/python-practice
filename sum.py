def sumofn(n):
    if (n==0 or n==1):
        return 1
    else :
        return n + sumofn(n-1)

n = int(input("enter a number : "))

print(f"sum {sumofn(n)}")