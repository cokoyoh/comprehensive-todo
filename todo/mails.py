from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings


class Mailer:
    def __init__(self, subject, receiver=[], data={}, sender=None):
        self.subject = subject
        self.sender = sender
        self.receiver = receiver
        self.data = data

    def send(self):
        email_body = render_to_string("emails/default.html", self.data)
        message = EmailMultiAlternatives(
            subject=self.subject,
            from_email=self.sender or settings.SUPPORT_EMAIL,
            to=self.receiver,
        )
        message.attach_alternative(email_body, "text/html")
        message.send()
