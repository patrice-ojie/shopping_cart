"""The purpose of this project is to create a shopping cart application for an all-encompassing store. Users will be
able to add items, remove items, view the total cost, and checkout"""


def shopping_cart(items, prices):
    print("\nThis is your shopping cart:\n")
    for i in range(len(items)):
        print(f"{items[i]}: £{prices[i]:.2f}")


# TODO 1: Create empty lists for items and prices
items = []
prices = []

# TODO 2: Opening greeting for users
print("Welcome to Everything Store! The store where anything you can possibly think of can be bought!\n")
print("This is your shopping cart:")

# TODO 3: Present options for the users and invite user to choose
while True:
    print("\nHere are your options:\n1. Add an item to your cart\n2. Remove an item from your cart\n3. View the total "
          "cost of your cart\n4. Checkout\n")
    while True:
        try:
            choice = int(input("Please enter the number of the option you would like to choose: "))
            if choice > 4:
                print("You have entered an invalid choice. Please try again.")
            else:
                break
        except Exception:
            print("You have entered an invalid choice. Please try again.")
    # TODO 4: Execute the options
    if choice == 1:
        item = input("What would you like to add to your cart? ")
        items.append(item.lower())
        while True:
            try:
                price = float(input("How much does the item cost? £"))
                break
            except Exception:
                print("You have entered an invalid price. Please try again.")
        prices.append(price)
        print(f"\n{item} has been added to your shopping cart successfully.")
        shopping_cart(items, prices)
    elif choice == 2:
        remove = input("What would you like to remove from your cart? ")
        if remove.lower() in items:
            index = items.index(remove)
            items.remove(remove)
            prices.pop(index)
            print(f"\n{remove} has been removed from your cart successfully.")
            shopping_cart(items, prices)
        else:
            print("That item is not in your cart.")
    elif choice == 3:
        total_cost = sum(prices)
        shopping_cart(items, prices)
        print(f"\nThe total cost of your shopping cart is £{total_cost:.2f}")

    # TODO 5: While loop for users to choose again until they checkout
    else:
        shopping_cart(items, prices)
        print("\nThank you for shopping at Everything Store!")
        break
