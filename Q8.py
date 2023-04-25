#Write a Python program to check whether a list contains a sublist.

food_list=["Vadapav", "Dabeli", "Pizza", "Burger", "Salad"]

#print(food_list)

sublist=["Pizza", "Burger"]
if set(sublist).issubset(set(food_list)):
    print("It contains a sublist")
else:
    print("It does not contain a sublist")

