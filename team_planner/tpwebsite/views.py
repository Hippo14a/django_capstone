from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


from category.models import Location, Member, Manager, Team



# Admin page
def admin_page(request):
    return HttpResponse("Admin Page login to go here")

#    return render(request, "tpwebsite/landing_page.html",
#                  {"teams": Team()})



# Landing page
def landing_page(request):
    return render(request, "tpwebsite/landing_page.html",
                  {"teams": Team()})


# Teams page
def teams_list_page(request):
    return render(request, "tpwebsite/teams_list_page.html",
                  {"teams": Team()})


def teams_list_page_mem(request):
    return render(request, "tpwebsite/teams_list_page_mem_test.html",
                  {"teams": Team()})


# Create page
def create_page(request):
    return render(request, "tpwebsite/create_page.html",
                  {"teams": Team()})


# Read page
def read_page(request):
    return render(request, "tpwebsite/read_page.html",
                  {"teams": Team()})


# Update page
def update_page(request):
    return render(request, "tpwebsite/update_page.html",
                  {"teams": Team()})


# Delete page
def delete_page(request):
    return render(request, "tpwebsite/delete_page.html",
                  {"teams": Team()})


# Location page
def location_page(request):
    return render(request, "tpwebsite/location_page.html",
                  {"locations": Location()})


# Manager page
def manager_page(request):
    return render(request, "tpwebsite/manager_page.html",
                  {"managers": Manager()})


# Member page
def member_page(request):
    return render(request, "tpwebsite/member_page.html",
                  {"members": Member()})


# Team page
def team_page(request):
    return render(request, "tpwebsite/team_page.html",
                  {"teams": Team()})


# Date page
def date_page(request):
    return HttpResponse("This page was updated at " + str(datetime.now()))


# About page
def about_page(request):
    return HttpResponse("This is the about page for Hippo's Team Planner Capstone Project")


def member_list_tl(request):
    return render(request, "category/members_list_tl.html",
                  {"memlist": Member.objects.all()})
