from django.conf.urls import url, include

from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken import views as rest_views
from django.urls import path
from app import views

# API endpoints
urlpatterns = format_suffix_patterns([

    path('jobcoach/pendingresumes/', views.pendingResumeOverview, name = "resumeoverview")

])

