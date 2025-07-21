import smtplib  # Library to send emails through SMTP
from email.message import EmailMessage

def send_email_to_parent(parent_email, child_name, risk_level, suggestion):
    """
    This function sends the results to the parent email based on the risk level.
    """

    msg = EmailMessage()  # Create a new empty email object
    msg['Subject'] = f"earlyaid Health Update for {child_name}"  # Subject line
    msg['From'] = "earlyaid.notify@gmail.com"  # This email has been created especially for the earlyaid app
    msg['To'] = parent_email  # Parent's email

    # Customize the suggestion based on the risk level
    if risk_level == "High":
        suggestion = (
            "Our assessment indicates that your child's symptoms may require urgent medical attention. "
            "We strongly recommend that you visit a healthcare provider as soon as possible. "
            "Please do not delay in seeking professional care."
        )
    elif risk_level == "Moderate":
        suggestion = (
            "Your child's symptoms may not be critical at the moment, but we encourage you to continue monitoring closely. "
            "If symptoms persist or worsen, consider consulting a healthcare provider for further guidance."
        )
    else:  # Low risk
        suggestion = (
            "Your child's responses suggest that there are no urgent health concerns at the moment. "
            "However, we encourage you to stay attentive and provide care as necessary. "
            "If you notify any unusual symptoms later, please restart another session with the earlyaid app to get more advice."
        )

    msg.set_content(f"""
Hello,
Here is the result of {child_name}'s earlyaid health check:

Risk level: {risk_level}

📌Recommendation:
{suggestion}


NOTE: earlyaid is a support tool and does not make a medication diagnosis.
Always consult a licenced doctor for proper diagnosis and treatment.

Thank you for using earlyaid!
Stay healthy,
-The earlyaid Team
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