from rest_framework.generics import ListAPIView
from .models import Contacts, Events,Council,Gallery,GalleryPage, Workshops,Pal,PhdDPPC,PhdCPPC,PhdSPPC,UgCouncil,LanguageTeam,LanguageCourses,BranchRepresentative, Carousel,AcademicSession, DataRequest, Dupc, RICGallery, RICCouncil, Links
from .serializers import (
    ContactsSerializer, 
    EventsSerializer, 
    CouncilSerializer,
      GallerySerializer,
      WorkshopsSerializer,
      PalSerializer,UgCouncilSerializer,
      PhdCPPCSerializer,PhdDPPCSerializer,
      PhdSPPCSerializer,LanguageTeamSerializer,
      LanguageCoursesSerializer,
      BranchRepresentativesSerializer, 
      CarouselSerializer, AcademicSessionSerializer, 
      DupcSerializer,GalleryPageSerializer,
      RICGallerySerializer, RICCouncilSerializer)
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils.timezone import now
from django.conf import settings
from django.core.mail import send_mail

from django.shortcuts import get_object_or_404
from .models import Certificate
from .serializers import CertificateSerializer

class Contacts(ListAPIView):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer

class Events(ListAPIView):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer


class CouncilListView(ListAPIView):
    serializer_class = CouncilSerializer

    def get_queryset(self):
        tenure = self.request.GET.get("tenure")

        if tenure == "all":
            return Council.objects.all().order_by("-tenure")

        if tenure:
            return Council.objects.filter(tenure=tenure)

        # Default → use AcademicSession
        session = AcademicSession.objects.first()
        if session:
            return Council.objects.filter(tenure=session.current_year)

        return Council.objects.none()

class GalleryPageView(ListAPIView):
    queryset = GalleryPage.objects.all()
    serializer_class = GalleryPageSerializer

    def get_queryset(self):
        tenure = self.request.GET.get("tenure")

        if tenure == "all":
            return GalleryPage.objects.all().order_by("-tenure")

        if tenure:
            return GalleryPage.objects.filter(tenure=tenure)

        session = AcademicSession.objects.first()
        if session:
            return GalleryPage.objects.filter(tenure=session.current_year)

        return GalleryPage.objects.none()


