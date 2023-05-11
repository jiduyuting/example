
m=eval(input())
n=eval(input())
arr = []
arr=[[0 for j in range(n)]for i in range(m)]
for i in range(m):
    line=input().strip()
    arr[i]=[int(x) for x in line.split()]

for i in range(m):
    for j in range(n):
       if arr[i][j]==min(arr[i]) and arr[i][j]==min([arr[k][j] for k in range(m)]):
           print(arr[i][j],i+1,j+1)
