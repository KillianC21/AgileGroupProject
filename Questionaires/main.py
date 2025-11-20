#Main function for running tests

# import trained model
import pickle

# import assessment modules
from Questionaires.SocialPersonalAssessment import social_personal_assessment


#load the trained model
#implement here

def main():
    print("Welcome to PTMack\n"
          "Here you can self assessment yourself\n"
          "The assessment is for a diagonises if you are introvert, extrovert or ambivert.")

    print("\n-- PLEASE BE AWARE --\n"
          "This is not an accurate diagnoises of your personality\n"
          "You will may be asked personal questions.\n"
          "You can use these results at your own accord\n")

    try:
        while True:
            user_input = input("Do you wish to continue? (Y/N)").upper()
            try:
                if user_input == 'Y':
                    print("Great! Let's get started.")
                    print("Do you have an account? (Y/N)")
                    has_account = input().upper()
                    if has_account == 'Y':
                        print("Please log in to continue.")
                        # Add login functionality here
                        pass
                        print("Starting the assessment...\n")
                        scores = social_personal_assessment()



                        print(scores)
                        break


                        # Make prediction
                        # prediction = predict_model.predict([scores])
                        #
                        # print("\n------ ASSESSMENT COMPLETE -----")
                        # print("Based on your responses\n")
                        # print(f"your personality type: {prediction}")
                        # if prediction == ['Extrovert']:
                        #     print("You are outgoing, energetic, and thrive in social situations.\n")
                        #
                        # elif prediction == ['Introvert']:
                        #     print("You are reflective, reserved, and prefer solitary activities.\n")
                        #
                        # elif prediction == ['Ambivert']:
                        #     print("You exhibit qualities of both introversion and extroversion, adapting to different situations.\n")

                        print("--------------------------------\n")
                        print("Thank you for completing the assessment!")

                    elif has_account == 'N':
                        print("Please create an account to continue.")
                        # Add account creation functionality here

                    else:
                        print("Invalid option. Please enter 'Y' or 'N'.")

                elif user_input == 'N':
                    print("Thank you for visiting PTMack. Goodbye!")
                    break

                else:
                    print("Invalid option. Please enter 'Y' or 'N'.")

            except Exception as e:
                print(f"An error occurred: {e}")

    except KeyboardInterrupt:
        print("\nProcess interrupted. Exiting the program.")


if __name__ == "__main__":
    main()

