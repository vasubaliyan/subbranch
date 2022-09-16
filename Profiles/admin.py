from django.contrib import admin
from.models import SellerProfile,BuyersProfile

@admin.register(SellerProfile)
class SellerProfileAdmin(admin.ModelAdmin):
    list_display=["name","user_name","email","phone_no","address_line1","address_line2","address_line3","pin","city","state","pic"]
    list_editable=["user_name","email","phone_no","pic"]
    
@admin.register(BuyersProfile)
class BuyersProfileAdmin(admin.ModelAdmin):
    list_display=["name","user_name","email","phone_no","address_line1","address_line2","address_line3","pin","city","state","pic"]
    list_editable=["user_name","email","phone_no","pic"]   
