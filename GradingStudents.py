def gradingStudents(grades):
    # Write your code here
    result = []
    for grade in grades:
        rem = grade%5
        toAdd = 5 - rem
        multipleOf5 = grade + toAdd
        if grade < 38:
            result.append(grade)
        elif multipleOf5 - grade < 3:
            result.append(multipleOf5)
        else:
            # no rounding
            result.append(grade)
    
    return result



grades = [73,67,38,33]
result = gradingStudents(grades)

print(result)  # required result [75,67,40,33]