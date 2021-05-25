def isprime(n):
  # Corner cases
    if (n <= 1) :
        return False
    if (n <= 3) :
        return True
 
    # This is checked so that we can skip
    # middle five numbers in below loop
    if (n % 2 == 0 or n % 3 == 0) :
        return False
 
    i = 5
    while(i * i <= n) :
        if (n % i == 0 or n % (i + 2) == 0) :
            return False
        i = i + 6
 
    return True


m=int(input())
p=0
t=0
for i in range(2,m):
  p=m-i
  if(isprime(i) and isprime(p)):
      t=1
      break
if(t==1):
    print("True")
else:
    print("false")