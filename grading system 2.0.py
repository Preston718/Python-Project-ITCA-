def get_grade(percentage):
    """
    Function to determine the South African grade based on percentage score.

    Grading scale:
    - 80-100%: 7 (Outstanding)
    - 70-79%: 6 (Meritorious)
    - 60-69%: 5 (Substantial)
    - 50-59%: 4 (Moderate)
    - 40-49%: 3 (Adequate)
    - 30-39%: 2 (Elementary)
    - 0-29%: 1 (Not Achieved)

    Args:
    percentage (float or int): The percentage score (0-100)

    Returns:
    str: The corresponding grade level
    """
    if not isinstance(percentage, (int, float)) or percentage < 0 or percentage > 100:
        return "Invalid score"

    if percentage >= 80:
        return "7 (Outstanding)"
    elif percentage >= 70:
        return "6 (Meritorious)"
    elif percentage >= 60:
        return "5 (Substantial)"
    elif percentage >= 50:
        return "4 (Moderate)"
    elif percentage >= 40:
        return "3 (Adequate)"
    elif percentage >= 30:
        return "2 (Elementary)"
    else:
        return "1 (Not Achieved)"


def calculate_overall_grade():
    """
    Function to calculate overall grade from multiple tests.
    Each test has marks obtained and total possible marks.
    """
    print("=" * 50)
    print("South African Grading System - Overall Calculation")
    print("=" * 50)
    
    total_obtained = 0
    total_possible = 0
    test_count = 0
    test_details = []
    
    try:
        num_tests = int(input("How many tests/subjects do you have? "))
        
        if num_tests <= 0:
            print("Please enter a positive number of tests.")
            return
        
        print("\nEnter your marks for each test:")
        print("-" * 50)
        
        for i in range(num_tests):
            print(f"\nTest {i + 1}:")
            total_marks = float(input(f"  How much was the test out of? (total marks): "))
            marks_obtained = float(input(f"  How much did you get? (marks obtained): "))
            
            if marks_obtained < 0 or total_marks <= 0 or marks_obtained > total_marks:
                print("  Invalid input! Marks must be positive and obtained marks <= total marks.")
                return
            
            total_obtained += marks_obtained
            total_possible += total_marks
            test_count += 1
            
            # Calculate percentage for this test
            test_percentage = (marks_obtained / total_marks) * 100
            test_details.append({
                'test_num': i + 1,
                'obtained': marks_obtained,
                'total': total_marks,
                'percentage': test_percentage
            })
        
        # Calculate overall percentage
        overall_percentage = (total_obtained / total_possible) * 100
        
        # Display summary
        print("\n" + "=" * 50)
        print("OVERALL RESULTS SUMMARY")
        print("=" * 50)
        
        print("\nIndividual Test Breakdown:")
        print("-" * 50)
        for test in test_details:
            print(f"Test {test['test_num']}: {test['obtained']:.0f}/{test['total']:.0f} ({test['percentage']:.2f}%)")
        
        print("-" * 50)
        print(f"Total Marks Obtained: {total_obtained:.0f}")
        print(f"Total Possible Marks: {total_possible:.0f}")
        print(f"Overall Percentage: {overall_percentage:.2f}%")
        
        # Check if rounding is needed
        if overall_percentage != int(overall_percentage):
            rounded_percentage = round(overall_percentage)
            print(f"Rounded Percentage: {rounded_percentage}%")
            grade = get_grade(rounded_percentage)
        else:
            rounded_percentage = int(overall_percentage)
            grade = get_grade(rounded_percentage)
        
        print(f"You got level {grade}")
        print("=" * 50)
        
    except ValueError:
        print("Invalid input. Please enter numeric values.")


# Main program
if __name__ == "__main__":
    calculate_overall_grade()
