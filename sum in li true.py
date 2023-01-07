a=list(map(int,input().split()))
n=int(input())
for i in range(0,len(a)):
    for j in range(0,len(a)):
        m=a[i]+a[j]
        if n==m:
            print("True")
        break

       
