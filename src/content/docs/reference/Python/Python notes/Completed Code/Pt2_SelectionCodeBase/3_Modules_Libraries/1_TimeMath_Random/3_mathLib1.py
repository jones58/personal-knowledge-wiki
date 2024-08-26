import math # import (module) math
# This module provides access to the mathematical functions defined by the C standard

radius = float(input("Enter radius: "))
# area = math.pi * radius ** 2
area1 = math.pi * math.pow(radius,2) #Return x**y (x to the power of y).

"Predict, then Run, and then Investigate"

# print(f"The area is {area}")
print(f"The area 1 is {area1}")

# Method 1
# Round (round) a number to a given precision in decimal digits.
print(f"The area displayed is rounded to 2 decimal places {round(area1, 2)}")

# # Method 2
print(f"The area displayed is rounded to 2 decimal places {area1:.2f}")


# # Method 3
roundNum = math.ceil(area1)
print(f"The area displayed is rounded up {roundNum}")


# # Method 4
roundNumDown = math.floor(area1)
print(f"The area displayed is rounded down {roundNumDown}")


  


