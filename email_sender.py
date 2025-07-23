import smtplib  # Library to send emails through SMTP
from email.message import EmailMessage

def send_email_to_parent(parent_email, child_name, risk_level, suggestion, short_topic, doctor_details = None):
    """
    This function sends the results to the parent email based on the risk level.
    """

    msg = EmailMessage()  # Create a new empty email object
    msg['Subject'] = f"earlyaid Health Update for {child_name}"  # Subject line
    msg['From'] = "earlyaid.notify@gmail.com"  # This email has been created especially for the earlyaid app
    msg['To'] = parent_email  # Parent's email


    msg.set_content(f"""
Hello User,

Here is the result of {child_name}'s earlyaid health check:

📌 CHILD NAME: {child_name}
🧪 Risk level: {risk_level}

{short_topic}

📌 RECOMMENDATION:
-----------------------
{suggestion}
-----------------------

{doctor_details}

NOTE: earlyaid is a support tool and does not make a real medication diagnosis.
Always consult a licenced doctor for proper diagnosis and treatment.

Thank you for using earlyaid!

Stay healthy,
The Earlyaid Team


—
If you did not sign up for EarlyAid or believe this message was sent to you by mistake, please disregard it. No action is required.
""")

    # Connect to Gmail's SMTP server and send the email securely
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            # Log in using the app's email and App password
            smtp.login("earlyaid.notify@gmail.com", "fvip arbm sebr ptgt")

            # Send the message
            smtp.send_message(msg)

            print(f"Email sent to {parent_email} successfully!")

    except Exception as e:  # Show an error message if there is a fail in sending the email
        print(f"Error: Failed to send email to {parent_email}: {e}")
    except smtplib.SMTPRecipientsRefused:  # Show an error message if the email address is not valid
        print("The email address you entered is invalid. Please enter your email.")