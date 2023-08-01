#Exercise 2:Reverse a number using while loop
num=int(input("Enter a number: "))
n=num//10
while num>0:
  remainder=num %10

  re=remainder+n
  break
print(f"Reversed number of {num} is {re}")