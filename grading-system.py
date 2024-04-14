score_input = input("What is your score? ")
num_score = int(score_input)

def grades():
    if num_score >= 90 and num_score <= 150:
        print("You got an A!")
    elif num_score >= 80 and num_score <= 89:
        print("You got a B!")
    elif num_score >= 70 and num_score <= 79:
        print("You got a C!")
    elif num_score >= 60 and num_score <= 69:
        print("You got a D!")
    else:
        print("You failed...")
        
        
grades()
