N=int(input())
c=0
ans=0
tem=N
if(N<=100000000000):
  while(N>0):
    c+=1
    N=N//10
while(tem>0):
  rev=tem%10
  ans+=rev**c
  tem=int(tem/10)
print(ans)
