score = float(input("Enter Graduation Score :"))
backlogs = int(input("Enter number of active backlogs :"))

if score >= 70 and backlogs == 0:
    print("\n Candidate is Eligible for Placement .")
else:
 print("\n Candidate is not Eligible for Placement .")

