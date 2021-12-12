from django.db import models
from django.conf import settings
from django.utils import timezone
import datetime
from django.urls import reverse
  
# class Category(models.Model):
#     name = models.CharField(max_length=50)
  
#     @staticmethod
#     def get_all_categories():
#         return Category.objects.all()
  
#     def __str__(self):
#         return self.name
class Product(models.Model):

    title=models.CharField(max_length=50)
    description=models.TextField()
    photo_prod=models.ImageField(upload_to='media/images/',null=True)
    price=models.IntegerField()
#    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)

    def publish(self):
        self.save()

#     class Meta:
#         verbose_name = _("")
#         verbose_name_plural = _("s")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("product_page", kwargs={"id": self.id})

# class User(models.Model):
#    name=CITextField()
#    email=models.EmailField( max_length=254)
#    phone=models.PhoneNumberField()
#    admin='AD'
#    client='CL'
   

#     def publish(self):
#         self.save()

#     class Meta:
#         verbose_name = _("")
#         verbose_name_plural = _("s")

#     def __str__(self):
#         return self.name

#     def get_absolute_url(self):
#         return reverse("_detail", kwargs={"pk": self.pk})

from django.db import models
  
  
class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    password = models.CharField(max_length=100)
  
    # to save the data
    def register(self):
        self.save()
  
    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False
  
    def isExists(self):
        if Customer.objects.filter(email=self.email):
            return True
  
        return False
# # # Create your models here.
class Order(models.Model):
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,
                                 on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=50, default='', blank=True)
    phone = models.CharField(max_length=50, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)
  
    def placeOrder(self):
        self.save()
  
    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-date')

  
