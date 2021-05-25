#Code starts complete the code
sum=0
a=[]
for i in range(0,100):
    n = input()
    if(int(n)>=0 and (int(n)%2)==0):
        a.append(int(n))
    elif(int(n)<0 and (int(n)%2)==0):
        print("Sum of even positive integers ")
        break
    elif((int(n)%2)!=0):
        print("Invalid series term")
        print("Sum of even positive integers till now ")
        break
    
    
    
    
for x in range (0,len(a)):
    sum = sum + a[x]
print(sum)
    
        
            
           
       
       
       
       
       
#Code Ends here