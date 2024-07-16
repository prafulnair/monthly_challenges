from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse # for dynamic redirection of urls

# HttpResponseRedirect - for redirection of the url

# Create your views here.


challenges_data = {
    "january": "walk everyday for 30 mins",
    "february": "dont w",
    "march": "eat no meat",
    "april": "Gym for 2 hours everyday",
    "may": "Go for swimming everyday",
    "june": "Learn new skills",
    "july": "Celebrate your birthday",
    "august": "No maggi",
    "september": "Learn new Programming language",
    "october" : "Travel to Vancouver",
    "november": "Thank god",
    "december": "celebrate christmas"
}

def monthly_challenges(request, month):
    if month.lower() in challenges_data:
        return HttpResponse(challenges_data[month.lower()])
    
    else:
        return HttpResponseNotFound("This month is not Supported")
    


def monthly_challenges_number(request, month):
    months_list = list(challenges_data.keys())
    month_num = months_list[month-1]

    redirect_path = reverse("month-challenge", args=[month_num]) 
    # basically construct a url dynamically like /challenge/january 
    
    try:
        return HttpResponseRedirect(redirect_path)
    except:
        return HttpResponseNotFound("Enter a valid month or month Number")