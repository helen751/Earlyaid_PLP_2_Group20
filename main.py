import user_class
import colored_message
"""
EarlyAid Welcome Interface/ Display Welcome
This module provides the welcome screen, about and instructions for the EarlyAid system,
then calls the main user_class.py functionality.
"""

coloredMessage = colored_message.ColoredMessage()
def display_welcome():
    print("\n\n")
    coloredMessage.print("✨ >_< ✨".center(65), "blue")
    coloredMessage.print("👶🩺 Welcome to Early Aid - Child Health Evaluation System 🩺👶".center(70), "blue")
    print("_" * 70)



def display_about():
    coloredMessage.print("📘ABOUT EARLY AID:\n", "blue")
    print("Early Aid is a command-line tool designed to help caregivers assess and monitor")
    print("the health of children aged 0 to 12. It guides users through symptom-based questions,")
    print("analyzes the risk level, and provides personalized advice or urgent care recommendations.\n")

def show_instructions():
    coloredMessage.print("🛠️HOW TO USE:\n", "blue")
    print("1️⃣  Register - Create a profile to save your children's health assessments.")
    print("2️⃣  Login - Access saved data and continue previous sessions.")
    print("3️⃣  Continue as Guest - Do a one-time health check without saving info.\n")
    coloredMessage.print("✨ Tip: Registering gives you personalized suggestions and stores your progress.\n", "red")


def main():
    """Main function that displays welcome screen and calls user_class functionality"""

    # Display welcome screen FIRST then others
    display_welcome()

    display_about()

    show_instructions()

    # Wait for user to see the welcome message
    input("\n🚀 Press ENTER to continue to EarlyAid...")
    print("\n" + "_" * 50)


    # Initialize and run the USER class from teammate's code
    print("Loading EarlyAid system...\n")
    user_system = user_class.User().user_acess()  # This should handle all the registration/login/guest logic

if __name__ == "__main__":
    main()
