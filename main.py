"""
EarlyAid Welcome Interface/ Display Welcome
This module provides the welcome screen, about and instructions for the EarlyAid system,
then calls the main user_class.py functionality.
"""


def display_welcome():
    print(("✨ >_< ✨").center(65))
    print("👶🩺 Welcome to Early Aid - Child Health Evaluation System 🩺👶".center(70))
    print("_" * 70)
    print("\nEarly Aid helps caregivers, monitor and assess the health of children aged 0 to 12.")
    print("Through guided questions, it detects early signs of illness and advises accordingly.\n")


def display_about():
    print("📘ABOUT EARLY AID:\n")
    print("Early Aid is a command-line tool designed to help caregivers assess and monitor")
    print("the health of children aged 0 to 12. It guides users through symptom-based questions,")
    print("analyzes the risk level, and provides personalized advice or urgent care recommendations.\n")

def show_instructions():
    print("🛠️HOW TO USE:\n")
    print("1️⃣  Register - Create a profile to save your children's health assessments.")
    print("2️⃣  Login - Access saved data and continue previous sessions.")
    print("3️⃣  Continue as Guest - Do a one-time health check without saving info.\n")
    print("✨ Tip: Registering gives you personalized suggestions and stores your progress.\n")


def main():
    """Main function that displays welcome screen and calls user_class functionality"""
    try:
        # Display welcome screen FIRST then others
        display_welcome()

        display_about()

        show_instructions()

        # Wait for user to see the welcome message
        input("\n🚀 Press ENTER to continue to EarlyAid...")
        print("\n" + "_" * 50)

        # Import the teammate's user_class module
        from user_class import USER  # Adjust import based on their class name

        # Initialize and run the USER class from teammate's code
        print("Loading EarlyAid system...\n")
        user_system = USER()  # This should handle all the registration/login/guest logic

        # The USER class should handle the rest of the application flow
        # including registration, login, guest mode, and health assessments

    except ImportError as e:
        print("❌ Error: Could not import user_class module.")
        print(f"   Make sure user_class.py is in the same directory.")
        print(f"   Error details: {e}")
    #except Exception as e:
     #   print(f"⚠️ An unexpected error occurred: {e}")
      #  print("   Please contact support or try again.")
 
if __name__ == "__main__":
    main()
