def calculate_grade():
    # Initialize variables
    total_points = 0
    total_weight = 0

    # Get input from the user
    while True:
        assignment_type = input("Enter the type of assignment (homework/exams/attendance) or 'done' to finish: ")
        
        if assignment_type.lower() == 'done':
            break
        
        try:
            weight = float(input(f"Enter the weight of{assignment_type} in percentage: "))
            score = float(input(f"Enter your score for {assignment_type}: "))
        except ValueError:
            print("Invalid input. Please enter valid numeric values.")
            continue

        # Update total points and total weight
        total_points += (score * weight / 100)
        total_weight += weight

    # Calculate the average grade
    if total_weight == 0:
        print("No assignments entered. Cannot calculate the average.")
    else:
        average_grade = total_points / total_weight * 100
        print(f"\nYour estimated class grade is: {average_grade:.2f}%")

# Run the program
calculate_grade()
