"""team_planner URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from tpwebsite.views import landing_page, create_page, read_page, update_page, delete_page
from tpwebsite.views import location_page, manager_page, member_page, team_page
from tpwebsite.views import date_page, about_page, teams_list_page

# Urls for the project "team_planner" (including the generic paths to include all urls in project Apps)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing_page, name='landing_page'),
    path('home', landing_page, name='landing_page'),
    path('create', create_page, name='create_page'),
    path('read', read_page, name='read_page'),
    path('update', update_page, name='update_page'),
    path('delete', delete_page, name='delete_page'),
    path('tlpage', teams_list_page, name='teams_list_page'),
    path('locn', location_page, name='location_page'),
    path('mngr', manager_page, name='manager_page'),
    path('mebr', member_page, name='member_page'),
    path('team', team_page, name='team_page'),
    path('date', date_page),
    path('about', about_page),
    path('category/', include('category.urls')),
]
