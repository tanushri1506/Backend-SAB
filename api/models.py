

from django.db import models
from django.core.exceptions import ValidationError



class Contacts(models.Model):
    role = models.CharField(max_length=200, blank=True)
    name = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)

    class Meta:
        verbose_name_plural = "Contacts"

    def __str__(self):
        return self.name or "Unnamed Contact"


class Council(models.Model):
    name = models.CharField(max_length=200)
    post = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
    linkedin = models.URLField(blank=True)
    tenure = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='council/', blank=True, null=True)
    extra_por = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Council"

    def __str__(self):
        return f"{self.name} ({self.tenure})"


class Events(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField(blank=True)
    icon = models.ImageField(upload_to='events/', blank=True, null=True)

    class Meta:
        verbose_name_plural = "Events"

    def __str__(self):
        return self.title


class Gallery(models.Model):
    label = models.CharField(max_length=200)
    image = models.ImageField(upload_to='gallery/')

    class Meta:
        verbose_name_plural = "Gallery"

    def __str__(self):
        return self.label
    

class GalleryPage(models.Model):
    label = models.CharField(max_length=200)
    image = models.ImageField(upload_to='gallery-page/')
    tenure = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = "GalleryPage"

    def __str__(self):
        return self.label


class Workshops(models.Model):
    title = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='workshops/',blank=True)
    venue = models.CharField(max_length=50)
    date = models.DateField()
    fees = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    register_url = models.URLField(blank=True)
    resource_link = models.URLField(blank=True) 

    class Meta:
        verbose_name_plural = "Workshops"

    def __str__(self):
        return self.title

class Pal(models.Model):
    label = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='pal/', blank=True, null=True)

    class Meta:
        verbose_name_plural = "Pal"

    def __str__(self):
        return self.label


class UgCouncil(models.Model):
    name = models.CharField(max_length=200)
    post = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
    linkedin = models.URLField(blank=True)
    photo = models.ImageField(upload_to='ugcouncil/', blank=True, null=True)

    class Meta:
        verbose_name_plural = "UgCouncil"

    def __str__(self):
        return self.name


class PhdDPPC(models.Model):
    role = models.CharField(max_length=100, default="DPPC Representative")
    name = models.CharField(max_length=200)
    post = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
    linkedin = models.URLField(blank=True)
    photo = models.ImageField(upload_to='phd_dppc/', blank=True, null=True)
    extra_por = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "PhdDPPC"

    def __str__(self):
        return self.name


class PhdCPPC(models.Model):
    role = models.CharField(max_length=100, default="CPPC Representative")
    name = models.CharField(max_length=200)
    post = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
    linkedin = models.URLField(blank=True)
    photo = models.ImageField(upload_to='phd_cppc/', blank=True, null=True)
    extra_por = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "PhdCPPC"

    def __str__(self):
        return self.name


class PhdSPPC(models.Model):
    role = models.CharField(max_length=100, default="SPPC Representative")
    name = models.CharField(max_length=200)
    post = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
    linkedin = models.URLField(blank=True)
    photo = models.ImageField(upload_to='phd_sppc/', blank=True, null=True)
    extra_por = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "PhdSPPC"

    def __str__(self):
        return self.name


class LanguageTeam(models.Model):
    name = models.CharField(max_length=200)
    post = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
    linkedin = models.URLField(blank=True)
    photo = models.ImageField(upload_to='language_team/', blank=True, null=True)

    class Meta:
        verbose_name_plural = "LanguageTeam"

    def __str__(self):
        return self.name


class LanguageCourses(models.Model):
    title = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='language-courses/',blank=True)
    venue = models.CharField(max_length=50)
    date = models.DateField()
    fees = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    register_url = models.URLField(blank=True)
    resource_link = models.URLField(blank=True) 

    class Meta:
        verbose_name_plural = "LanguageCourses"

    def __str__(self):
        return self.title


class BranchRepresentative(models.Model):
    role = models.CharField(max_length=100, default="Branch Representative")
    name = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    linkedin = models.URLField(blank=True)
    photo = models.ImageField(upload_to='branch_reps/', blank=True, null=True)
    tenure = models.CharField(max_length=7)
    extra_por = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "BranchRepresentatives"

    def __str__(self):
        return f"{self.name} ({self.tenure})"
    

class Dupc(models.Model):
    role = models.CharField(max_length=100, default="DUPC Representative")
    name = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    linkedin = models.URLField(blank=True)
    photo = models.ImageField(upload_to='dupc/', blank=True, null=True)
    tenure = models.CharField(max_length=7)
    extra_por = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "DUPCs"

    def __str__(self):
        return f"{self.name} ({self.tenure})"


class Carousel(models.Model):
    label = models.CharField(max_length=200)
    image = models.ImageField(upload_to='carousel/')
    link = models.URLField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Carousel"

    def __str__(self):
        return self.label
    

class AcademicSession(models.Model):
    current_year = models.CharField(
        max_length=20,
        unique=True,
        help_text="Example: 2025-26"
    )

    def save(self, *args, **kwargs):
        # Enforce SINGLE ROW
        if not self.pk and AcademicSession.objects.exists():
            raise ValidationError("Only one Academic Session can exist.")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Current Academic Session: {self.current_year}"
    

class RICGallery(models.Model):
    title = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to="ric_gallery/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title or f"RIC Image {self.id}"