class Gallery(ListAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer


class Pal(ListAPIView):
    queryset = Pal.objects.all()
    serializer_class = PalSerializer

class UgCouncil(ListAPIView):
    queryset = UgCouncil.objects.all()
    serializer_class = UgCouncilSerializer

class PhdDPPC(ListAPIView):
    queryset = PhdDPPC.objects.all()
    serializer_class = PhdDPPCSerializer

class PhdCPPC(ListAPIView):
    queryset = PhdCPPC.objects.all()
    serializer_class = PhdCPPCSerializer

class PhdSPPC(ListAPIView):
    queryset = PhdSPPC.objects.all()
    serializer_class = PhdSPPCSerializer

class LanguageTeam(ListAPIView):
    queryset = LanguageTeam.objects.all()
    serializer_class = LanguageTeamSerializer

class LanguageCoursesView(ListAPIView):
    def get(self, request):
        today = now().date()

        upcoming = LanguageCourses.objects.filter(date__gte=today).order_by("date")
        previous = LanguageCourses.objects.filter(date__lt=today).order_by("-date")

        return Response({
            "upcoming": LanguageCoursesSerializer(
                upcoming,
                many=True,
                context={"request": request}
            ).data,
            "previous": LanguageCoursesSerializer(
                previous,
                many=True,
                context={"request": request}
            ).data
        })


class BranchRepresentatives(ListAPIView):
    serializer_class = BranchRepresentativesSerializer

    def get_queryset(self):
        session = AcademicSession.objects.first()
        tenure = self.request.GET.get(
            "tenure",
            session.current_year if session else None
        )

        if tenure and tenure.lower() == "all":
            return BranchRepresentative.objects.all()
        return BranchRepresentative.objects.filter(tenure=tenure)

class DupcView(ListAPIView):
    serializer_class = DupcSerializer

    def get_queryset(self):
        session = AcademicSession.objects.first()
        tenure = self.request.GET.get(
            "tenure",
            session.current_year if session else None
        )

        if tenure and tenure.lower() == "all":
            return Dupc.objects.all()
        return Dupc.objects.filter(tenure=tenure)

class CarouselListView(ListAPIView):
    queryset = Carousel.objects.all()
    serializer_class = CarouselSerializer

class AcademicSessionView(APIView):
    def get(self, request):
        session = AcademicSession.objects.first()
        return Response({
            "current_year": session.current_year if session else None
        })
    
class WorkshopListView(APIView):
    def get(self, request):
        today = now().date()

        upcoming = Workshops.objects.filter(date__gte=today).order_by("date")
        previous = Workshops.objects.filter(date__lt=today).order_by("-date")

        return Response({
            "upcoming": WorkshopsSerializer(
                upcoming,
                many=True,
                context={"request": request}
            ).data,
            "previous": WorkshopsSerializer(
                previous,
                many=True,
                context={"request": request}
            ).data
        })


class CertificateDetailView(APIView):
    def get(self, request, group, public_code):
        certificate = get_object_or_404(
            Certificate,
            group=group,
            public_code=public_code,
            is_active=True
        )

        serializer = CertificateSerializer(
            certificate,
            context={"request": request}
        )
        return Response(serializer.data)
    
from django.utils import timezone
from datetime import timedelta
from django.http import JsonResponse
from django.core.mail import EmailMessage
from django.views.decorators.csrf import csrf_exempt
import json
from django.core.mail import EmailMultiAlternatives
from .utils.email_undersign import get_sab_signature

@csrf_exempt
def send_certificate_email(request):
    if request.method != "POST":
        return JsonResponse({"error": "Invalid request"}, status=400)

    try:
        data = json.loads(request.body)
        credential_id = data.get("credential_id")

        certificate = Certificate.objects.get(credential_id=credential_id)

        if not certificate.email:
            return JsonResponse({"error": "No email registered"}, status=400)

        if certificate.last_sent_at:
            if timezone.now() - certificate.last_sent_at < timedelta(days=7):
                return JsonResponse(
                    {"error": "Certificate download limit exceeded"},
                    status=429
                )

        email = EmailMultiAlternatives(
            subject="Your Certificate from Students' Academic Board IITG",
            from_email=settings.EMAIL_HOST_USER,
            to=[certificate.email],
        )
 
        special_types = ["BR", "DUPC", "DPPC", "CPPC", "SPPC"]

        if certificate.certificate_type in special_types:
            position_line = f"Position of Responsibility: {certificate.get_certificate_type_display()}, {certificate.designation}"
        else:
            position_line = f"Position of Responsibility: {certificate.designation}, {certificate.get_certificate_type_display()}"

        html_content = f"""
        <p>
        This certificate was awarded to <b>{certificate.recipient_name}</b> by the Students' Academic Board, IIT Guwahati.
        </p>

        <p><b>Details</b><br>
        Name: {certificate.recipient_name}<br>
        {position_line}<br>
        Tenure: {certificate.session}
        </p>

        <p> We sincerely acknowledge their dedication and valuable service to the Students' Academic Board during the stated tenure.</p>

        <p>Their contribution is duly recognised and appreciated.</p>
        """

        html_content += get_sab_signature()

        email.attach_alternative(html_content, "text/html")

        email.attach_file(certificate.certificate_file.path)

        email.send()

        certificate.last_sent_at = timezone.now()
        certificate.save()

        return JsonResponse({"success": "Certificate sent to email"})

    except Certificate.DoesNotExist:
        return JsonResponse({"error": "Certificate not found"}, status=404)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
    

class RICGalleryView(ListAPIView):
    serializer_class = RICGallerySerializer

    def get_queryset(self):
        return RICGallery.objects.all().order_by("-uploaded_at")

class RICCouncilListView(ListAPIView):
    serializer_class = RICCouncilSerializer

    def get_queryset(self):
        tenure = self.request.GET.get("tenure")

        if tenure == "all":
            return RICCouncil.objects.all().order_by("-tenure")

        if tenure:
            return RICCouncil.objects.filter(tenure=tenure)

        # Default → use AcademicSession
        session = AcademicSession.objects.first()
        if session:
            return RICCouncil.objects.filter(tenure=session.current_year)

        return RICCouncil.objects.none()


import csv
from io import StringIO
from django.core.mail import EmailMessage
from django.http import HttpResponse
from .utils.data_generators import DATA_HANDLERS
from django.core.mail import EmailMessage

import os

FRONTEND_BASE_URL = os.environ.get("FRONTEND_BASE_URL")

@csrf_exempt
def create_request(request):
    data = json.loads(request.body)

    email = data.get("email")
    request_type = data.get("type")
    session = data.get("session")

    if not email or not request_type:
        return JsonResponse({"error": "Missing fields"}, status=400)

    req = DataRequest.objects.create(
        email=email,
        request_type=request_type,
        session=session,
    )

    approval_link = f"{FRONTEND_BASE_URL}/api/approve/{req.id}/?token={req.token}"

    html_content = f"""
<b>This is an automated request from www.iitg.ac.in/sab</b><br><br>

A new request has been submitted with the following details:<br><br>

• <b>Email:</b> {email}<br>
• <b>Request Type:</b> {req.get_request_type_display()}<br>
• <b>Session:</b> {session}<br>
• <b>Request Time:</b> {timezone.localtime(req.created_at).strftime("%d %B %Y, %I:%M %p")}<br><br>

To review and take action, use the link below:<br>
<a href="{approval_link}">{approval_link}</a><br><br>

<i>This link will expire in 5 days.</i>
"""
    
    html_content += get_sab_signature()

    email_obj = EmailMessage(
        subject=f"New {req.get_request_type_display()} Data Request Received",
        body=html_content,
        from_email=settings.EMAIL_HOST_USER,
        to=[email],
    )


    email_obj.content_subtype = "html"
    email_obj.send()

    return JsonResponse({"success": "Request submitted"})

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from datetime import timedelta

@csrf_exempt
def approve_request(request, request_id):
    req = get_object_or_404(DataRequest, id=request_id)

    token = request.GET.get("token")
    action = request.GET.get("action")

   
    if str(req.token) != token:
        return HttpResponse("❌ Unauthorized access. Invalid or tampered link.")

    if timezone.now() > req.created_at + timedelta(days=5):
        return HttpResponse("❌ This approval link has expired (valid for 5 days only).")


    if action == "cancel":
        return HttpResponse("❌ Request has been cancelled. No data was sent.")

    if request.method == "GET":
        return HttpResponse(f"""
<html>
<body style="text-align:center; margin-top:50px; font-family:sans-serif;">
    <h2>Review Request</h2>

    <p>Please confirm whether you want to approve this request.</p>

    <div style="margin:20px 0;">
        <p><b>Email:</b> {req.email}</p>
        <p><b>Request Type:</b> {req.get_request_type_display()}</p>
        <p><b>Session:</b> {req.session}</p>
    </div>

    <form method="POST">
        <button type="submit" style="padding:10px 20px; background:green; color:white; border:none; border-radius:5px;">
            Approve Request
        </button>
    </form>

    <br><br>

    <a href="/api/approve/{req.id}/?token={req.token}&action=cancel"
       style="color:red; text-decoration:none;">
        Cancel Request
    </a>
</body>
</html>
""")
    if request.method == "POST":
        if req.is_approved:
            return HttpResponse("⚠️ This request has already been approved.")

        handler = DATA_HANDLERS.get(req.request_type)

        if not handler:
            return HttpResponse("❌ Invalid request type provided.")

        csv_data = handler(req.session)

        
        html_content=f"""
<b>This is an automated mail. For any discrepancies, contact us at sab@iitg.ac.in</b><br><br>

Greetings,<br><br>

Your request has been <b>successfully approved</b>.<br><br>

Please find the requested data attached with this email.<br><br>

"""
        html_content += get_sab_signature()
        session_part = f" – {req.session}" if req.session else ""

        email = EmailMessage(
            subject=f"{req.get_request_type_display()} Data{session_part}",
            from_email=settings.EMAIL_HOST_USER,
            to=[req.email],
            body=html_content,
            
        )
        
        email.content_subtype = "html"


        filename = f"{req.request_type.lower()}_data.csv"
        email.attach(filename, csv_data, "text/csv")
        email.send()

        req.is_approved = True
        req.save()

        return HttpResponse("✅ Request approved successfully. Data has been sent via email.")
    


# views.py
from django.http import JsonResponse
from .models import Links

def get_links(request):
    obj = Links.objects.first()

    if not obj:
        return JsonResponse({
            "faq_url": None,
            "feedback_url": None
        })

    return JsonResponse({
        "faq_url": obj.faq_url,
        "feedback_url": obj.feedback_url,
    })

