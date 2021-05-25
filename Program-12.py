#Code starts complete the code

m = int(input())

n = int(input())

product_sum = 0
for i in range(m,n+1):
    pr = 1
    while(i>0):
        rem = i%10
        pr = pr*rem
        i = i//10
    product_sum += pr
    
avg = (m+n)//2

print("product sum=",product_sum)
if(product_sum > avg):
    print("True")
else:
    print("False")
    

#Code Ends here