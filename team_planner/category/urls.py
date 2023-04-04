from django.urls import path

from . import views
# from .views import update_location

# urls for the App "category" within the project "team_planner"

urlpatterns = [
    # Url paths for locations
    path('new_location', views.new_location, name="newloc"),
    path('location', views.location_list, name="locations"),
    path('update_location', views.update_location, name="updloc"),
    path('delete_location', views.delete_location, name="delloc"),
    path('delete_location_specific<int:id>', views.delete_location_specific, name="dellocn"),
    path('loclist<int:id>', views.locdet, name="locationdetail"),
    path('locupd<int:id>', views.update_existing_location, name="locationdetupd"),
    path('locdel<int:id>', views.delete_existing_location, name="locationdetdel"),

    # Url paths for managers
    path('new_manager', views.new_manager, name="newmgr"),
    path('manager', views.manager_list, name="managers"),
    path('update_manager', views.update_manager, name="updmgr"),
    path('delete_manager', views.delete_manager, name="delmgr"),
    path('delete_manager_specific<int:id>', views.delete_manager_specific, name="delmngr"),
    path('mgrdel<int:id>', views.delete_existing_manager, name="managerdetdel"),
    path('manlist<int:id>', views.mgrdet, name="managerdetail"),
    path('manupd<int:id>', views.update_existing_manager, name="managerdetupd"),

    # Url paths for members
    path('new_member', views.new_member, name="newmem"),
    path('member', views.member_list, name="members"),
    path('update_member', views.update_member, name="updmem"),
    path('delete_member', views.delete_member, name="delmem"),
    path('delete_member_specific<int:id>', views.delete_member_specific, name="delmemb"),
    path('memdel<int:id>', views.delete_existing_member, name="memberdetdel"),
    path('memlist<int:id>', views.memdet, name="memberdetail"),
    path('memlisttl<int:id>', views.memdet_tl, name="memberdettl"),
    path('memupd<int:id>', views.update_existing_member, name="memberdetupd"),

    # Url paths for teams
    path('new_team', views.new_team, name="newtea"),
    path('team', views.team_list, name="teams"),
    path('update_team', views.update_team, name="updtea"),
    path('delete_team', views.delete_team, name="deltea"),
    path('delete_team_specific<int:id>', views.delete_team_specific, name="delteam"),
    path('teadel<int:id>', views.delete_existing_team, name="teamdetdel"),
    path('tealist<int:id>', views.teamdet, name="teamdetail"),
    path('teaupd<int:id>', views.update_existing_team, name="teamdetupd"),

]
