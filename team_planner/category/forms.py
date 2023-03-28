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


