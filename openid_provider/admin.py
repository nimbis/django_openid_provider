# -*- coding: utf-8 -*-
# vim: set ts=4 sw=4 : */

from django.contrib import admin

from openid_provider.models import TrustedRoot, OpenID

class TrustedRootInline(admin.TabularInline):
    model = TrustedRoot

class OpenIDAdmin(admin.ModelAdmin):
    list_display = ['openid', 'user', 'default']
    inlines = [TrustedRootInline, ]
    raw_id_fields = ("user",)
    search_fields = ('user__email',)
    
admin.site.register(OpenID, OpenIDAdmin)
