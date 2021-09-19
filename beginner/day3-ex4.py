# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if size == "S":
    pizza = 15
if size == "M":
    pizza = 15
if size == "L":
    pizza = 20


if add_pepperoni == "Y":
    if size == "S":
        pizza = pizza +2
    if size == "M" or size == "L":
        pizza = pizza + 3

if extra_cheese == "Y":
    pizza = pizza + 1

print(f"Your total for pizza is ${pizza}.")