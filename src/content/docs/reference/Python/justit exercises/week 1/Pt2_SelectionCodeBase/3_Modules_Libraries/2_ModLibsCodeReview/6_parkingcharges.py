import time # Import (module) time
# This module provides various functions to manipulate time values.

# (function) time() -> float
# time() -> floating point number
# Return the current time in seconds since the Epoch. Fractions of a second may be present if the system clock provides them.
startTimeSecs = time.time()

print(startTimeSecs)

# (function) ctime(secs: float | None = ...) -> str
# ctime(seconds) -> string
# Convert a time in seconds since the Epoch to a string in local time. This is equivalent to asctime(localtime(seconds)). 
# When the time tuple is not present, current time as returned by localtime() is used.
formattedStarTime = time.ctime(startTimeSecs)

hours = int(input("Input hours of parking required ( 2, 4, or 12)"))
numInSecs = hours * 60 * 60
if hours == 2:
    parkingCharge = 5.00
elif hours == 4:
    parkingCharge = 8.00
else:
    parkingCharge =15.00
endTimeInSecs = startTimeSecs + numInSecs
print("\nTime now :", formattedStarTime )
endFormattedTimed = time.ctime(endTimeInSecs)
print("Expires On: ", endFormattedTimed)
print(f"Parking Charge = {parkingCharge}")



"Add notes below to explain the application in your own words"