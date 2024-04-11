
from .models import User
from .models import Artist
from .models import Artist_Login
from .models import Art
from .models import Customer
from .models import Customer_Login
from .models import Categories
from .models import Orders
from.models import Transaction
from.models import Wishlist
from.models import Cart

from .serializers import userSerializer
from .serializers import ArtistSerializer
from .serializers import Artist_LoginSer
from .serializers import Art_serializer
from .serializers import CustomerSer
from .serializers import Customer_loginSer
from .serializers import CategorySerializer
from .serializers import OrderSerializer
from .serializers import TranSerializer
from .serializers import WishSerializer
from .serializers import CartSerializer

from rest_framework.generics import ListAPIView,RetrieveDestroyAPIView,ListCreateAPIView,RetrieveUpdateAPIView

# Create your views here.

#USER CRUD
class Userlist_create(ListCreateAPIView):
    queryset=User.objects.all()
    serializer_class=userSerializer

class UserRetrive_Update(RetrieveUpdateAPIView):
    queryset=User.objects.all()
    serializer_class=userSerializer

class User_Retrive_Delete(RetrieveDestroyAPIView):
    queryset=User.objects.all()
    serializer_class=userSerializer

#ARTIST CRUD
class Artist_create(ListCreateAPIView):
    queryset=Artist.objects.all()
    serializer_class=ArtistSerializer

class Artist_Retrive_Update(ListCreateAPIView):
    queryset=Artist.objects.all()
    serializer_class=ArtistSerializer

class Artist_Retrive_Delete(RetrieveDestroyAPIView):
    queryset=Artist.objects.all()
    serializer_class=ArtistSerializer

#ARTIST_LOGIN API
class ArtistLogin_list(ListAPIView):
    queryset=Artist_Login.objects.all()
    serializer_class=Artist_LoginSer

#ART CRUD 
class ArtListCreate(ListCreateAPIView):
    queryset=Art.objects.all()
    serializer_class=Art_serializer

class ArtRetriveUpdate(RetrieveUpdateAPIView):
    queryset=Art.objects.all()
    serializer_class=Art_serializer

class ArtRetriveDelete(RetrieveDestroyAPIView):
    queryset=Art.objects.all()
    serializer_class=Art_serializer

#CUSTOMER CRUD API
class CustomerListCreate(ListCreateAPIView):
    queryset=Customer.objects.all()
    serializer_class=CustomerSer

class CustomerListUpdate(RetrieveUpdateAPIView):
    queryset=Customer.objects.all()
    serializer_class=CustomerSer

class CustomerListDelete(RetrieveDestroyAPIView):
    queryset=Customer.objects.all()
    serializer_class=CustomerSer

#CUSTOMER_LOGIN_API
class CustomerLoginList(ListAPIView):
    queryset=Customer_Login.objects.all()
    serializer_class=Customer_loginSer

#CATEGORIES_API
class CategoryListCreate(ListCreateAPIView):
    queryset=Categories.objects.all()
    serializer_class=CategorySerializer

class CategoryListUpdate(RetrieveUpdateAPIView):
    queryset=Categories.objects.all()
    serializer_class=CategorySerializer

class CategoryListDelete(RetrieveDestroyAPIView):
    queryset=Categories.objects.all()
    serializer_class=CategorySerializer

#ORDER_API
class OrderListCreate(ListCreateAPIView):
    queryset=Orders.objects.all()
    serializer_class=OrderSerializer

class OrderListUpdate(RetrieveUpdateAPIView):
    queryset=Orders.objects.all()
    serializer_class=OrderSerializer

class OrderListDelete(RetrieveDestroyAPIView):
    queryset=Orders.objects.all()
    serializer_class=OrderSerializer

#TRANSACTION API
class TransactionList(ListCreateAPIView):
    queryset=Transaction.objects.all()
    serializer_class=TranSerializer

#WISHLIST API
class WishListData(ListCreateAPIView):
    queryset=Wishlist.objects.all()
    serializer_class=WishSerializer

#CART API
class CartData(ListCreateAPIView):
    queryset=Cart.objects.all()
    serializer_class=CartSerializer
