from django.urls import path
from django.http import HttpResponseRedirect
from django.utils.html import format_html

from .utils.email_service import send_ack_email


class SendMailAdminMixin:
    def send_mail_button(self, obj):
        return format_html(
            '<a class="button" href="{}">Send Mail</a>',
            f'./send-mail/{obj.pk}/'
        )

    send_mail_button.short_description = "Send Mail"

    def get_urls(self):
        urls = super().get_urls()

        custom_urls = [
            path(
                'send-mail/<int:pk>/',
                self.admin_site.admin_view(self.send_mail_view),
                name='send-mail'
            ),
        ]

        return custom_urls + urls

    def send_mail_view(self, request, pk):
        obj = self.model.objects.get(pk=pk)

        send_ack_email(obj)

        self.message_user(request, f"Email sent to {obj.name}")

        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))