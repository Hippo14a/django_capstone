from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.forms import modelform_factory
from .models import Team, Location, Member, Manager
from .forms import LocationForm, ManagerForm, MemberForm, TeamForm
from django.contrib import messages


# LOCATION section
# Add location
NewLocationForm = modelform_factory(Location, exclude=[])
def new_location(request):
    if request.method == "POST":
        form = NewLocationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "New location added successfully")
            return redirect("newloc")
    else:
        form = NewLocationForm()
    return render(request, "category/locations_new.html", {"form": form})

# list an individual location's details
def locdet(request, id):
    location = get_object_or_404(Location, pk=id)
    return render(request, "category/locations_detail.html", {"location": location})

# list all locations
def location_list(request):
    return render(request, "category/locations_list.html",
                  {"loclist": Location.objects.all()})


# selection list of all locations for update
def update_location(request):
# hmtl file name refactored / renamed 29th am
    return render(request, "category/locations_update_list.html",
                  {"loclist": Location.objects.all()})

# update selected location
def update_existing_location(request, id):
    #dictionary for initial data with fields names as keys
#    context ={}
    #fetch the object related to passed id
    location = get_object_or_404(Location, pk=id)
    # pass the object as instance in form
    form = LocationForm(request.POST or None, instance = location)
    #save the data from the form and redirect to "empty location update page"
    if form.is_valid():
        form.save()
        messages.success(request, "Location amendment(s) added successfully")
        return redirect("updloc")
    else:
        form= LocationForm()
    return render(request, "category/locations_update_selection.html", {"form": form})


# selection list of all locations for delete

def delete_location(request):
    return render(request, "category/locations_delete_list.html",
                  {"loclist": Location.objects.all()})


# list the detail of the location selected for deletion for final review
def delete_existing_location(request, id):
    location = get_object_or_404(Location, pk=id)
    return render(request, "category/locations_delete_selection.html", {"location": location})

# delete the location
def delete_location_specific(request, id):
    location = get_object_or_404(Location, pk=id)
    location.delete()
    return redirect("landing_page")
    return render(request, "category/locations_delete_list.html",
                  {"loclist": Location.objects.all()})


# MANAGER section

# Add Manager
NewManagerForm = modelform_factory(Manager, exclude=[])
def new_manager(request):
    if request.method == "POST":
        form = NewManagerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "New manager added successfully")
            return redirect("newmgr")
    else:
        form = NewManagerForm()
    return render(request, "category/managers_new.html", {"form": form})


# list an individual managers details
def mgrdet(request, id):
    manager = get_object_or_404(Manager, pk=id)
    return render(request, "category/managers_detail.html", {"manager": manager})

# list all managers
def manager_list(request):
    return render(request, "category/managers_list.html",
                  {"mgrlist": Manager.objects.all()})

# selection list of all managers for update
def update_manager(request):
    return render(request, "category/managers_update_list.html",
                  {"mgrlist": Manager.objects.all()})


# update selected manager
def update_existing_manager(request, id):
    #dictionary for initial data with fields names as keys
    context ={}
    #fetch the object related to passed id
    manager = get_object_or_404(Manager, pk=id)
    # pass the object as instance in form
    form = ManagerForm(request.POST or None, instance = manager)
    #save the data from the form and redirect to "empty location update page"
    if form.is_valid():
        form.save()
        messages.success(request, "Manager amendment(s) added successfully")
        return redirect("updmgr")
    else:
        form= LocationForm()
    return render(request, "category/managers_update_selection.html", {"form": form})


# selection list of all managers for delete

# delete Manager
def delete_manager(request):
    return render(request, "category/managers_delete_list.html",
                  {"mgrlist": Manager.objects.all()})


# list the detail of the location selected for deletion for final review
def delete_existing_manager(request, id):
    manager = get_object_or_404(Manager, pk=id)
    return render(request, "category/managers_delete_selection.html", {"manager": manager})

# delete the manager
def delete_manager_specific(request, id):
    manager = get_object_or_404(Manager, pk=id)
    manager.delete()
    return redirect("landing_page")
    return render(request, "category/managers_delete_list.html",
                  {"mgrlist": Manager.objects.all()})






# list the detail of the manager selected for deletion for final review




# MEMBER section

# Add Member
NewMemberForm = modelform_factory(Member, exclude=[])
def new_member(request):
    if request.method == "POST":
        form = NewMemberForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "New member added successfully")
            return redirect("newmem")
    else:
        form = NewMemberForm()
    return render(request, "category/members_new.html", {"form": form})

