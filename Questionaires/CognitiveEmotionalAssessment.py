#Section for asking cognitive and emotional assessment questions
#Cognitive and emotional traits -  How a person thinks, feels, and regulates emotions.
    #Empathy
    #Emotional Stability
    #Curiosity
    #Risk Taking
    #Stress Handling

#Covers thinking style, curiosity, and how they handle social tasks.

from Questionaires.CognitiveEmotionalAssessment import cognitive_emotional_assessment


def cognitive_emotional_assessment():
    print("Cognitive and Emotional Assessment")
    print("This assessment will help us understand your cognitive and emotional traits.")
    print("Please answer the following questions honestly.")
    print("You will be asked to rate each statement on a scale from 1 (Strongly Disagree) to 10 (Strongly Agree).")

    questions = [
        "I am able to understand and share the feelings of others.",
        "I remain calm and composed in stressful situations.",
        "I have a strong desire to learn and explore new ideas.",
        "I am willing to take risks to achieve my goals.",
        "I effectively manage stress in my daily life."
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
                    print("Please enter a number between 1 and 5.")

            except ValueError:
                print("Invalid input. Please enter a number between 1 and 5.")

    return scores

