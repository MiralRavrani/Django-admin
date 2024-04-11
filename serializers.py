from rest_framework import serializers
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


class userSerializer(serializers.ModelSerializer):
    class Meta:
     model= User
     fields=['id','user_name','user_email','user_password','user_type']

class ArtistSerializer(serializers.ModelSerializer):
   class Meta:
      model=Artist
      fields='__all__'

class Artist_LoginSer(serializers.ModelSerializer):
   class Meta:
      model=Artist_Login
      fields='__all__'

class Art_serializer(serializers.ModelSerializer):
   class Meta:
      model=Art
      fields='__all__'

class CustomerSer(serializers.ModelSerializer):
   class Meta:
      model=Customer
      fields='__all__'
    
class Customer_loginSer(serializers.ModelSerializer):
   class Meta:
      model=Customer_Login
      fields='__all__'

class CategorySerializer(serializers.ModelSerializer):
   class Meta:
      model=Categories
      fields='__all__'

class OrderSerializer(serializers.ModelSerializer):
   class Meta:
      model=Orders
      fields='__all__'

class TranSerializer(serializers.ModelSerializer):
   class Meta:
      model=Transaction
      fields='__all__'

class WishSerializer(serializers.ModelSerializer):
   class Meta:
      model=Wishlist
      fields='__all__'

class CartSerializer(serializers.ModelSerializer):
   class Meta:
      model=Cart
      fields='__all__'
