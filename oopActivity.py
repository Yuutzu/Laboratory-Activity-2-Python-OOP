class Order:
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.items = {}  # dictionary: item -> quantity
        self.prices = {"apple": 30, "banana": 20, "orange": 25, "milk": 50, "bread": 40}

    def add_item(self, item, quantity):
        """Add item to the order"""
        if item not in self.prices:
            raise ValueError(f"Item '{item}' is not available.")
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")
        self.items[item] = self.items.get(item, 0) + quantity
        return f"Added {quantity} {item}(s) to your order."

    def remove_item(self, item, quantity):
        """Remove item from the order"""
        if item not in self.items:
            raise ValueError(f"Item '{item}' is not in your order.")
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")
        if quantity > self.items[item]:
            raise ValueError(f"You only have {self.items[item]} {item}(s) in your order.")
        self.items[item] -= quantity
        if self.items[item] == 0:
            del self.items[item]
        return f"Removed {quantity} {item}(s) from your order."

    def view_order(self):
        """View current order and total bill"""
        if not self.items:
            return "Your order is empty."
        total = sum(self.prices[item] * qty for item, qty in self.items.items())
        details = "\n".join([f"{item} x{qty} = {self.prices[item]*qty} PHP" for item, qty in self.items.items()])
        return f"Order for {self.customer_name}:\n{details}\nTotal: {total} PHP"

def main():
    print("Welcome to the Item Ordering System!")
    name = input("Enter your name: ")
    order = Order(name)

    while True:
        print("\nChoose an action:")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. View Order")
        print("4. Exit")

        try:
            choice = int(input("Enter choice (1-4): "))
            if choice == 1:
                item = input("Enter item name (Apple, Banana, Orange, Milk, Bread): ").lower()
                quantity = int(input("Enter quantity: "))
                print(order.add_item(item, quantity))
            elif choice == 2:
                item = input("Enter item name to remove: ").lower()
                quantity = int(input("Enter quantity to remove: "))
                print(order.remove_item(item, quantity))
            elif choice == 3:
                print(order.view_order())
            elif choice == 4:
                print("Thank you for ordering! Goodbye!")
                break
            else:
                print("Invalid choice. Please select 1-4.")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
