grades = [75, 82, 68, 90, 55]

print("Current grades:", grades)

index = int(input("Enter the index position to update (0-4): "))

new_grade = int(input("Enter the new grade: "))

grades[index] = new_grade

print("Corrected list:", grades)