"""Exercise 5:
Write a program to print the inputted value as it is and break
the loop if the value is 'done'.
Example run of the program
:hello there
hello there
:finished
finished
:done
done"""


while input !="done":
  input=input("Enter content: ")
  if input=="done":
    break
     print("done")
  else:
    print(input)