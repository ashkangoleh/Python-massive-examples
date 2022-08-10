# fibo = lambda x: x if x <=1 else fibo(x-1) + fibo(x-2)
# x = int(input("What fibonacci factor would you like: "))

# Result = fibo(x)



# print("Your fibonacci number is: " + str(Result))


def recur_fibo(n):  
   if n <= 1:  
       return n  
   else:  
       return(recur_fibo(n-1) + recur_fibo(n-2))  
   
nterms = int(input("How many terms? "))  
li = []
for i in range(nterms):  
    li.append(recur_fibo(i))
    
print("==>> li: ", li)
print("==>> li: ", li.index(8))