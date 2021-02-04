x = str(input("Enter a Phrase: "))  # User Input Which Can Be Int Type Or Char Type
t = x.split()  # Splitting The Text
a = " " # Used For Spaces If Exists
for i in t:
    a += str(i[0]).upper()
print(a)