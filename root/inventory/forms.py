from django import forms

from .models import Item
from .models import Category
from .models import Brand


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ["name", "item_id",
                "category", "image",
                "model_number", "serial_number", "brand_name", "remarks"]
        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter Item Name"
            }),
            "item_id": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter Item Id"
            }),
            "category": forms.Select(attrs={
                "class": "regDropDown",
            }),
            "image": forms.ClearableFileInput(attrs={
                "class": "form-control",
            }),
            "model_number": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter Item Model Number"
            }),
            "serial_number": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter Item Serial Number"
            }),
            "brand_name": forms.Select(attrs={
                "class": "regDropDown"
            }),
            "remarks": forms.Textarea(attrs={
                "class": "form-control",
                "placeholder": "Enter Item Description "
            })
        }
                

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name", "description", "category_id"]
        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Category Name"
            }),
            "description": forms.Textarea(attrs={
                "class": "form-control",
                "placeholder": "Enter description"
            }),
            "category_id": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Category Id"
            })
        }


class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ["name", "description"]
        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Brand Name"
            }),
            "description": forms.Textarea(attrs={
                "class": "form-control",
                "placeholder": "Description"
            })
        }


class AdminLogin(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Enter your username"
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-control",
        "placeholder": "Enter your password"
    }))