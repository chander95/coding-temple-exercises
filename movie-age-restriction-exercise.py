#Rating options should be: G, PG, PG-13, and R

g_rating = "This is an infant friendly option. Goo Goo Gaa Gaa!"
pg_rating = "This is a family friendly option. Enjoy fam!"
pg13_rating = "This option suitable for teenagers under the age of 18. Enjoy the film!"
r_rating = "This options is suitable only for adults over the age of 18. Enjoy the film!"

age_str = input("Hello! How old are you? ")
age = int(age_str)

if  0 <= age <= 2:
    print(g_rating)
elif 3 <= age <= 12:
    print(pg_rating)
elif 13 <= age <= 17:
    print(pg13_rating)
elif age >= 18:
    print(r_rating)
else:
    print("I'm sorry, I do not understand. Please enter your age in numerical value. e.i. 15")
