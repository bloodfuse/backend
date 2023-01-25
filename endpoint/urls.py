from django.urls import path

from .views import (
    AnonymousVisitorsAnalysis,
    AnonymousVisitorsAnalysisGet,
    AllDonors
)

urlpatterns = [
    path('visitors/anonymous', AnonymousVisitorsAnalysis.as_view()),
    path('visitors/anonymous/get', AnonymousVisitorsAnalysisGet.as_view()),
    path('donors', AllDonors.as_view()),
]