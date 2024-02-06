from django.contrib import admin
from .models import Department, Role, Employee

# Register your models here.

admin.site.register(Role)
admin.site.register(Department)

class Employee2(admin.ModelAdmin):
    list_display = ("First_name", "Last_name", "Department", "Salary", "Bonus", "Role", "Phone","Hiring_date")
admin.site.register(Employee, Employee2)