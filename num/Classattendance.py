# Function to check if the student can attend based on their attendance percentage
def check_attendance(attended, missed):
    # Total classes = attended + missed
    total_classes = attended + missed

    # Calculate the attendance percentage
    attendance_percentage = (attended / total_classes) * 100

    # Print the attendance percentage
    print(f"Your attendance percentage is: {attendance_percentage:.2f}%")

    # Check if the attendance percentage is less than 75%
    if attendance_percentage < 75:
        print("Sorry, you cannot attend the next class.")
    else:
        print("You can attend the next class.")

# Ask the student for input
attended_classes = int(input("How many classes have you attended? "))
missed_classes = int(input("How many classes have you missed? "))

# Call the function to check the attendance
check_attendance(attended_classes, missed_classes)