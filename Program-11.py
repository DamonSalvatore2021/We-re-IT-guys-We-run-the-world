#Code starts complete the code

n = int(input())
count = 0

for i in range(1,n+1):
    m = str(i+i*(i+1)+i*(i+1)*(i+2))
    summ = 0
    for digit in str(m):
        summ = summ + int(digit)
        sum1 = summ
    if(summ < 2):
        print(m)
    else:
        for j in range(2, sum1):
            if(sum1 % j == 0):
                print(m)
                break
        else:
            print(m)
            print("primesum")
            count = count + 1

print("Total prime sum values:",count)
#Code Ends here