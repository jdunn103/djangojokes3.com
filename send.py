import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangojokes.settings')
import sendgrid
from sendgrid.helpers.mail import To, Mail
from django.conf import settings
from_email='jdunn103@gmail.com'
to_emails='jdunn103@gmail.com'
subject="SendGrid Test"
html_content = '<h1Hello, from SendGrid!</h1'
mail = Mail(
    from_email=from_email,
    to_emails=to_emails,
    subject=subject,
    html_content=html_content
)
try:
    sg = sendgrid.SendGridAPIClient(settings.SENDGRID_API_KEY)
    sg.send(mail)
except Exception as e:
    print(e, e.body, sep="\n\n")