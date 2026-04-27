from django.core.mail import send_mail
from django.conf import settings
from .email_undersign import get_sab_signature
from django.core.mail import EmailMessage


EMAIL_TEMPLATE = """
<div style="font-family: Arial, sans-serif; line-height: 1.6; color: #222;">

    <div style="text-align: center; margin-bottom: 20px;">
        <h2 style="margin: 0; color: #1a237e;">STUDENTS' ACADEMIC BOARD</h2>
        <h3 style="margin: 5px 0; font-weight: normal; color: #444;">
            Acknowledgment of Service
        </h3>
        <p style="margin: 0; font-weight: bold;">
            {tenure_line}
        </p>
    </div>

    <p>Dear <b>{name}</b>,</p>

    <p>
        We are pleased to formally acknowledge your service as the
        <b>{role}</b> for the <b>{post} department</b> {tenure_text}.
    </p>

    <p>
        Your contribution in representing student voices and engaging in academic matters has been highly valuable.
        Through your active involvement, you have helped strengthen the bridge between the student body and the academic administration.
    </p>

    <p>
        We sincerely appreciate your dedication and thank you for your efforts in fulfilling this important responsibility.
    </p>

    <br>

</div>
"""


def send_ack_email(user):
    tenure = getattr(user, "tenure", None)

    if tenure:
        tenure_line = f"FOR THE SESSION {tenure}"
        tenure_text = f"during the academic session {tenure}"
    else:
        tenure_line = ""
        tenure_text = ""

    message = EMAIL_TEMPLATE.format(
        name=user.name,
        post=user.post,
        role=user.role, 
        tenure_line=tenure_line,
        tenure_text=tenure_text
    )

    message += get_sab_signature()

    email = EmailMessage(
        subject=f"Acknowledgment of {user.role} Service",
        body=message,
        from_email=settings.EMAIL_HOST_USER,
        to=[user.email],
    )

    email.content_subtype = "html"  # IMPORTANT

    email.send()