#CognitiveEmotional Assessment
#Lifestyle and Behavioral Traits
    #Adventurousness
    #Travel Desire
    #Work Style Collaborative
    #Decision Speed
    #Sport interest
    #Reading Habit

#Covers routines, and willingness to participate in a hobby.


def lifestyle_behavioural_assessment():
    print("Social Personal Assessment")
    print("This assessment will help us understand your lifestyle and behavioural traits.")
    print("Please answer the following questions honestly.")
    print("You will be asked to rate each statement on a scale from 1 (Strongly Disagree) to 10 (Strongly Agree).")

    questions = [
        "I enjoy trying new and adventurous activities.",
        "I have a strong desire to travel and explore new places.",
        "I prefer working in a collaborative team environment.",
        "I make decisions quickly and confidently.",
        "I have a keen interest in sports and physical activities.",
        "I regularly engage in reading as a hobby."
    ]

    scores = []

    for q in questions:
        while True:
            try:
                score = int(input(f"{q} (1-10): "))
                if 1 <= score <= 10:
                    scores.append(score)
                    break

                else:
                    print("Please enter a number between 1 and 10.")

            except ValueError:
                print("Invalid input. Please enter a number between 1 and 10.")

    return scores
