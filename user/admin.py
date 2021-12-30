from django.contrib import admin

# Register your models here.
from .models import *
class contactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'mobile')
admin.site.register(contact, contactAdmin)

class galleryAdmin(admin.ModelAdmin):
    list_display = ('pdes', 'gpic', 'gdate')
admin.site.register(gallery, galleryAdmin)

class eventAdmin(admin.ModelAdmin):
    list_display = ('city', 'etitle', 'epurpose', 'epic', 'edate', 'sthanks')
admin.site.register(events, eventAdmin)

class membershipAdmin(admin.ModelAdmin):
    list_display = ('name', 'dob', 'gender', 'email', 'mobile', 'cityname', 'profession', 'address', 'mdate', 'picture')
admin.site.register(membership, membershipAdmin)

class donateAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'mobile', 'cityname', 'occupation', 'address', 'amount', 'ddate')
admin.site.register(donate, donateAdmin)

class notificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'news', 'ndate')
admin.site.register(notification, notificationAdmin)

class cityAdmin(admin.ModelAdmin):
    list_display = ('cityname', 'cdate')
admin.site.register(city, cityAdmin)

class sliderAdmin(admin.ModelAdmin):
    list_display = ('stitle','sdes','spic')
admin.site.register(slider,sliderAdmin)

class videoAdmin(admin.ModelAdmin):
    list_display = ('vlink','vtitle','vdate')
admin.site.register(video,videoAdmin)
