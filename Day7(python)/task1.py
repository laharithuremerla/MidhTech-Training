food_item = input(str("Enter your food item(press 'q' to quit):"))
while not food_item=='q':
    print(f"you like {food_item}")
    food_item = input(str("Enter your food item(press 'q' to quit):"))
print("Thank you")

num = int(input("Enter tge food b/w 1-10: "))
while num<1 or num>2:
    print(f" your {num} is invalid")
    num = int(input("Enter a numberb/w 1-10: "))
    print(f"you give review {num}")




