#this is a weather suggestion program including raining, sunny, windy, humid, and snowing

response = input("Good morning. What is the weather outside? ")

raining = "You should wear a hat, hoodie, raincoat, or take an umbrella with you today!"
sunny = "Great! Sounds like a shorts and sandals kind of day!"
windy = "Careful driving and leave the loose hats at home!"
humid = "Maybe stay indoors with the AC on blast!"
snowing = "Get ready to plow and build snowmen....ugh"

if response == "raining" or response == "Raining":
    print(raining)
elif response == "sunny" or response == "Sunny":
    print(sunny)
elif response == "windy" or response == "Windy":
    print(windy)
elif response == "humid" or response == "Humid":
    print(humid)
elif response == "snowing" or response == "Snowing":
    print(snowing)
else:
    print("Please respond with the following options: raining, sunny, windy, humid, or snowing.")