# Information about (Maellet)
my_name = "Maellet M. Bundu"
my_age = 24 # Not a lie
my_height = 56 # Inches
my_weight = 100 # lbs
my_eyes = "Black"
my_teeth = "White"
my_hair = "Black"

# Requesting an input from another user
userName = str(input("Please Enter Your Name: "))
userAge = int(input("Your age please: "))
userHeight = int(input("Your height please: "))
userEyesColor = str(input("What is the color of your eyes?: "))
userTeethColor = str(input("What is the color of your teeth?: "))





print(f"Let's talk about {my_name}.")
print(f"He's {my_height} inches tall.")
print(f"He's {my_weight} pounds heavy.")
print(f"Actually that's not too heavy.")
print(f"He's not got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")



# this line is tricky, try to get it exacrly right.
total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height}, and {my_weight} I get {total}.")
