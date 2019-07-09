from django.contrib import admin
from main.models import Branch, Customer, Device, Reading, Location
# Register your models here.

class BranchAdmin(admin.ModelAdmin):
    list_display = ('name', 'address' )
    

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'company_name', 'phone' )

class LocationAdmin(admin.ModelAdmin):
    list_display = ('customer', 'branch', 'phone' )

class DeviceAdmin(admin.ModelAdmin):
    list_display = ('customer', 'location', 'device_id' )

class ReadingAdmin(admin.ModelAdmin):
    list_display = ('customer', 'device', 'post_time', 'post_date' )

admin.site.register(Branch, BranchAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Device, DeviceAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Reading, ReadingAdmin)