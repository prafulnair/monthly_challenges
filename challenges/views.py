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
    try:
        challenge_text = challenges_data[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>Enter a valid Month or Month Number</h1>")
    


def monthly_challenges_number(request, month):
    months_list = list(challenges_data.keys())
    month_num = months_list[month-1]

    redirect_path = reverse("month-challenge", args=[month_num]) 
    # basically construct a url dynamically like /challenge/january 
    
    return HttpResponseRedirect(redirect_path)
