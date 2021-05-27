from django import forms
#from .models import Profile
from django.contrib.auth.models import User
from user.models import Profile, Address
from product.models import Order, Review
from allauth.account.forms import SignupForm


class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')
    username = forms.CharField(label='Adhar Number')
    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.username = self.cleaned_data['username']
        user.save()
        return user


class NameForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']
        widgets = {
            "first_name": forms.TextInput(attrs={'placeholder': 'First Name', 'class': 'form-control', 'required': 'required', 'autofocus':'""'}),
            "last_name": forms.TextInput(attrs={'placeholder': 'Last Name', 'class': 'form-control', 'required': 'required'}),
            }
            
class MobileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['mobile','gender']
        widgets = {
            "mobile": forms.TextInput(attrs={'placeholder': 'Mobile', 'class': 'form-control', 'required': 'required'}),
            "gender": forms.Select(attrs={'placeholder': 'Gender', 'class': 'form-control', 'required': 'required', 'autofocus':'""'}),
            }


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['address_line','landmark','city','district','state','pin']
        widgets = {
            "address_line": forms.TextInput(attrs={'placeholder': 'Address Line', 'class': 'form-control', 'required': 'required'}),
            "landmark": forms.TextInput(attrs={'placeholder': 'Landmark', 'class': 'form-control'}),
            "city": forms.TextInput(attrs={'placeholder': 'City', 'class': 'form-control', 'required': 'required'}),
            "district": forms.TextInput(attrs={'placeholder': 'District', 'class': 'form-control', 'required': 'required'}),
            "state": forms.Select(attrs={'placeholder': 'State', 'class': 'form-control', 'required': 'required'}),
            "pin": forms.TextInput(attrs={'placeholder': 'Pin Code', 'class': 'form-control', 'required': 'required'}),
            }


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['family']
        widgets = {
            "family": forms.Select(attrs={'placeholder': 'Select Family', 'class': 'form-control', 'required': 'required', 'autofocus':'""'}),
            "product": forms.Select(attrs={'placeholder': 'User', 'class': 'form-control', 'required': 'required', 'autofocus':'""'}),
            }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['order', 'title', 'body']
        widgets = {
            "order": forms.Select(attrs={'placeholder': 'Select Order', 'class': 'form-control', 'required': 'required', 'autofocus':'""'}),
            "title": forms.TextInput(attrs={'placeholder': 'Review Title', 'class': 'form-control', 'required': 'required'}),
            "body": forms.TextInput(attrs={'placeholder': 'Review Body', 'class': 'form-control', 'required': 'required'}),
            }