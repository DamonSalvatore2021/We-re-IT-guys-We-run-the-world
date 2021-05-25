#Code starts complete the code
years=int(input())
sum1=0
for i in range(0, years):
    
    for j in range(0,12):
        
       
        print("data for month %i of year %i"%(j,i))
        numbers= int(input())
        sum1=sum1 + numbers
      
      
print("Total inches of rainfall",sum1,"inches")
print("Total months",years*12)
print("Average rainfall per month",(sum1/(years*12)),"inches")





#Code Ends here