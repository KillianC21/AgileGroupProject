#Main function for running tests
import json
# import trained model
import pickle
import os

# import assessment modules
from Questionaires.SocialPersonalAssessment import social_personal_assessment
from Questionaires.CognitiveEmotionalAssessment import cognitive_emotional_assessment
from Questionaires.LifestyleBehavioralAssessment import lifestyle_behavioural_assessment

#import login and sign up modules
from Auth.login import login_system
from Auth.signup import signup_system


#load the trained model
#implement here

FILE_NAME = "users.json"

#load user database with .json
def load_user_db():
   try:
       with open(FILE_NAME, 'r') as f:
           return json.load(f)

   except Exception as e:
         print(f"An error occurred while loading user database: {e}")
         return {}

#save JSON user database
def save_userdb(user_db):
    try:
        with open(FILE_NAME, 'w') as f:
            json.dump(user_db, f)
    except Exception as e:
        print(f"An error occurred while saving user database: {e}")

def conduct_tests():
    total_scores = []
    scores1 = social_personal_assessment()
    scores2 = cognitive_emotional_assessment()
    scores3 = lifestyle_behavioural_assessment()

    print(scores1)
    total_scores.extend(scores1)
    print(scores2)
    total_scores.extend(scores2)
    print(scores3)
    total_scores.extend(scores3)

    # print total scores
    print(total_scores)

def main():
    print("Welcome to PTMack\n"
          "Here you can self assessment yourself\n"
          "The assessment is for a diagonises if you are introvert, extrovert or ambivert.")

    print("\n-- PLEASE BE AWARE --\n"
          "This is not an accurate diagnoises of your personality\n"
          "You will may be asked personal questions.\n"
          "You can use these results at your own accord\n")

    user_db = load_user_db()
    total_scores = []
    while True:
        user_input = input("Do you wish to continue? (Y/N)?").upper()

        if user_input == 'Y':
            print("Great! Let's get started.")
            has_account = input("Do you have an account? (Y/N)?").upper()

            #----LOGIN----
            if has_account == 'Y':
                print("Please log in to continue.")
                if login_system(user_db):
                    login_system(user_db)

                    print("Starting the assessment...\n")

                    # Conduct assessments
                    scores1 = social_personal_assessment()
                    scores2 = cognitive_emotional_assessment()
                    scores3 = lifestyle_behavioural_assessment()

                    print(scores1)
                    total_scores.extend(scores1)
                    print(scores2)
                    total_scores.extend(scores2)
                    print(scores3)
                    total_scores.extend(scores3)

                    #print total scores
                    print(total_scores)

                    # Make prediction
                    # prediction = predict_model.predict([scores])
                    #
                    # print("\n------ ASSESSMENT COMPLETE -----")
                    # print("Based on your responses\n")
                    # print(f"your personality type: {prediction}")
                    # if prediction == ['Extrovert']:
                    #     print("You are outgoing, energetic, and thrive in social situations.\n")
                    # elif prediction == ['Introvert']:
                    #     print("You are reflective, reserved, and prefer solitary activities.\n")
                    #
                    # elif prediction == ['Ambivert']:
                    #     print("You exhibit qualities of both introversion and extroversion, adapting to different situations.\n")
                    #
                    print("--------------------------------\n")
                    print("Thank you for completing the assessment!")
                    break
                else:
                    print("Auth failed")

            elif has_account == 'N':
                print("Please create an account to continue.")

                if signup_system(user_db):
                    #implement signup
                    signup_system(user_db)
                    save_userdb(user_db)



            else:
                print("Invalid option. Please enter 'Y' or 'N'.")

        elif user_input == 'N':
            print("Thank you for visiting PTMack. Goodbye!")
            break

        else:
            print("Invalid option. Please enter 'Y' or 'N'.")


if __name__ == "__main__":
    main()

