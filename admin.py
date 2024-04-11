from django.contrib import admin
from .models import User
from .models import Artist
from .models import Art
from .models import Customer
from .models import Artist_Login
from .models import Customer_Login
from .models import Categories
from .models import Orders
from.models import Transaction
from.models import Wishlist
from.models import Cart


# Register your models here.

@admin.register(User)
class Useradmin(admin.ModelAdmin):
    list_display=['id','user_name','user_email','user_type']
admin.site.register(Artist)
admin.site.register(Art)
admin.site.register(Customer)
admin.site.register(Artist_Login)
admin.site.register(Customer_Login)
admin.site.register(Categories)
admin.site.register(Orders)
admin.site.register(Transaction)
admin.site.register(Wishlist)
admin.site.register(Cart)


