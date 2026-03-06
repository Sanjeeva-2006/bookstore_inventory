import json

# -----------------------------
# Task 1: Read the inventory
# -----------------------------

# Open the JSON file and load its contents
with open("inventory.json", "r") as file:
    inventory = json.load(file)

# Print the number of books
print("Total number of books:", len(inventory))


# -----------------------------
# Task 2: Add a new book
# -----------------------------

new_book = {
    "title": "Atomic Habits",
    "author": "James Clear",
    "price": 14.99,
    "in_stock": True
}

# Add the new book to the inventory list
inventory.append(new_book)

# Save the updated inventory back to the JSON file
with open("inventory.json", "w") as file:
    json.dump(inventory, file, indent=4)


# -----------------------------
# Task 3: Display updated inventory
# -----------------------------

# Read the updated file again
with open("inventory.json", "r") as file:
    updated_inventory = json.load(file)

print("\nUpdated Inventory:\n")

# Print each book in required format
for book in updated_inventory:
    print(f"Title: {book['title']} | Author: {book['author']} | Price: ${book['price']}")