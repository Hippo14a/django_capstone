from django.db import models

class Team(models.Model):
    team_name = models.CharField(max_length=20)
    team_email = models.EmailField()
    team_manager = models.CharField(max_length=25)

    def __str__(self):
        return f"{self.team_name}"


class Location(models.Model):
    location_name = models.CharField(max_length=30)
    address_line_1 = models.CharField(max_length=30)
    address_line_2 = models.CharField(max_length=30)
    city = models.CharField(max_length=15)
    post_code = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.location_name}"

class Role(models.Model):
    role_title = models.CharField(max_length=15)
    read_permissions = models.CharField(max_length=15)
    update_permissions = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.role_title}"


class Member(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    employee_number = models.IntegerField()
    start_date = models.DateField()
    internal_phone = models.CharField(max_length=6)
    internal_email = models.EmailField(default="*_*@python-django.com")
    job_description = models.CharField(max_length=15)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    gui_type = models.CharField(max_length=7, default="User")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Manager(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    employee_number = models.IntegerField()
    start_date = models.DateField()
    internal_phone = models.CharField(max_length=6)
    internal_email = models.EmailField(default="*_*@python-django.com")
    job_description = models.CharField(max_length=15)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    gui_type =  models.CharField(max_length=7, default="Manager")


    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Fkey(models.Model):
    fk_title = models.CharField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.fk_title}"


#    room = models.ForeignKey(Room, on_delete=models.CASCADE)

