from rest_framework import generics
from rest_framework import status
from rest_framework import authentication
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from app.src.utilities import *
from django.http import JsonResponse

def pendingResumeOverview(requests): 
    pending_resumes=""
    try:
        pending_resumes = requests.session['pending_resume']
    except: 
        initializeData(requests)
        pending_resumes = requests.session['pending_resume']
    #confirmed_resumes = requests.session['confirmed_resume']

    response ={"pending" :pending_resumes, }
    #"approved" : confirmed_resumes }

    return JsonResponse(response)
