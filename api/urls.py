# urls.py
from django.urls import path
# from .views import Contacts, Events,CouncilListView,Gallery,WorkshopListView,Pal,UgCouncil,PhdDPPC,PhdCPPC,PhdSPPC,LanguageTeam,LanguageCoursesView,BranchRepresentatives,CarouselListView,AcademicSessionView
from .views import (
    Contacts, Events, CouncilListView, Gallery, WorkshopListView, Pal,
    UgCouncil, PhdDPPC, PhdCPPC, PhdSPPC, LanguageTeam, LanguageCoursesView,
    BranchRepresentatives, CarouselListView, AcademicSessionView,
    CertificateDetailView, send_certificate_email, create_request, approve_request, DupcView,
    RICGalleryView, RICCouncilListView, get_links
)

urlpatterns = [
    path('api/contacts/', Contacts.as_view(), name='contacts-list'),
    path('api/events/', Events.as_view(), name='events-list'),
    path('api/council/', CouncilListView.as_view(), name='team-list'),
    path('api/gallery/', Gallery.as_view(), name='gallery-list'),
    path('api/workshops/', WorkshopListView.as_view(), name='workshops-list'),
    path('api/pal/', Pal.as_view(), name='pal'),
    path('api/ug/', UgCouncil.as_view(), name='ug'),
    path('api/dppc/', PhdDPPC.as_view(), name='dppc'),
    path('api/cppc/', PhdCPPC.as_view(), name='cppc'),
    path('api/sppc/', PhdSPPC.as_view(), name='sppc'),
    path('api/language-team/', LanguageTeam.as_view(), name='language-team'),
    path('api/language-courses/', LanguageCoursesView.as_view(), name='language-courses'),
    path('api/branch-reps/', BranchRepresentatives.as_view(), name='branch-reps-list'),
    path('api/dupc/', DupcView.as_view(), name='dupc-list'),
    path('api/carousel/', CarouselListView.as_view(), name='carousel-list'),
    path('api/academic-session/', AcademicSessionView.as_view()),
    path(
    'api/certificates/<slug:group>/<slug:public_code>/',
    CertificateDetailView.as_view(),
    name='certificate-detail'
    ),
    path("api/send-certificate/", send_certificate_email),
    path("api/request/", create_request),
    path("api/approve/<int:request_id>/", approve_request),
    path("api/ric-gallery/", RICGalleryView.as_view()),
    path('api/ric-council/', RICCouncilListView.as_view(), name='ricteam-list'),
    path("api/links/", get_links),
    
]
