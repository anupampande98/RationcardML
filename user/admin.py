from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Profile, Address, Distributor, Family, Location, Relation

admin.site.site_header = "e-Rration System"
admin.site.site_title = "e-Rration System"

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'


class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    list_select_related = ('profile', )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

class AddressAdmin(admin.ModelAdmin):
    model = Address
    list_display = ('address_line', 'user', 'landmark', 'city', 'pin', 'state', 'is_active')
    search_fields = ['city', 'user']
    list_filter =['pin','city','user']
    list_editable = ['is_active']

admin.site.register(Address, AddressAdmin)

class DistributorAdmin(admin.ModelAdmin):
    model = Distributor
    list_display = ('user', 'location', 'is_active', 'created')
    search_fields = ['location', 'user']
    list_editable = ['is_active']

admin.site.register(Distributor, DistributorAdmin)


class FamilyAdmin(admin.ModelAdmin):
    model = Family
    list_display = ('title', 'added_by', 'type', 'is_active', 'created')
    search_fields = ['title', 'added_by']
    list_editable = ['is_active', 'type']

admin.site.register(Family, FamilyAdmin)

class LocationAdmin(admin.ModelAdmin):
    model = Location
    list_display = ('location', 'is_active', 'pincode')
    search_fields = ['location', 'pincode']
    list_editable = ['is_active']


admin.site.register(Location, LocationAdmin)
admin.site.register(Relation)