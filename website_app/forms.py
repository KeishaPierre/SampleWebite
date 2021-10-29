from website_app.models import Products
from django import forms
# from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    # this widget/plugin '.PasswordInput' hides the chars with '****'
    password = forms.CharField(widget=forms.PasswordInput)

class AddProducts(forms.ModelForm):
    class Meta:
        model= Products
        fields= ('title','Description')
