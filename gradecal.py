"""
Returns the grade of the student.
Takes marks as input and returns the grade.
"""

# Marks      Grade
# 90–100     A+
# 80–89      A
# 70–79      B
# 60–69      C
# 50–59      D
# Below 50   F


students_grades = [
    ("John", 90), ("Marcin", 100), ("Mahwish", 100), ("Roy", 100),
    ("Anna", 70), ("Poul", 60), ("Mark", 75), ("Prabha", 89),
    ("Michael", 50), ("Vannesa", 87)
]

def average():
    """
    Calculates the average.
    """
    total = 0
    count = 0
    for _,grade in (students_grades):
        total += grade
        count += 1
        avg = total / count
    return avg 

def grade_calculator(grade):
    """
    Returns the grade and message based on the student's grade.
    """
    if grade < 0 or grade > 100:
        return "Invalid", "Grade should be between 0 and 100."
    
    if 90 <= grade <= 100:
        return 'A+', "Excellent!"
    elif 80 <= grade <= 89:
        return 'A', "Good job!"
    elif 70 <= grade <= 79:
        return 'B', "Nice Work!"
    elif 60 <= grade <= 69:
        return 'C', "Decent Effort!"
    elif 50 <= grade <= 59:
        return 'D', "Needs improvement!"
    else:
        return 'F', "Work harder next time."

#avg =  average()
print(f"Group Average: {average()}") 

for name, grade in students_grades:
    
    grade_letter, message = grade_calculator(grade) 
    
    print(f"{name}: Grade = {grade_letter} — {message}")









