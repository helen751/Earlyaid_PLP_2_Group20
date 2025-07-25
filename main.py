"""
EarlyAid Welcome Interface
This module provides the welcome screen and instructions for the EarlyAid system,
then calls the main user_class.py functionality.
"""


def display_welcome():
    print("=" * 70)
    print("👶🩺 Welcome to Early Aid - Child Health Evaluation System 🩺👶".center(70))
    print("=" * 70)
    print("\nEarly Aid helps caregivers monitor and assess the health of children aged 0 to 12.")
    print("Through guided questions, it detects early signs of illness and advises accordingly.\n")


def display_about():
    print("\nAbout Early Aid:")
    print("Early Aid is a command-line tool designed to help caregivers monitor and assess")
    print("the health of children aged 0 to 12 through symptom-based guided questions.")
    print("It aims to detect early signs of illness, provide risk assessments, and recommend")
    print("appropriate actions including medical consultation.\n")

def show_instructions():
    print("How to use Early Aid:")
    print("1. Register - Create a secure profile to track multiple children and save history.")
    print("2. Login - Access your saved profiles and previous assessments.")
    print("3. Continue as Guest - Perform a quick health check without saving data.\n")
    print("Registration is recommended for a personalized and saved experience.\n")


def main():
    """Main function that displays welcome screen and calls user_class functionality"""
    try:
        # Display welcome screen FIRST
        display_welcome()

        # Wait for user to see the welcome message
        input("\n🚀 Press ENTER to continue to EarlyAid...")
        print("\n" + "=" * 50)

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
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")
        print("   Please contact support or try again.")


if __name__ == "__main__":
    main()

