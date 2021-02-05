# This code will generate the random string having uppercase, lowercase, digits & special character.
# The length of the string cannot exceeds the number of characters passed

import random
l = int(input("Enter the length of password: "))
s = "~!@#$%^&ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890*()-_=+/*,.<>?:;'~`|"
p = "".join(random.sample(s, l))
print(p)
