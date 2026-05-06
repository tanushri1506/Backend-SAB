from django.contrib import admin
from django.utils.html import format_html
from .models import (
    Contacts, Events, Council, Gallery, Workshops, Pal, UgCouncil,
    PhdDPPC, PhdCPPC, PhdSPPC, LanguageTeam, LanguageCourses,
    BranchRepresentative, Carousel, AcademicSession, Certificate,
    Dupc,
    RICGallery, RICCouncil, Links, GalleryPage
)
from .admin_mixins import SendMailAdminMixin

admin.site.register(Contacts)
admin.site.register(Events)
admin.site.register(Gallery)
admin.site.register(Workshops)
admin.site.register(Pal)
admin.site.register(UgCouncil)
admin.site.register(LanguageTeam)
admin.site.register(LanguageCourses)
admin.site.register(Carousel)

@admin.register(PhdDPPC)
class PhdDPPCAdmin(SendMailAdminMixin,admin.ModelAdmin):
    list_display = ("name", "post", "send_mail_button")
    search_fields = ("name", "post")

@admin.register(PhdCPPC)
class PhdCPPCAdmin(SendMailAdminMixin,admin.ModelAdmin):
    list_display = ("name", "post", "send_mail_button")
    search_fields = ("name", "post")

@admin.register(PhdSPPC)
class PhdSPPCAdmin(SendMailAdminMixin,admin.ModelAdmin):
    list_display = ("name", "post", "send_mail_button")
    search_fields = ("name", "post")



@admin.register(Council)
class CouncilAdmin(admin.ModelAdmin):
    list_display = ("name", "post", "tenure")
    list_filter = ("tenure",)
    search_fields = ("name", "post")

@admin.register(GalleryPage)
class GalleryPageAdmin(admin.ModelAdmin):
    list_display = ("label", "tenure")
    list_filter = ("tenure",)


@admin.register(BranchRepresentative)
class BranchRepresentativesAdmin(SendMailAdminMixin,admin.ModelAdmin):
    list_display = ("name", "post", "tenure", "send_mail_button")
    list_filter = ("tenure",)
    search_fields = ("name", "post")

@admin.register(Dupc)
class DupcAdmin(SendMailAdminMixin,admin.ModelAdmin):
    list_display = ("name", "post", "tenure", "send_mail_button")
    list_filter = ("tenure",)
    search_fields = ("name", "post")


@admin.register(AcademicSession)
class AcademicSessionAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not AcademicSession.objects.exists()
    

@admin.register(RICGallery)
class RICGalleryAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "uploaded_at")

@admin.register(RICCouncil)
class RICCouncilAdmin(SendMailAdminMixin,admin.ModelAdmin):
    list_display = ("name", "post", "tenure", "send_mail_button")
    list_filter = ("tenure",)
    search_fields = ("name", "post")



@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = (
        "recipient_name",
        "email",
        "certificate_type",
        "group",
        "certificate_number",
        "session",
        "issue_date",
        "is_active",
        "verification_link",
    )

    list_filter = ("group", "certificate_type", "session", "is_active", "is_verified")
    search_fields = ("recipient_name", "designation", "credential_id", "certificate_number", "public_code")

    readonly_fields = (
        "certificate_number",
        "public_code",
        "credential_id",
        "public_url_preview",
        "qr_preview",
        "created_at",
        "category",
    )

    fieldsets = (
        ("Recipient Details", {
            "fields": ("recipient_name", "designation","email")
        }),
        ("Certificate Details", {
            "fields": ("group", "certificate_type", "session", "issue_date", "certificate_number", "signed_by")
        }),
        ("Final Certificate Upload", {
            "fields": ("certificate_file",)
        }),
        ("QR Code", {
            "fields": ("qr_preview",)
        }),
        ("Status", {
            "fields": ("is_active", "is_verified")
        }),
        ("Verification Details", {
            "fields": ("public_code", "credential_id", "public_url_preview", "created_at")
        }),
    )

    def public_url_preview(self, obj):
        if obj.pk:
            return format_html(
                '<a href="{0}" target="_blank">{0}</a>',
                obj.get_public_url()
            )
        return "Will be generated after save"

    public_url_preview.short_description = "Public URL"

    def verification_link(self, obj):
        return obj.public_code

    verification_link.short_description = "Verification Code"

    def qr_preview(self, obj):
        if obj.qr_code:
            return format_html(
                '<a href="{0}" target="_blank">Open QR</a><br><br>'
                '<img src="{0}" width="180" height="180" style="border:1px solid #ddd; padding:5px;" />',
                obj.qr_code.url
            )
        return "QR will be generated after save"

    qr_preview.short_description = "QR Preview"


from .models import Links

@admin.register(Links)
class LinksAdmin(admin.ModelAdmin):
    list_display = ("faq_url", "feedback_url")