from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


from category.models import Location, Member, Manager, Role, Team

def landing_page(request):
    return render(request, "tpwebsite/landing_page.html",
                  {"teams": Team.objects.all()})
'''
the website does not work without all of lines 10 & equivalents
in all CRUD page definitions ... BUT ... adding the code below does not work, so Im not cure why 
or if this has any impact on my urls issue
                  {"managers": Manager.objects.all()},
                  {"members": Member.objects.all()},
                  {"teams": Team.objects.all})
'''

def teams_list_page(request):
    return render(request, "tpwebsite/teams_list_page.html",
                  {"teams": Team.objects.all()})


def create_page(request):
    return render(request, "tpwebsite/create_page.html",
                  {"teams": Team.objects.all()})


def read_page(request):
    return render(request, "tpwebsite/read_page.html",
                  {"teams": Team.objects.all()})

def update_page(request):
    return render(request, "tpwebsite/update_page.html",
                  {"teams": Team.objects.all()})


def delete_page(request):
    return render(request, "tpwebsite/delete_page.html",
                  {"teams": Team.objects.all()})


def location_page(request):
    return render(request, "tpwebsite/location_page.html",
                  {"teams": Team.objects.all()})


def manager_page(request):
    return render(request, "tpwebsite/manager_page.html",
                  {"teams": Team.objects.all()})

def member_page(request):
    return render(request, "tpwebsite/member_page.html",
                  {"teams": Team.objects.all()})


def team_page(request):
    return render(request, "tpwebsite/team_page.html",
                  {"teams": Team.objects.all()})

def date_page(request):
    return HttpResponse("This page was updated at " + str(datetime.now()))


def about_page(request):
    return HttpResponse("This is the about page for Hippo's Team Planner Capstone Project")

