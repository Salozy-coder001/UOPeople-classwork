# Create borrower tuple
borrower = ("John Doe", "B1023", "2025-10-15")

print("Borrower Details:")
print(borrower)

# Attempt to modify tuple
try:
    borrower[0] = "Jane Doe"
except TypeError as error:
    print("Error:", error)

# Length of tuple
print("Length of tuple:", len(borrower))

# Display each element
print("Tuple Elements:")
for item in borrower:
    print(item)
