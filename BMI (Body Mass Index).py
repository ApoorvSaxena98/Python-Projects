# Mass in kg
m = float(input("Enter mass (in kg): "))
# Height in metre
h = float(input("Enter height (in m): "))
# Body Mass Index(BMI) = (m/(h*2))
b = (m/(h*2))

# Approx. values as per Indian Standard
if(b>0):
    if (b<=18.5):                                                              
        print("BMI is: ", b, "\nUnder-Weight\nThoda zyada khaa lia kr khaana")
    elif (b > 18.5 and b<=24.9):
        print("BMI is: ", b, "\nHealthy\n Khaana to theek thaak khaa rha hai")
    elif (b > 24.9 and b <= 30):
        print("BMI is: ", b, "\nOver-Weight\nThoda km khaaya kr")
    elif (b > 30 and b <=35):
        print("BMI is: ", b, "\nObese Category-1\nKitna khayega")
    elif (b > 35 and b<=40):
        print("BMI is: ", b, "\nObese Category-2\nZyada mt khaa")
    elif (b > 40):
        print("BMI is: ", b, "\nSevere Obesity\nZyada mt khaa gubbara bn jayega")
    else:
        print("Enter correct value")
