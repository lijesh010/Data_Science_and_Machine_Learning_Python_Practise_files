c1=int(input("Enter the first amount: "))
c2=int(input("Enter the second amount: "))
print("CELSIUS\t\tFAHRENHEIT")
for celsius in range(c1,c2+2):
    fahren=celsius*9/5+32
    print(celsius,'\t\t',fahren)
