#recommend a type of coffee based on user preferences about sweetness and milk.
print("Welcome to The New England Coffee Bar!")
taste = input("Would you like your coffee sweet or bitter? ")
milk = input("Would you like no milk, little milk, or more milk? ")

bitter_no_milk = "We recommend an espresso"
sweet_no_milk = "We recommend a floral light roast"
sweet_little_milk = "We recommend a caramel cappuccino"
sweet_more_milk = "We recommend a vanilla latte"
bitter_little_milk = "We recommend an espresso macchiato"
bitter_more_milk = "We recommend a cappuccino"

if taste == "sweet" and milk == "no milk":
    print(sweet_no_milk)
elif taste == "sweet" and milk == "little milk":
    print(sweet_little_milk)
elif taste == "sweet" and milk == "more milk":
    print(sweet_more_milk)
elif taste == "bitter" and milk == "no milk":
    print(bitter_no_milk)
elif taste == "bitter" and milk == "little milk":
    print(bitter_little_milk)
elif taste == "bitter" and milk == "more milk":
    print(bitter_more_milk)
else:
    print("I'm sorry, please let me know if you would like your drink sweet or bitter and if you would like no milk, little milk, or more milk.")