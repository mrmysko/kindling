# Problem - Math is only specific to 15 decimals.

import math

while True:
    length = input("Length: ")
    if length.isdigit():
        length = int(length)
        break

# Limit
if length > 200:
    length = 200

print(
    round(
        74725372462738546 * math.sin(math.radians(180) / 74725372462738546),
        int(length),
    )
)
