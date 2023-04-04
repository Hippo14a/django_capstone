from django.shortcuts import render, get_object_or_404, redirect
from django.forms import modelform_factory
from .models import Team, Location, Member, Manager
from .forms import LocationForm, ManagerForm, MemberForm, TeamForm
from django.contrib import messages


# Location section


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

# List an individual location's details


def locdet(request, id):
    location = get_object_or_404(Location, pk=id)
    return render(request, "category/locations_detail.html", {"location": location})

# List all locations


def location_list(request):
    return render(request, "category/locations_list.html",
                  {"loclist": Location.objects.all()})


# Selection list of all locations for update
def update_location(request):
    # Hmtl file name refactored / renamed 29th am
    return render(request, "category/locations_update_list.html",
                  {"loclist": Location.objects.all()})


# Update selected location


def update_existing_location(request, id):
    location = Location.objects.get(id=id)
    if request.method == "POST":
        form = LocationForm(request.POST, instance=location)
        if form.is_valid():
            form.save()
            return redirect("locations")
    else:
        form = LocationForm(instance=location)
    return render(request, "category/locations_update_selection.html", {"form": form})


# Selection list of all locations for delete

def delete_location(request):
    return render(request, "category/locations_delete_list.html",
                  {"loclist": Location.objects.all()})


# List the detail of the location selected for deletion for final review
def delete_existing_location(request, id):
    location = get_object_or_404(Location, pk=id)
    return render(request, "category/locations_delete_selection.html", {"location": location})


# Delete the location


def delete_location_specific(request, id):
    location = get_object_or_404(Location, pk=id)
    location.delete()
    return redirect("location_page")
#    return render(request, "category/locations_delete_list.html",
#                 {"loclist": Location.objects.all()})


# Manager section


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


# List an individual managers details
def mgrdet(request, id):
    manager = get_object_or_404(Manager, pk=id)
    return render(request, "category/managers_detail.html", {"manager": manager})

# List all managers


def manager_list(request):
    return render(request, "category/managers_list.html",
                  {"mgrlist": Manager.objects.all()})


# Selection list of all managers for update


def update_manager(request):
    return render(request, "category/managers_update_list.html",
                  {"mgrlist": Manager.objects.all()})


def update_existing_manager(request, id):
    manager = Manager.objects.get(id=id)
    if request.method == "POST":
        form = ManagerForm(request.POST, instance=manager)
        if form.is_valid():
            form.save()
            return redirect("managers")
    else:
        form = ManagerForm(instance=manager)
    return render(request, "category/managers_update_selection.html", {"form": form})


# Selection list of all managers for delete


# Delete Manager
def delete_manager(request):
    return render(request, "category/managers_delete_list.html",
                  {"mgrlist": Manager.objects.all()})


# List the detail of the manager selected for deletion for final review
def delete_existing_manager(request, id):
    manager = get_object_or_404(Manager, pk=id)
    return render(request, "category/managers_delete_selection.html", {"manager": manager})

# Delete the manager


def delete_manager_specific(request, id):
    manager = get_object_or_404(Manager, pk=id)
    manager.delete()
    return redirect("manager_page")
#    return render(request, "category/managers_delete_list.html",
#                  {"mgrlist": Manager.objects.all()})


# Member section


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

# List an individual members details


def memdet(request, id):
    member = get_object_or_404(Member, pk=id)
    return render(request, "category/members_detail.html", {"member": member})


def memdet_tl(request, id):
    member = get_object_or_404(Member, pk=id)
    return render(request, "category/members_detail_tl.html", {"member": member})


# List all members
def member_list(request):
    return render(request, "category/members_list.html",
                  {"memlist": Member.objects.all()})


# Selection list of all members for update
def update_member(request):
    return render(request, "category/members_update_list.html",
                  {"memlist": Member.objects.all()})


# Update selected member


def update_existing_member(request, id):
    member = Member.objects.get(id=id)
    if request.method == "POST":
        form = MemberForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect("members")
    else:
        form = MemberForm(instance=member)
    return render(request, "category/members_update_selection.html", {"form": form})


# Selection list of all members for delete

# Delete Member
def delete_member(request):
    return render(request, "category/members_delete_list.html",
                  {"memlist": Member.objects.all()})


# List the detail of the member selected for deletion for final review
def delete_existing_member(request, id):
    member = get_object_or_404(Member, pk=id)
    return render(request, "category/members_delete_selection.html", {"member": member})

# Delete the member


def delete_member_specific(request, id):
    member = get_object_or_404(Member, pk=id)
    member.delete()
    return redirect("member_page")
#    return render(request, "category/members_delete_list.html",
#                  {"memlist": Member.objects.all()})


# Team section

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

# List an individual teams details


def teamdet(request, id):
    team = get_object_or_404(Team, pk=id)
    return render(request, "category/teams_detail.html", {"team": team})


# List all teams

def team_list(request):
    return render(request, "category/teams_list.html",
                  {"teamlist": Team.objects.all()})


# Selection list of all teams for update


# Update selected team
def update_existing_team(request, id):
    team = Team.objects.get(id=id)
    if request.method == "POST":
        form = TeamForm(request.POST, instance=team)
        if form.is_valid():
            form.save()
            return redirect("teams")
    else:
        form = TeamForm(instance=team)
    return render(request, "category/teams_update_selection.html", {"form": form})


# Selection list of all teams for delete

# Delete Team
def delete_team(request):
    return render(request, "category/teams_delete_list.html",
                  {"teamlist": Team.objects.all()})


# List the detail of the team selected for deletion for final review
def delete_existing_team(request, id):
    team = get_object_or_404(Team, pk=id)
    return render(request, "category/teams_delete_selection.html", {"team": team})

# Delete the team


def delete_team_specific(request, id):
    team = get_object_or_404(Team, pk=id)
    team.delete()
    return redirect("team_page")
#    return render(request, "category/teams_delete_list.html",
#                  {"tealist": Team.objects.all()})


# Update Team
    # Selection list of all teams
    # Update page for specified team
def update_team(request):
    return render(request, "category/teams_update_list.html",
                  {"teamlist": Team.objects.all()})
