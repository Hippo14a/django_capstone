from django import forms
from .models import Team, Location, Member, Manager


# Create a form for location update
class LocationForm(forms.ModelForm):
    # Create meta class
    class Meta:
        # Specify model to be used
        model = Location
        # Specify fields to be used
        fields = '__all__'


# Create a form for manager update
class ManagerForm(forms.ModelForm):
    # Create meta class
    class Meta:
        # Specify model to be used
        model = Manager
        # Specify fields to be used
        fields = '__all__'


# Create a form for member update
class MemberForm(forms.ModelForm):
    # Create meta class
    class Meta:
        # Specify model to be used
        model = Member
        # Specify fields to be used
        fields = '__all__'


# Create a form for team update
class TeamForm(forms.ModelForm):
    # Create meta class
    class Meta:
        # Specify model to be used
        model = Team
        # Specify fields to be used
        fields = '__all__'

