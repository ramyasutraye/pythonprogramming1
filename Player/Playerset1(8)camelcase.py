string=str(input(''))
if(len(string <= 1000000)):
  a=string.split(' ')
  s=''
  for i in range(len(a)):
    a[i]=a[i].capitalize()
    s+=a[i]+' '
print(s)
  
