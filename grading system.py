def get_grade(score):
    """
    Function to determine the South African grade based on percentage score.

    Grading scale:
    - 80-100%: 7 (Outstanding)
    - 70-79%: 6 (Meritorious)
    - 60-69%: 5 (Substantial)
    - 50-59%: 4 (Moderate)
    -40-49%: 3 (Adequate)
    - 30-39%: 2 (Elementary)
    - 0-29%: 1 (Not Achieved)

    Args:
    score (float or int): The percentage score (0-100)

    Returns:
    str: The corresponding grade letter or "Invalid score" if input is invalid
    """
    if not isinstance(score, (int, float)) or score < 0 or score > 100:
        return "Invalid score"

    if score >= 80:
        return "7 (Outstanding)"
    elif score >= 70:
        return "6 (Meritorious)"
    elif score >= 60:
        return "5 (Substantial)"
    elif score >= 50:
        return "4 (Moderate)"
    elif score >= 40:
        return "3 (Adequate)"
    elif score >=30:
        return "2 (Elementary)"
    else:
        return "1 (Not Achieved)"

# Main program
if __name__ == "__main__":
    print("South African Grading System")
    try:
        score_input = float(input("Enter your score (0-100): "))
        if score_input != int(score_input):
            score = round(score_input)
            print(f"Rounded score: {score}")
        else:
            score = score_input
        grade = get_grade(score)
        print(f"You got level {grade}")
    except ValueError:
        print("Invalid input. Please enter a number between 0 and 100.")