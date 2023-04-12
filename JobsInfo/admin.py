from django.contrib import admin
from JobsInfo.models import hydjobs,punejobs,chennaijobs,bangljobs


# Register your models here.


class hydjobsAdmin(admin.ModelAdmin):
    list_display=[
        'date',
        'company',
        'title',
        'eligibility',
        'address',
        'email',
        'phonenumber'
    ]



class punejobsAdmin(admin.ModelAdmin):
    list_display=[
        'date',
        'company',
        'title',
        'eligibility',
        'address',
        'email',
        'phonenumber'
    ]


class chennaijobsAdmin(admin.ModelAdmin):
    list_display=[
        'date',
        'company',
        'title',
        'eligibility',
        'address',
        'email',
        'phonenumber'
    ]


class bangljobsAdmin(admin.ModelAdmin):
    list_display=[
        'date',
        'company',
        'title',
        'eligibility',
        'address',
        'email',
        'phonenumber'
    ]



admin.site.register(hydjobs,hydjobsAdmin)
admin.site.register(punejobs,punejobsAdmin)
admin.site.register(chennaijobs,chennaijobsAdmin)
admin.site.register(bangljobs,bangljobsAdmin)















