feedback = input("Enter your feedback :")
targeted_words = ["bad","hate","stupid"]

for word in targeted_words :
    feedback = feedback.replace(word,"***")

print("filtered feedback :"+feedback)