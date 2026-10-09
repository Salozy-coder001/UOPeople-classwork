# Create a list of books
books = ["The Alchemist", "1984", "Moby Dick", "Pride and Prejudice"]

# Add two books
books.append("To Kill a Mockingbird")
books.append("The Great Gatsby")

# Remove a damaged book
books.remove("Moby Dick")

# Sort the list alphabetically
books.sort()

# Display final list
print("Available Books:")
for book in books:
    print(book)
