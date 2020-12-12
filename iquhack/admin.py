# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Hackathon, Sponsor, Tier, CompanyContact

class SponsorInline(admin.TabularInline):
    model = Sponsor
    extra = 1

class HackathonAdmin(admin.ModelAdmin):
    list_display = ("__unicode__", "end_date", "published", "registration_open")
    inlines = (SponsorInline, )

class SponsorAdmin(admin.ModelAdmin):
    list_display = ("__unicode__", "hackathon", "company_contact")

admin.site.register(Hackathon, HackathonAdmin)
admin.site.register(Sponsor, SponsorAdmin)
admin.site.register(Tier)
admin.site.register(CompanyContact)