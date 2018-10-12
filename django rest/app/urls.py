from django.conf.urls import url, include

from django.urls import path
from app import views

# API endpoints
urlpatterns = [

    path('jobcoach/pendingresumes/', views.pendingResumeOverview, name = "resumeoverview"),
    path('jobcoach/confirmingResume', views.confirmPendingResume, name = "confirmResume"),
    path('chatbotResult', views.datacleaning, name= "datacleaning"),

    path('view1', views.view1),
    #path('view2', views.view2),
    #path('view3', views.view3),
    #path('view4', views.view4),
]

