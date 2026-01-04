from app.email_notifier import send_email

to_email = "ronygilboa1@gmail.com"
subject = "Test Email from Surf App"
body = """
Hello Rony!

This is a test email from your surf forecast app.

If you're reading this, email notifications are working! 🎉

Wave height: 1.5m
Wave direction: 280°
Time: 8:00 AM

Good surfing!
"""

print("Sending test email...")
send_email(to_email, subject, body)
print("Done! Check your inbox!")
