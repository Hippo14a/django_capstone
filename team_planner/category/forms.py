from django import forms
from .models import Team, Location, Member, Manager

#create a form for location update
class LocationForm(forms.ModelForm):
    #create meta class
    class Meta:
        #specify model to be used
        model = Location
        #specify fields to be used
        fields = [
            "location_name",
            "address_line_1",
            "address_line_2",
            "city",
            "post_code"]

#create a form for manager update
class ManagerForm(forms.ModelForm):
    #create meta class
    class Meta:
        #specify model to be used
        model = Manager
        #specify fields to be used
        fields = [
            "first_name",
            "last_name",
            "employee_number",
            "start_date",
            "internal_phone",
            "internal_email",
            "job_description",
            "team",
            "role",
            "location",
            "gui_type"]

#create a form for member update
class MemberForm(forms.ModelForm):
    #create meta class
    class Meta:
        #specify model to be used
        model = Member
        #specify fields to be used
        fields = [
            "first_name",
            "last_name",
            "employee_number",
            "start_date",
            "internal_phone",
            "internal_email",
            "job_description",
            "team",
            "role",
            "location",
            "gui_type"]

#create a form for team update
class TeamForm(forms.ModelForm):
    #create meta class
    class Meta:
        #specify model to be used
        model = Team
        #specify fields to be used
        fields = [
            "team_name",
            "team_email",
            "team_manager"]

