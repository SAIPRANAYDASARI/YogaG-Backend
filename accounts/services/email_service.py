from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


class EmailService:

    @staticmethod
    def send_password_reset_email(user, reset_link):

        html_content = render_to_string(
            "emails/password_reset.html",
            {
                "first_name": user.first_name,
                "reset_link": reset_link,
            },
        )

        email = EmailMultiAlternatives(
            subject="YogaG Password Reset",
            body="Please use an HTML supported email client.",
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[user.email],
        )

        email.attach_alternative(
            html_content,
            "text/html",
        )

        try:
            email.send()
        except Exception as e:
            raise Exception(f"Failed to send email: {str(e)}")