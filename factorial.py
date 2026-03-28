n = 5   # fixed value

fact = 1
if n < 0:
    print("Factorial not defined")
elif n == 0:
    print("Factorial is 1")
else:
    for i in range(1, n+1):
        fact = fact * i
    print("Factorial is:", fact)