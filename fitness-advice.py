#Fitness advice based on how many days a week the user exercises. 

not_active = "Get up, couch potato!"
active_light = "Okay! Try adding another day or two next week!"
active_medium = "Great job! Let's build a long streak!"
active_heavy = "Excellent work! Now invite your friends and family to exercise with you!"
active_over = "Don't forget that recovery is an important aspect of a good exercise routine!"

response = input("How many days did you exercise this week? ")
activity = int(response)

if activity == 0:
    print(not_active)
elif 1 <= activity <= 2:
    print(active_light)
elif 3 <= activity <= 4:
    print(active_medium)
elif 5 <= activity <= 6:
    print(active_heavy)
else:
    print(active_over)