from django.urls import path

from . import views
from .views import update_location

# urls for the App "category" within the project "team_planner"

urlpatterns = [
    path('location<int:id>', views.locdet, name="locationdetail"),
    path('location<int:id>', views.locdetupd, name="locdetupd"),
    path('manager<int:id>', views.mgrdet, name="managerdetail"),
    path('member<int:id>', views.memdet, name="memberdetail"),
    path('team<int:id>', views.teamdet, name="teamdetail"),

    path('new_location', views.new_location, name="newloc"),
    path('location', views.location_list, name="locations"),
    path('update_location', views.update_location, name="updloc"),
    path('updloctest', views.update_location_list, name="updloc_test"),
    path('delete_location', views.delete_location, name="delloc"),


    path('new_manager', views.new_manager, name="newmgr"),
    path('manager', views.manager_list, name="managers"),
    path('update_manager', views.update_manager, name="updmgr"),
    path('delete_manager', views.delete_manager, name="delmgr"),


    path('new_member', views.new_member, name="newmem"),
    path('member', views.member_list, name="members"),
    path('update_member', views.update_member, name="updmem"),
    path('delete_member', views.delete_member, name="delmem"),


    path('new_team', views.new_team, name="newtea"),
    path('team', views.team_list, name="teams"),
    path('update_team', views.update_team, name="updtea"),
    path('delete_team', views.delete_team, name="deltea"),

#    path('update', update_location),
]
