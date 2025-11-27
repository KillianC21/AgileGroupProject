#social personal assessment test
#Social and Personal traits  - How a person interacts with others
    #social energy
    #talkativeness
	#party liking
	#leadership
#Covers how they interact in conversations, groups, and leadership roles

def social_personal_assessment():
    print("Social Personal Assessment")
    print("This assessment will help us understand your Social traits.")
    print("Please answer the following questions honestly.")
    print("You will be asked to rate each statement on a scale from 1 (Strongly Disagree) to 10 (Strongly Agree).")

    questions = [
        "I enjoy social gatherings.",
        "I engage in conversations with strangers.",
        "I enjoy going to parties.",
        "I often take the lead in group settings."
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

