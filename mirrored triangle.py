n=int(input("Enter the number of rows:"))

print("Mirrored Right Triangle Star Pattern")
for i in range(1, n+1):
    for j in range(1, n+1):
        if(j<= n-i):
            print(' ', end= ' ') 
        else:
            print('*', end= ' ')
    print()