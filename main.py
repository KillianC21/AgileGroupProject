import json

# Authentication
from auth.login import login_system
from auth.signup import signup_system

# ML and visualization
from models.predict import predict_personality
from auth.save_patient import save_patient
from visualizations.model_visuals import visualize_feature_importance, visualize_pca_clusters, visualize_trait_means

# Questionnaires
from questionnaires.SocialPersonalAssessment import social_personal_assessment
from questionnaires.CognitiveEmotionalAssessment import cognitive_emotional_assessment
from questionnaires.LifestyleBehavioralAssessment import lifestyle_behavioural_assessment




# USER DATABASE HELPERS
FILE_NAME = "users.json"

def load_user_db():
    try:
        with open(FILE_NAME, 'r') as f:
            return json.load(f)
    except:
        return {}

def save_user_db(user_db):
    with open(FILE_NAME, 'w') as f:
        json.dump(user_db, f, indent=4)


# QUESTIONNAIRE
def run_full_assessment():
    print("\n--- Social & Personal Assessment ---")
    scores_social = social_personal_assessment()

    print("\n--- Cognitive & Emotional Assessment ---")
    scores_cognitive = cognitive_emotional_assessment()

    print("\n--- Lifestyle & Behavioral Assessment ---")
    scores_lifestyle = lifestyle_behavioural_assessment()

    # combine into one list of 15 values
    total_scores = scores_social + scores_cognitive + scores_lifestyle
    return total_scores



# MAIN DOCTOR MENU

def doctor_menu():
    while True:
        print("\n=== Doctor Menu ===")
        print("1. Conduct Personality Test")
        print("2. Feature Importance (Model)")
        print("3. PCA Cluster Plot")
        print("4. Trait Means by Personality Type")
        print("5. Exit")


        choice = input("\nEnter choice: ")

        if choice == "1":
            scores = run_full_assessment()
            prediction = predict_personality(scores)
            print("\nPredicted Personality:", prediction)
            save_patient(scores, prediction)

        elif choice == "2":
            visualize_feature_importance()

        elif choice == "3":
            visualize_pca_clusters()

        elif choice == "4":
            visualize_trait_means()

        elif choice == "5":
            break


        else:
            print("Invalid option. Try again.")


# LOGIN / SIGNUP MENU

def main():
    print("=== Welcome to PTMack Personality Assessment ===\n")

    user_db = load_user_db()

    while True:
        print("1. Login")
        print("2. Signup")
        print("3. Exit")

        option = input("Choose an option: ")

        # LOGIN 
        if option == "1":
            if login_system(user_db):
                print("Login successful! Access granted.")
                doctor_menu()   # ← Enter the assessment menu
                break
            else:
                print("Login failed. Try again.\n")

        # SIGNUP 
        elif option == "2":
            if signup_system(user_db):
                save_user_db(user_db)
                print("Signup complete. You can now log in.\n")

        # EXIT 
        elif option == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Try again.\n")


if __name__ == "__main__":
    main()
