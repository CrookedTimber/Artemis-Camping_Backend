from django.contrib import admin
from .models import Message, Trip, Place, Member, Checklist, Budget

# Register your models here.

admin.site.register(Trip)
admin.site.register(Place)
admin.site.register(Member)
admin.site.register(Message)
admin.site.register(Checklist)
admin.site.register(Budget)



