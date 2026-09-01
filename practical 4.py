print("---Traffic Signal Simulation System ---")

signal=input("Enter the Signal Colour:").lower()

if signal=="red":
    print("Action: STOP")

elif signal=="yellow":
    print("Action: SLOW DOWN")

elif signal=="green":
    print("Action: GO")

else:
    print("Invalid Signal enter Red/Yellow/Green :")