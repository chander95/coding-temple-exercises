#create a traffic light simulation. Green should say "GO!", Yellow should say "SLOW DOWN!", and Red should say "STOP!"

light = input("What color is the light? ")
green = "GO!"
yellow = "SLOW DOWN!"
red = "STOP!"

if light == "Green" or light == "green":
    print(green)
elif light == "Yellow" or light == "yellow":
    print(yellow)
elif light == "Red" or light == "red":
    print(red)
else:
    print("I do not understand. Please respond 'Green', 'Yellow', or 'Red'. ")