# list an individual members details
def memdet(request, id):
    member = get_object_or_404(Member, pk=id)
    return render(request, "category/members_detail.html", {"member": member})


# list all members
def member_list(request):
    return render(request, "category/members_list.html",
                  {"memlist": Member.objects.all()})


# selection list of all members for update
def update_member(request):
    return render(request, "category/members_update_list.html",
                  {"memlist": Member.objects.all()})

# update selected member
def update_existing_member(request, id):
    #dictionary for initial data with fields names as keys
    context ={}
    #fetch the object related to passed id
    member = get_object_or_404(Member, pk=id)
    # pass the object as instance in form
    form = MemberForm(request.POST or None, instance = member)
    #save the data from the form and redirect to "empty location update page"
    if form.is_valid():
        form.save()
        messages.success(request, "Member amendment(s) added successfully")
        return redirect("updmem")
    else:
        form= LocationForm()
    return render(request, "category/members_update_selection.html", {"form": form})



# selection list of all members for delete

# delete Member
def delete_member(request):
    return render(request, "category/members_delete_list.html",
                  {"memlist": Member.objects.all()})


# list the detail of the member selected for deletion for final review
def delete_existing_member(request, id):
    member = get_object_or_404(Member, pk=id)
    return render(request, "category/members_delete_selection.html", {"member": member})

# delete the member
def delete_member_specific(request, id):
    member = get_object_or_404(Member, pk=id)
    member.delete()
    return redirect("landing_page")
    return render(request, "category/members_delete_list.html",
                  {"memlist": Member.objects.all()})


# TEAM section

# Add Team
NewTeamForm = modelform_factory(Team, exclude=[])
def new_team(request):
    if request.method == "POST":
        form = NewTeamForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "New team added successfully")
            return redirect("newtea")
    else:
        form = NewTeamForm()
    return render(request, "category/teams_new.html", {"form": form})

# list an individual teams details

def teamdet(request, id):
    team = get_object_or_404(Team, pk=id)
    return render(request, "category/teams_detail.html", {"team": team})


# list all teams

def team_list(request):
    return render(request, "category/teams_list.html",
                  {"teamlist": Team.objects.all()})



# selection list of all teams for update

# update selected team
def update_existing_team(request, id):
    #dictionary for initial data with fields names as keys
    context ={}
    #fetch the object related to passed id
    team = get_object_or_404(Team, pk=id)
    # pass the object as instance in form
    form = TeamForm(request.POST or None, instance = team)
    #save the data from the form and redirect to "empty location update page"
    if form.is_valid():
        form.save()
        messages.success(request, "Team amendment(s) added successfully")
        return redirect("updtea")
    else:
        form= LocationForm()
    return render(request, "category/teams_update_selection.html", {"form": form})


# selection list of all teams for delete

# delete Team
def delete_team(request):
    return render(request, "category/teams_delete_list.html",
                  {"teamlist": Team.objects.all()})


# list the detail of the team selected for deletion for final review
def delete_existing_team(request, id):
    team = get_object_or_404(Team, pk=id)
    return render(request, "category/teams_delete_selection.html", {"team": team})

# delete the team
def delete_team_specific(request, id):
    team = get_object_or_404(Team, pk=id)
    team.delete()
    return redirect("landing_page")
    return render(request, "category/teams_delete_list.html",
                  {"tealist": Team.objects.all()})



















# update Team
    # selection list of all teams
    # update page for specified team
def update_team(request):
    return render(request, "category/teams_update_list.html",
                  {"teamlist": Team.objects.all()})







# CAR PARK OF STUFF

'''
def locdetupd(request, id):
    location = get_object_or_404(Location, pk=id)
    return render(request, "category/locations_detail_upd.html", {"location": location})
'''

# 29th am'''
# 29th am def update_location(request, id=1):
# next line added 29th am

'''
def locdetupdtest(request, id):
    location = get_object_or_404(Location, pk=id)
    if request.method == "POST":
        form= LocationForm(request.POST, instance=location)
        if form.is_valid():
            form.save()
            messages.success(request, "Location amendment(s) added successfully")
            return redirect("locdetupd")
    else:
        form= LocationForm(instance=location)
    return render(request, "category/locations_detail_upd.html", {"form": form})
'''

'''
def update_location_list(request):
    return render(request, "category/locations_list_upd.html",
                  {"loclist": Location.objects.all()})
'''









