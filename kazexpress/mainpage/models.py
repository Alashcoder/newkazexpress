from django.db import models
class product (models.Model):

    title=models.CharField(max_length=50)
    description=models.TextField(blank=true)
    photo_prod=models.ImageField(_, upload_to=None, height_field=None, width_field=None, max_length=None)
    price=models.IntegerField()




    class Meta:
        verbose_name = _("")
        verbose_name_plural = _("s")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
)
class User(models.Model):
   name=CITextField()
   email=models.EmailField( max_length=254)
   phone=models.PhoneNumberField()
   admin='AD'
   client='CL'
   

    

    class Meta:
        verbose_name = _("")
        verbose_name_plural = _("s")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})


# Create your models here.
