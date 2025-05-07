import sys

# In-memory data store
wishlists = {}

# ---------------------- Inclusivity Heuristic #1: Explain Benefits ----------------------
def show_new_features():
    print("=== What's New in Wishlist Manager ===")
    print(" • create   : Quickly start organizing a new wishlist to track gifts, groceries, or projects.")
    print(" • add      : Effortlessly add detailed items (name, price, description) to any wishlist.")
    print(" • remove   : Safely remove items with confirmation to avoid accidental deletions.")
    print(" • view     : Instantly view all your wishlists and their items in one place.")
    print(" • help     : Display this menu and learn the benefits of each feature.")
    print(" • exit (q) : Exit the program when you’re done managing your lists.")
    print("=======================================\n")

# ----------------------------- Banner (IH #1 & #2) -------------------------------------
def banner():
    print("Welcome to Wishlist Manager!")                             # IH#1: Purpose & value
    print("Getting started takes ~2 minutes. Because we value your time.")   # IH#2: Communicated cost
    print()

# --------------------------- Main Menu & Interaction ----------------------------------
def show_menu():
    print("Choose an action (by number or name):")                         # IH#4: Familiar conventions
    print(" 1) create    2) add       3) remove")
    print(" 4) view      5) help      6) exit (or 'q')")                       # IH#7: Redundant input methods
    return input("\n> ").strip().lower()

# ------------------------- User Story Implementations --------------------------------
def create_wishlist():
    name = input("Enter new wishlist name (or 'back'): ").strip()
    if name.lower() == "back": return                                       # IH#5: Backtracking
    if name in wishlists:
        print("Error: That wishlist already exists.")                        # QA: Error handling
        return
    wishlists[name] = []
    print(f"Wishlist '{name}' created! Organize your items effectively.")      # US1 Acceptance


def add_item():
    if not wishlists:
        print("No wishlists; create one first.")
        return
    name = input("Wishlist to add into (or 'back'): ").strip()
    if name.lower() == "back": return                                         # IH#5
    if name not in wishlists:
        print("Error: Unknown wishlist.")                                      # QA
        return
    item = input("Item name (or 'back'): ").strip()
    if item.lower() == "back": return                                         # IH#5
    desc = input("Description: ").strip()
    price = input("Price: ").strip()
    try:
        price_val = float(price)
    except ValueError:
        print("Error: Price must be a number.")                               # QA: Error handling
        return
    wishlists[name].append((item, desc, price_val))                            
    print(f"Added '{item}' to '{name}'! You can view your list anytime.")       # US2 Acceptance


def remove_item():
    if not wishlists:
        print("No wishlists; create one first.")
        return
    name = input("Wishlist to remove from (or 'back'): ").strip()
    if name.lower() == "back": return                                         # IH#5
    if name not in wishlists:
        print("Error: Unknown wishlist.")                                      # QA
        return
    items = wishlists[name]
    if not items:
        print("No items to remove.")
        return
    for i, (item, *_ ) in enumerate(items, 1):
        print(f"{i}. {item}")
    idx = input("Number to remove (or 'back'): ").strip()
    if idx.lower() == "back": return                                           # IH#5
    if not idx.isdigit() or not (1 <= int(idx) <= len(items)):
        print("Error: Invalid number.")                                        # QA
        return
    # IH#8: Confirmation prompt for error prevention
    confirm = input(f"Are you sure you want to delete '{items[int(idx)-1][0]}'? (y/N): ").lower()
    if confirm == 'y':
        removed = items.pop(int(idx)-1)
        print(f"Removed '{removed[0]}' successfully.")                        # US3 Acceptance
    else:
        print("Deletion cancelled.")


def view_wishlist():
    if not wishlists:
        print("No wishlists exist.")
        return
    print("\n=== Your Wishlists ===")
    for name, items in wishlists.items():
        print(f"\n{name}:")
        for item, desc, price in items:
            print(f" - {item} (${price:.2f}): {desc}")
    print("======================\n")

# -------------------------- Help with Benefits (IH #1) -------------------------------
def show_help():
    print("\nCommands and Benefits:")
    print(" create  : Create a new wishlist so you can group and organize items easily.")
    print(" add     : Add detailed items (name, price, description) for better tracking.")
    print(" remove  : Remove items safely with confirmation, preventing mistakes.")
    print(" view    : View all your wishlists and items at a glance.")
    print(" help    : Display this help menu and learn why each command is useful.")
    print(" exit(q) : Exit the program when you’re finished.")
    print()

# --------------------------------- Main Loop -----------------------------------------
def main():
    banner()
    show_new_features()  # IH#1: Explain benefits of features
    while True:
        cmd = show_menu()
        if cmd in ('1', 'create'):
            create_wishlist()
        elif cmd in ('2', 'add'):
            add_item()
        elif cmd in ('3', 'remove'):
            remove_item()
        elif cmd in ('4', 'view'):
            view_wishlist()
        elif cmd in ('5', 'help'):
            show_help()
        elif cmd in ('6', 'exit', 'q'):
            print("Goodbye! Remember to come back anytime.")  # IH#7
            sys.exit(0)
        else:
            print("Unknown command; type 'help' to see options.")  # QA

if __name__ == '__main__':
    main()
