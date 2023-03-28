from django.contrib import admin

from .models import Location, Member, Role, Team, Manager, Fkey

admin.site.register(Location)
admin.site.register(Member)
admin.site.register(Role)
admin.site.register(Team)
admin.site.register(Manager)
admin.site.register(Fkey)
