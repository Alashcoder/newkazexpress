from django.db import models
from django.conf import settings
from django.utils import timezone
class Product(models.Model):

    title=models.CharField(max_length=50)
    description=models.TextField()
    photo_prod=models.ImageField(upload_to='media/images/',null=True)
    price=models.IntegerField()

    def publish(self):
        self.save()


    # class Meta:
    #     verbose_name = _("")
    #     verbose_name_plural = _("s")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})

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


# # # Create your models here.
