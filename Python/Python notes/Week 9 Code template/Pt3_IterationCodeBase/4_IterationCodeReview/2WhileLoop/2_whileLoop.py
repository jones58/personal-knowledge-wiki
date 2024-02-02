num = 0
while num <=20: # checks num value is less than 20
    num+=1 # increment num value by 1
    if num%3 == 0:# used modulus to find numbers between 0 to 20 that are not divisible by 3 without
        continue # continue print all numbers not divisible by 3 without remainder
    print("This number %i is not divisible by 3 "%(num))# returns all number not divisible by three
    


