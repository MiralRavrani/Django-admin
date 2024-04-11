from django.db import models

# Create your models here.
class User(models.Model):
    user_name=models.CharField(max_length=20)
    user_email=models.EmailField(max_length=40)
    user_password = models.CharField(max_length=20)
    user_type=models.CharField(max_length=10)

   
class Artist(models.Model):
    artist_email = models.EmailField(max_length=100,blank=False)
    artist_phone = models.CharField(max_length=10)
    artist_pass = models.CharField(max_length=20)

class Artist_Login(models.Model):
    Artists_id=models.ForeignKey(Artist,on_delete=models.CASCADE)
    artist_username = models.CharField(max_length=20)
    artist_password = models.CharField(max_length=20)

class Art(models.Model):
    art_id = models.ForeignKey(Artist, on_delete=models.CASCADE)
    art_title = models.CharField(max_length=30)
    art_price = models.DecimalField(max_digits=10, decimal_places=2)
    art_category = models.CharField(max_length=50)
    art_quantity = models.IntegerField()
    art_description = models.TextField()
    art_image = models.ImageField(upload_to='art_images')

class Customer(models.Model):
    customer_name = models.CharField(max_length=20)
    customer_email = models.EmailField(max_length=100)

class Customer_Login(models.Model):
    Customer_id=models.ForeignKey(Customer,on_delete=models.CASCADE)
    c_username = models.CharField(max_length=50)
    c_password = models.CharField(max_length=50)

class Categories(models.Model):
    cat_name = models.CharField(max_length=50)
    cat_image = models.ImageField(upload_to='category_images')

class Orders(models.Model):
    order_name = models.CharField(max_length=50)
    order_price = models.DecimalField(max_digits=10, decimal_places=2)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    art = models.ForeignKey(Art, on_delete=models.CASCADE)

class Transaction(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    art = models.ForeignKey(Art, on_delete=models.CASCADE)
    t_status = models.CharField(max_length=100)
    payment_info = models.CharField(max_length=255)
    payment_tra_id = models.CharField(max_length=100)
    paymentApiStatus = models.CharField(max_length=100)

class Wishlist(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    art = models.ForeignKey(Art, on_delete=models.CASCADE)

class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    art = models.ForeignKey(Art, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)