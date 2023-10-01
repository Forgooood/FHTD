from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

admin.site.register(CustomUser)
admin.site.register(Category)
admin.site.register(OfferSale)
admin.site.register(OfferBuy)
admin.site.register(Manufacturer)
admin.site.register(OfferModel)
admin.site.register(Unit)
admin.site.register(News)