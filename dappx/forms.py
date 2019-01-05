from django import forms
from dappx.models import UserProfileInfo
from django.contrib.auth.models import User
from django.forms import ModelForm 
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
class UserForm(forms.ModelForm):
	# password = forms.CharField(widget=forms.PasswordInput())
	class Meta():
 		model = User
 		fields = ('username','password','email')
class UserProfileInfoForm(forms.ModelForm):
	class Meta():
 		model = UserProfileInfo
 		fields = ('portfolio_site','pack')