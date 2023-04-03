from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


from category.models import Location, Member, Manager, Role, Team


# Landing page
def landing_page(request):
    return render(request, "tpwebsite/landing_page.html",
                  {"teams": Team.objects.all()})

# Teams page
def teams_list_page(request):
    return render(request, "tpwebsite/teams_list_page.html",
                  {"teams": Team.objects.all()})

# Create page
def create_page(request):
    return render(request, "tpwebsite/create_page.html",
                  {"teams": Team.objects.all()})


# Read page
def read_page(request):
    return render(request, "tpwebsite/read_page.html",
                  {"teams": Team.objects.all()})


# Update page
def update_page(request):
    return render(request, "tpwebsite/update_page.html",
                  {"teams": Team.objects.all()})


# Delete page
def delete_page(request):
    return render(request, "tpwebsite/delete_page.html",
                  {"teams": Team.objects.all()})


# Location page
def location_page(request):
    return render(request, "tpwebsite/location_page.html",
                  {"teams": Team.objects.all()})


# Manager page
def manager_page(request):
    return render(request, "tpwebsite/manager_page.html",
                  {"teams": Team.objects.all()})


# Member page
def member_page(request):
    return render(request, "tpwebsite/member_page.html",
                  {"teams": Team.objects.all()})


# Team page
def team_page(request):
    return render(request, "tpwebsite/team_page.html",
                  {"teams": Team.objects.all()})


# Date page
def date_page(request):
    return HttpResponse("This page was updated at " + str(datetime.now()))



# About page
def about_page(request):
    return HttpResponse("This is the about page for Hippo's Team Planner Capstone Project")

