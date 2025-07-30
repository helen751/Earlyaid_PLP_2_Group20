"""Ask the user if they want to restart the session or exit the application. """
import user_class
import colored_message

coloredMessage = colored_message.ColoredMessage()

#asking the user if they want to restart or exit the app
def exit_or_restart(user_id, user_email):

    while True:
        print("\nWould you like to: ")
        print("0.Exit")
        print("1.Restart the session")
        print("2.Evaluate another child")
        choice = input("Please select 0 - 2: ").strip()

        #calling the user class for restart
        if choice == "1":
            print("\n\n")
            user_class.User().user_acess()

        elif choice == "2":
            print("\n\n")
            user_class.User().child_info(user_id, user_email)
        elif choice == "0":
            coloredMessage.print("\n\tThank you for using EarlyAid. We hope you enjoyed this!\n\n", "blue")
            exit(2)
        else:
            coloredMessage.print("Invalid choice. Please select 1 or 2.", "red")
