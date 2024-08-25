"To DO: Read through the casting examples in your own time and reference or use it as a guide during your lesson"
# Converting a value from one data type to another is known as casting

"To DO: Further reading on casting in python"
# https://www.w3docs.com/learn-python/python-casting.html

# To convert values to different data types, you need to know the functions that are available to you.
# Here are the most common functions that you will need to know.
# You can find these in the Python documentation.
#
"Objectives"
"" '' # convert to string
# str()
"" '' # convert to integer
# int()
"" '' # convert to float
# float()


"""create a list"""
lst = [20, 30, 50, 234]
print(type(lst), "\n")  # returns list type class
print(lst, "\n")

"""converting a list into bytes"""
b = bytes(lst)
print(type(b), "\n")  # returns list type class
print(b, "\n")

"""converting a list into bytearray"""
b1 = bytearray(lst)
print(type(b1), "\n")  # returns list type class
print(b1)

###### Numerric data types ##########
""" Type conversion functions """
num1 = 13
num2 = 100
num3 = -66

print(num1, num2, num3)

num4 = 33.5
num5 = 25.8
num6 = 205

print(num4, num5, num6)

num7 = 3 + 5j
print(num7)

num8 = 0b1010
print(num8)

num9 = 0xFF
print(num9)

a = True
b = False
print(a)

print(b)

print(type(a), type(b))

print(9 > 8)
print(9 < 8)

print(
    type(num1),
    type(num2),
    type(num3),
    type(num4),
    type(num5),
    type(num6),
    type(num7),
    type(num8),
    type(num9),
)
num10 = int(num4)
print("This value is converted to a whole number", num10)

print(type(num10))

i = float("22.5")  # String converted to float
print(i)

print(type(i))  # type is now float after casting

print(bin(num6))  # casting to binary datatype

print(hex(num2))  # casting to hexadeximal datatype

print(hex(10))  # casting to hexadeximal datatype

print(oct(num1))  # casting to octal string datatype
print(type(num1))

print(oct(10))  # casting to octal string datatype


# Type Cast string to int
num_int = 123
num_str = "456"

print("Data type of num_int:", type(num_int))
print("Data type of num_str before Type Casting:", type(num_str))

num_str = int(num_str)
print("Data type of num_str after Type Casting:", type(num_str))

num_sum = num_int + num_str

print("Sum of num_int and num_str:", num_sum)
print("Data type of the sum:", type(num_sum))

# typecast string to float

# Note: Please note that, if you have decimal point in the string,
# you cannot typecast that directly to an integer. You should first
#  typecast string # to float and then that to integer. Following is a quick code snippet for the same.

# first float
s = "132.65"
f = float(s)
print(f)
print(type(f))

#  now from float to int
n = int(float(s))
print(n)
print(type(n))

# Type Cast string to int  directly
s1 = "123"
print(type(s1))
n1 = int(s1)
print(type(n1))
print(n1)

# Type Cast int to float and string
# integer
n = 100

# float
f = float(n)
print(type(f))
print(f)

# string
s = str(n)
print(type(s))
print(s)
