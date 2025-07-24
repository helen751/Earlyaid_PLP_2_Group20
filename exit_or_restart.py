<<<<<<< HEAD
"""
Ask the user if they want to restart the session or exit the application.
Returns True if they want to restart, False if they want to exit.
 """
=======
"""Ask the user if they want to restart the session or exit the application. """
>>>>>>> 7842dab403bd34ffd6304480333384e7813a1c5c

def exit_or_restart():

    while True:
        print("\nWould you like to: ")
        print("1.Exit")
        print("2.Restart the session")
        choice = input("Please select 1 or 2: ").strip()

        if choice == "2":
            return True
        elif choice == "1":
<<<<<<< HEAD
            print("Thank you for using earlyaid.")
            return False
        else:
            print("Invalid choice. Please select 1 or 2.")
=======
            print("Thank you for using Earlyaid.")
            return False
        else:
            print("Invalid choice. Please select 1 or 2.")
>>>>>>> 7842dab403bd34ffd6304480333384e7813a1c5c
