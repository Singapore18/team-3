from rest_framework import generics
from rest_framework import status
from rest_framework import authentication
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from app.src.utilities import *
from django.http import JsonResponse
from django.shortcuts import render

def pendingResumeOverview(requests): 
    pending_resumes=""
    try:
        pending_resumes = requests.session['pending_resume']     
        confirmed_resumes = requests.session['confirmed_resume']
    except: 
        initializeData(requests)
        pending_resumes = requests.session['pending_resume']
        confirmed_resumes = requests.session['confirmed_resume']

    response ={"pending number": len(pending_resumes),"resumes number": len(confirmed_resumes),"pending" :pending_resumes,"approved" : confirmed_resumes }

    return JsonResponse(response)

def confirmPendingResume(requests):
    resume = requests.GET.get('resumeName')
    pending_resumes = requests.session['pending_resume']     
    confirmed_resumes = requests.session['confirmed_resume']
    confirmed_resumes[resume]= pending_resumes[resume]
    del pending_resumes[resume]
    requests.session['pending_resume'] = pending_resumes
    requests.session['confirmed_resume'] =confirmed_resumes
    response ={"pending number": len(pending_resumes),"resumes number": len(confirmed_resumes),"pending" :pending_resumes,"approved" : confirmed_resumes }

    return JsonResponse(response)

def addNewPendingResume(requests, data):
    print(data)
    pending_resumes = requests.session['pending_resume']
    pending_resumes[data["name"]]= {
        "name" : data["name"],
        "interests" : data["interests"],
        "address" : data["address"],
        "age" : data["age"]
    }
    requests.session['pending_resume'] = pending_resumes
    

def datacleaning(requests):
    interestList = ["bake", "clean", "cook", "dance", "make coffee", "make muffins",
                    "read", "play", "games", "singing", "dancing"]
    interests = []
    nameWhiteList = ["i", "am", "boy"] 
    mrtstations = ["Bedok", "Tampines", "Jurong", "Dhoby Ghaut", "Orchard", "Tanjong Pagar",
                   "Raffles Place"]
    toReturn = {}
    #userdata = request.POST.get['userdata']

    userdata = {"name" : "I am paulina", "interests" : "singing and dancing", "location" : "I live in Bedok", "age": "22" }
    for (key, value) in userdata.items():
        if key == "name":
            nameArray = value.split()
            for i in nameArray:
                if i not in nameWhiteList:    
                    toReturn["name"] = i
            
        elif key == "interests":
            interestArray = value.split()
            for i in interestArray:
                if (i in interestList):
                    interests.append(i)
                toReturn["interests"] = interests
                
        elif key == "address":
            addressArray = value.split()
            for i in addressArray:
                if i in mrtstations:
                    toReturn["address"] = i

        elif key == "age":
            toReturn["age"] = userdata["age"]
           
            #else if ("weekends" in scheduleArray and "all" in scheduleArray):
                #  toReturn[schedule] = "Weekends"
            #else:
                #   scheduler = []
                #  if ("monday" in scheduleArray):
                #     scheduler.append("Monday, ")
                #else if("tuesday" in scheduleArray):
                    #   scheduler.append("Tuesday, ")
                #else if("wednesday" in scheduleArray):
                #    scheduler.append("Wednesday, ")
                #else if("thursday" in scheduleArray):
                    #   scheduler.append("Thursday, ")
                #else if("friday" in scheduleArray):
                    #   scheduler.append("Friday, ")
                #else if("saturday" in scheduleArray):
                    #   scheduler.append("Saturday, ")
                #else if("sunday" in scheduleArray):
                    #   scheduler.append("Sunday")
                #toReturn[schedule] = scheduler
    addNewPendingResume(requests, toReturn)
    pending_resumes = requests.session['pending_resume']
    response ={"pending number": len(pending_resumes),"pending" :pending_resumes }

    return JsonResponse(response)

def view1(requests):
    return render(requests, "index.html", {})
