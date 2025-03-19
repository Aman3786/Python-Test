n = int(input())

# First Half to Print Character till in diamond shape n stage
for i in range(1,n+1):
    print(" "*(n-i),end=" ")
    for j in range(1,i+1):
        print(chr(j+64) + " ",end="")
    print()
    
# Second Half to print Character upside down in diamond shape n-1 stage
for i in range(n-1,0,-1):
    print(" "*(n-i),end=" ")
    for j in range(1,i+1):
        print(chr(j+64)+ " ", end="")
    print()