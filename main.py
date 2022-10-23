
# ******************************
# Make your Code
# ******************************

strval = input("Enter 5 numbers, separated by space: ").split()
numbers = []

for v in strval:
  numbers.append(int(v))


check = int(input("Enter int: "))
print(f"The occurences of {check}: {numbers.count(check)}")
