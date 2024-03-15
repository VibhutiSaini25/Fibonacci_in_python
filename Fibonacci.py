#USING RECURSION

#FIBONACCI

def Fibo(n):
    if(n<=1):
        return n
    return (Fibo(n-1)+Fibo(n-2))
n=int(input())
for i in range(n):
    print(Fibo(i),end=" ")