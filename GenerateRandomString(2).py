# This code will only print the random combination of UPPER Case, LOWER Case & Digits
# The length of generated string will be on user choice
# This will surely include all characters & digits in string

import string
import random
N = int(input("Enter the length of string: "))

# generate random strings
res = "".join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k = N))
print("The generated random string : " + str(res))
