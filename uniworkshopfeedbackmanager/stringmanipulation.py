# ==========================================
# University Workshop Feedback Manager
# ==========================================

# Question 1: String Manipulation

raw_feedback = " THE SPEAKER WAS GREAT but THE ROOM WAS COLD "

# Remove leading/trailing spaces and convert to lowercase
cleaned_feedback = raw_feedback.strip().lower()

# Replace "speaker" with "presenter"
cleaned_feedback = cleaned_feedback.replace("speaker", "presenter")

# Remove extra internal spaces
cleaned_feedback = " ".join(cleaned_feedback.split())

# Convert to title case
final_feedback = cleaned_feedback.title()

# Display final result using an f-string
print("QUESTION 1 OUTPUT")
print(f"Final Feedback: {final_feedback}")


# ==========================================
# Question 2: File Handling
# ==========================================

feedback_list = [
    final_feedback,
    "The Workshop Was Informative And Engaging",
    "The Venue Was Comfortable And Organized"
]

# Write feedback to feedback.txt
with open("feedback.txt", "w") as file:
    for feedback in feedback_list:
        file.write(feedback + "\n")

# Read feedback.txt
print("\nQUESTION 2 OUTPUT")
print("Original Feedback List:")

with open("feedback.txt", "r") as file:
    for line in file:
        print(line.strip())

# Append another feedback message
with open("feedback.txt", "a") as file:
    file.write("Great Session With Useful Examples\n")

# Read updated feedback file
print("\nUpdated Feedback List:")

with open("feedback.txt", "r") as file:
    for line in file:
        print(line.strip())


# ==========================================
# Question 3: Exception Handling
# ==========================================

print("\nQUESTION 3 OUTPUT")

try:
    with open("feedback.txt", "r") as file:
        print("Reading feedback file:")
        for line in file:
            print(line.strip())

except FileNotFoundError:
    print("File not found. Please create feedback.txt first.")

except PermissionError:
    print("Permission denied. Close the file and try again.")

finally:
    print("Operation completed.")


# ==========================================
# Question 4: Feedback Analysis
# ==========================================

# Read all feedback lines
with open("feedback.txt", "r") as file:
    feedback_lines = file.readlines()

# Count total feedback entries
total_feedback = len(feedback_lines)

# Count mentions of the word "great"
great_count = 0

for line in feedback_lines:
    if "great" in line.lower():
        great_count += 1

# Create summary.txt
with open("summary.txt", "w") as file:
    file.write("=== Workshop Feedback Summary ===\n")
    file.write(f"Total Feedback: {total_feedback}\n")
    file.write(f"Mentions of 'Great': {great_count}\n")

# Display summary on the console
print("\nQUESTION 4 OUTPUT")
print("=== Workshop Feedback Summary ===")
print(f"Total Feedback: {total_feedback}")
print(f"Mentions of 'Great': {great_count}")