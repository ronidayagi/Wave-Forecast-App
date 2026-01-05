from app.email_notifier import send_email

to_email = "ohad.amselem@gmail.com"
subject = "Test Email from Surf App"
body = """
Hello Ohad!

This is a test email from Roni's surf forecast app.

If you're reading this, email notifications are working! 🎉

Wave height: 1.5m
Wave direction: 280°
Time: 8:00 AM

Good surfing!
"""

print("Sending test email...")
send_email(to_email, subject, body)
print("Done! Check your inbox!")
