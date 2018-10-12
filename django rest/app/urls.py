from django.conf.urls import url, include

from django.urls import path
from app import views
from django.views.decorators.csrf import csrf_exempt

# API endpoints
urlpatterns = [

    path('jobcoach/pendingresumes/', views.pendingResumeOverview, name = "resumeoverview"),
    path('jobcoach/confirmingResume', views.confirmPendingResume, name = "confirmResume"),
    path('chatbotResult', csrf_exempt(views.datacleaning), name= "datacleaning"),

    path('view1', views.view1),
    #path('view2', views.view2),
    #path('view3', views.view3),
    #path('view4', views.view4),
]

