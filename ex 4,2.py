status=input("Enter atmospheric status(hot, cold, normal) :").lower()

if status == "hot":
    print("Recommendation : Turn on AC .")
elif status == "cold":
    print("Recommendation : Active heater.")
elif status == "normal":
    print("Recommendation : Keep the system idle.")
else :
 print("Invalid atmosphereic status.")
