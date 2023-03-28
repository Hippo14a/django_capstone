from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.forms import modelform_factory
from .models import Team, Location, Member, Manager
from .forms import LocationForm
from django.contrib import messages

# list details (field contents) of an individual model element
# list a location's details
def locdet(request, id):
    location = get_object_or_404(Location, pk=id)
    return render(request, "category/locations_detail.html", {"location": location})

def locdetupd(request, id):
    location = get_object_or_404(Location, pk=id)
    return render(request, "category/locations_detail_upd.html", {"location": location})


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









# list a manager's details
def mgrdet(request, id):
    manager = get_object_or_404(Manager, pk=id)
    return render(request, "category/managers_detail.html", {"manager": manager})


# list a member's details
def memdet(request, id):
    member = get_object_or_404(Member, pk=id)
    return render(request, "category/members_detail.html", {"member": member})


# list a team's details
def teamdet(request, id):
    team = get_object_or_404(Team, pk=id)
    return render(request, "category/teams_detail.html", {"team": team})


# list of elements in a model category

# list all locations
def location_list(request):
    return render(request, "category/locations_list.html",
                  {"loclist": Location.objects.all()})

def update_location_list(request):
    return render(request, "category/locations_list_upd.html",
                  {"loclist": Location.objects.all()})



# list all managers
def manager_list(request):
    return render(request, "category/managers_list.html",
                  {"mgrlist": Manager.objects.all()})


# list all members
def member_list(request):
    return render(request, "category/members_list.html",
                  {"memlist": Member.objects.all()})


# list all teams
def team_list(request):
    return render(request, "category/teams_list.html",
                  {"teamlist": Team.objects.all()})


# adding a new element to a model category

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


# Add Manager
NewManagerForm = modelform_factory(Manager, exclude=[])


def new_manager(request):
    if request.method == "POST":
        form = NewManagerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "New manager added successfully")
            return redirect("newman")
    else:
        form = NewManagerForm()
    return render(request, "category/managers_new.html", {"form": form})


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

# update fields in an element of a model category

# locations - note - files etc as per GFG tutorial -
# need to update and rationalise vs NH files
# when tested and all working Ok


# update Location
# selection list of all locations
#placeholder
#def update_location(request):
#    return render(request, "category/locations_update.html",
#                  {"loclist": Location.objects.all()})
#    # update page for specified location


def update_location(request, id):
    #dictionary for initial data with fields names as keys
    context ={}
    #fetch the object related to passed id
    obj = get_object_or_404(Location, pk = id)
    # pass the object as instance in form
    form = LocationForm(request.POST or None, instance = obj)
    #save the data from the form and redirect to "empty location update page"
    # NB used the same code as for new location (as per Pluralsight tutorial)
    if form.is_valid():
        form.save()
        messages.success(request, "Location amendment(s) added successfully")
        return redirect("updloc")
    else:
        form= LocationForm()
    return render(request, "category/locations_update.html", {"form": form})




# update Manager
    # selection list of all managers
    # update page for specified manager
def update_manager(request):
    return render(request, "category/managers_update.html",
                  {"mgrlist": Manager.objects.all()})

# update Member
    # selection list of all members
    # update page for specified member
def update_member(request):
    return render(request, "category/members_update.html",
                  {"memlist": Member.objects.all()})

# update Team
    # selection list of all teams
    # update page for specified team
def update_team(request):
    return render(request, "category/teams_update.html",
                  {"teamlist": Team.objects.all()})



# delete an element of a model category

# delete Location
def delete_location(request):
    return render(request, "category/locations_delete.html",
                  {"loclist": Location.objects.all()})

# delete Manager
def delete_manager(request):
    return render(request, "category/managers_delete.html",
                  {"mgrlist": Manager.objects.all()})

# delete Member
def delete_member(request):
    return render(request, "category/members_delete.html",
                  {"memlist": Member.objects.all()})

# delete Team
def delete_team(request):
    return render(request, "category/teams_delete.html",
                  {"teamlist": Team.objects.all()})
