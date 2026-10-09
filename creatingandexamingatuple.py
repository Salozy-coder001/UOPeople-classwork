# Create tuple
borrower = ("John Doe", "B1023", "2025-10-15")

print("Borrower Details:")
print(borrower)

# Attempt to modify tuple
try:
    borrower[0] = "Jane Doe"
except TypeError as e:
    print("Error:", e)

# Length of tuple
print("\nNumber of fields:", len(borrower))

# Display elements using loop
print("\nTuple Elements:")
for item in borrower:
    print(item)