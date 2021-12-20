#!/usr/bin/python3
from django import forms
from .models import  Product
class Search(forms.Form):
    search=forms.CharField(label="search",max_length=40)
    query=Product.objects.filter(title=search)


