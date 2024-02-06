from django.contrib import admin

# Register your models here.
from service.models import service_custom
class service_cust(admin.ModelAdmin):
    list_display=('service_1','service_2',"service_des")
admin.site.register(service_custom,service_cust)