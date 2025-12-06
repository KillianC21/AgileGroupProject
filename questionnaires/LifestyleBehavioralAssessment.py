def lifestyle_behavioural_assessment() -> list[int]:
    """Lifestyle and Behavioral Assessment - How a person lives and behaves in daily life.
    Covers adventurousness, travel interest, teamwork, decision-making, sports interest, and reading habits.

    Returns:
        list[int]: Scores for lifestyle and behavioral traits
    """
    
    print("Lifestyle and Behavioral Assessment")
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
