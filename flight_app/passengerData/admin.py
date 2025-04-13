from django.contrib import admin
from passengerData.models import passenger
# Register your models here.
class PassengerRecord(admin.ModelAdmin):
    list_display = ['firstName','lastName']

admin.site.register(passenger,PassengerRecord)    