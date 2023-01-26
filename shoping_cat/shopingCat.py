user_name = input("Enter your name: ")
print(f"Hello {user_name} Please Enter your food choice ")

all_foods = []
all_price = []
total = 0
while True:
 choice_food = input("Enter food (click E to exit) :")


 if choice_food.lower() == "e":
     break
 else:
     price = float(input(f"Enter the price for {choice_food} $:"))
     total += price
     all_foods.append(choice_food)
     all_price.append(price)

print("-------Your cat--------")
for all in all_foods:
    print(all,end=" ")
print(f"\nThe total amount of all your cart is ${total}")
