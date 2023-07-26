import math
x = float(input("enter a positive number: "))

# initialize the tolerance and estimate
tolerance = 0.0000001
estimate = 1.0

# perform the successive approximations
while True:
    estimate = (estimate +x/estimate) /2
    difference = abs(x - estimate ** 2)
    if difference <= tolerance:
        break

# Output the result
print("The program's estimate: ", estimate)
print("Python's estimate: ", math.sqrt(x))

