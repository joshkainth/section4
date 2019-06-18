cart = []

choice = "yes"

while choice == "yes":
    items = input("Add food item in your cart : ")
    cart.append(items)
    choice = input("Woulde you like to add more item(yes/no) : ")

print("Items added in your cart : ",cart)

#sort food item in cart in ascending order
# without any built in function

for i in range(0,len(cart)):
    print(cart[i])

# Enhanced for loop OR For each-loop
for elm in cart:
    print(elm)

# Explore Same Function in Set and Tuple