class RICCouncil(models.Model):
    name = models.CharField(max_length=200)
    post = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
    linkedin = models.URLField(blank=True)
    tenure = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='ric_council/', blank=True, null=True)

    class Meta:
        verbose_name_plural = "RICCouncil"

    def __str__(self):
        return f"{self.name} ({self.tenure})"




from django.db import models
from django.utils.text import slugify
from django.conf import settings
import qrcode
from io import BytesIO
from django.core.files import File


class Certificate(models.Model):
    GROUP_CHOICES = [
        ("pal", "PAL"),
        ("ug-council", "UG Council"),
        ("phd-council", "PhD Council"),
        ("workshops", "Workshops"),
        ("language", "Language"),
        ("sab-team", "SAB Team"),
        ("ric-team","RIC Team"),
        ("mentor","Mentor")
    ]

    TYPE_CHOICES = [
        ("PAL", "PAL Mentor"),
        ("BR", "Branch Representative"),
        ("DUPC", "DUPC Student Representative"),
        ("DPPC", "DPPC Student Representative"),
        ("CPPC", "CPPC Student Representative"),
        ("SPPC", "SPPC Student Representative"),
        ("WORKSHOP", "Workshop Course"),
        ("LANGUAGE", "Language Course"),
        ("EC", "SAB Executive Council"),
        ("RIC","RIC Executive Committee"),
        ("MENTOR", "Mentor"),
    ]

    recipient_name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    category = models.CharField(max_length=100, blank=True)
    group = models.CharField(max_length=50, choices=GROUP_CHOICES)
    certificate_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    email = models.EmailField(blank=True)
    signed_by = models.TextField(blank=True, null=True)


    session = models.CharField(max_length=50, help_text="Example: 2025-26")
    issue_date = models.DateField()
    last_sent_at = models.DateTimeField(null=True, blank=True)

    certificate_number = models.CharField(
        max_length=20,
        blank=True,
        editable=False,
        help_text="Automatically generated"
    )

    credential_id = models.CharField(
        max_length=100,
        unique=True,
        blank=True
    )

    public_code = models.SlugField(
        max_length=150,
        unique=True,
        blank=True
    )

    certificate_file = models.FileField(
        upload_to="certificates/",
        blank=True,
        null=True
    )

    qr_code = models.ImageField(
        upload_to="certificate_qr/",
        blank=True,
        null=True
    )

    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.recipient_name} - {self.certificate_type} ({self.certificate_number})"

    def generate_certificate_number(self):
        
        last_certificate = (
            Certificate.objects.filter(certificate_type=self.certificate_type)
            .exclude(certificate_number="")
            .order_by("-created_at")
            .first()
        )

        if last_certificate and last_certificate.certificate_number.isdigit():
            next_number = int(last_certificate.certificate_number) + 1
        else:
            next_number = 1

        return f"{next_number:05d}"

    def generate_public_code(self):
        type_map = {
            "PAL": "certificate_pal",
            "BR": "certificate_br",
            "DUPC": "certificate_dupc",
            "DPPC": "certificate_dppc",
            "CPPC": "certificate_cppc",
            "SPPC": "certificate_sppc",
            "WORKSHOP": "certificate_workshop",
            "LANGUAGE": "certificate_language",
            "EC": "certificate_ec",
            "RIC":"certificate_ric",
            "MENTOR":"certificate_mentor"
        }

        prefix = type_map.get(self.certificate_type, "certificate")
        return f"{prefix}_{self.certificate_number}"

    def generate_credential_id(self):
        return f"SAB-{self.certificate_type}-{self.session}-{self.certificate_number}"

    def get_public_url(self):
        return f"{settings.FRONTEND_BASE_URL}/sab/verify/{self.group}/{self.public_code}"

    def generate_qr_code(self):
        public_url = self.get_public_url()

        qr = qrcode.QRCode(
            version=1,
            box_size=10,
            border=4,
        )
        qr.add_data(public_url)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")

        buffer = BytesIO()
        img.save(buffer, format="PNG")
        file_name = f"{self.public_code}_qr.png"

        self.qr_code.save(file_name, File(buffer), save=False)

    def save(self, *args, **kwargs):
        is_new = self.pk is None

        if not self.certificate_number:
            self.certificate_number = self.generate_certificate_number()

        if not self.public_code:
            self.public_code = slugify(self.generate_public_code())

        if not self.credential_id:
            self.credential_id = self.generate_credential_id()

        if not self.category:
            self.category = self.get_group_display()

        super().save(*args, **kwargs)

        if not self.qr_code:
            self.generate_qr_code()
            super().save(update_fields=["qr_code"])



from django.db import models
import uuid

class DataRequest(models.Model):
    REQUEST_TYPES = [
        ("BR", "Branch Representatives"),
        ("DUPC", "DUPC Student Representatives"),
        ("DPPC", "DPPC Student Representatives"),
        ("CPPC", "CPPC Student Representatives"),
        ("SPPC", "SPPC Student Representatives"),
    ]

    email = models.EmailField()
    request_type = models.CharField(max_length=20, choices=REQUEST_TYPES)
    session = models.CharField(max_length=20, blank=True, null=True)

    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    token = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)


class Links(models.Model):
    faq_url = models.URLField()
    feedback_url = models.URLField()

    def __str__(self):
        return "Links"