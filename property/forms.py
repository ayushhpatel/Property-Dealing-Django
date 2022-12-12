from xml.parsers.expat import model
from django import forms
from .models import Property,Land,Buyer
# creating a form


class PropertyForm(forms.ModelForm):
    class Meta:
        model=Property
        fields=[
            "house_no",
            "society",
            "locality",
            "title",
            "city",
            "bedrooms",
            "bathrooms",
            "area",
            "price",
            "img",
            "desc",
            "age",
            "contactno"
        ]

class LandForm(forms.ModelForm):
    class Meta:
        model=Land
        fields=[
            "type",
            "locality",
            "city",
            "area",
            "price",
            "contactno",
            "img"
        ]

class BuyerForm(forms.ModelForm):
    class Meta:
        model=Buyer
        fields=[
            "incomecertificate",
            "phoneno",
            "email",
            "photo",
            "card",
        ]