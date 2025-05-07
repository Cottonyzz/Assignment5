import sys

# Global storage (humans often use globals for small scripts)
wishlists = {}

# Help message (less polished than AI)
def show_help():
    print("\n*** Wishlist Manager ***")
    print("create  - Make a new list")
    print("add     - Put stuff in a list")
    print("remove  - Delete stuff (careful!)")
    print("view    - See your lists")
    print("help    - Show this again")
    print("exit/q  - Quit")
    print()

# Menu prompt (casual wording)
def get_command():
    cmd = input("\nWhat now? (create/add/remove/view/help/exit) ").strip().lower()
    return cmd

# Create wishlist (with a simple confirmation)
def create_wishlist():
    name = input("New list name (or 'cancel'): ").strip()
    if name.lower() == 'cancel':
        return
    if name in wishlists:
        print(f"Whoops, '{name}' already exists!")
        return
    confirm = input(f"Create list '{name}'? (y/N): ").lower()
    if confirm == 'y':
        wishlists[name] = []
        print(f"Done! List '{name}' is ready.")
    else:
        print("Never mind then.")

# Add item (with price confirmation)
def add_item():
    if not wishlists:
        print("No lists yet! Make one first.")
        return
    list_name = input("Which list? (or 'cancel'): ").strip()
    if list_name.lower() == 'cancel':
        return
    if list_name not in wishlists:
        print("Uh, that list doesn't exist?")
        return
    item_name = input("Thing to add (or 'cancel'): ").strip()
    if item_name.lower() == 'cancel':
        return
    desc = input("Description (optional): ").strip() or "No description"
    price = input("Price (or '0' if free): ").strip()
    try:
        price_val = float(price)
    except:
        print("Not a number. Setting price to 0.")
        price_val = 0.0
    confirm = input(f"Add '{item_name}' (${price_val:.2f}) to '{list_name}'? (y/N): ").lower()
    if confirm == 'y':
        wishlists[list_name].append((item_name, desc, price_val))
        print("Added!")
    else:
        print("Okay, not adding it.")

# Remove item (with stronger confirmation)
def remove_item():
    if not wishlists:
        print("Nothing to remove, dude.")
        return
    list_name = input("Which list? (or 'cancel'): ").strip()
    if list_name.lower() == 'cancel':
        return
    if list_name not in wishlists:
        print("List not found. Did you typo?")
        return
    items = wishlists[list_name]
    if not items:
        print("List is empty. Nothing to do.")
        return
    print(f"\nItems in '{list_name}':")
    for i, (item, _, _) in enumerate(items, 1):
        print(f"{i}. {item}")
    choice = input("Number to remove (or 'cancel'): ").strip()
    if choice.lower() == 'cancel':
        return
    if not choice.isdigit() or int(choice) < 1 or int(choice) > len(items):
        print("Invalid. Try again.")
        return
    confirm = input(f"Really delete '{items[int(choice)-1][0]}'? (y/N): ").lower()
    if confirm == 'y':
        removed_item = items.pop(int(choice) - 1)
        print(f"Gone forever: '{removed_item[0]}'")
    else:
        print("Phew, close call.")

# View wishlists (unchanged, still casual)
def view_wishlists():
    if not wishlists:
        print("No lists yet. Get creating!")
        return
    print("\n=== YOUR WISHLISTS ===")
    for list_name, items in wishlists.items():
        print(f"\n{list_name.upper()}:")
        for item, desc, price in items:
            print(f" - {item} (${price:.2f}): {desc}")

# Main loop (slightly messy, like human code)
def main():
    print("\nWelcome to Wishlist Manager! (Type 'help' for commands)")
    while True:
        cmd = get_command()
        if cmd in ('create', 'c'):
            create_wishlist()
        elif cmd in ('add', 'a'):
            add_item()
        elif cmd in ('remove', 'r', 'delete'):
            remove_item()
        elif cmd in ('view', 'v', 'ls'):
            view_wishlists()
        elif cmd in ('help', 'h', '?'):
            show_help()
        elif cmd in ('exit', 'quit', 'q'):
            print("Later! Your lists are gone when you quit.")
            sys.exit()
        else:
            print("Huh? Try 'help'.")

if __name__ == "__main__":
    main()
