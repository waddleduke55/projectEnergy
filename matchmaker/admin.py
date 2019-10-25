from django.contrib import admin
from matchmaker.models import Member, Seller, Country, Listing

# Register your models here.
admin.site.register(Member)
admin.site.register(Seller)
admin.site.register(Country)
admin.site.register(Listing)
