from django import forms
from .models import Publication, Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PublicationForms(forms.ModelForm):
	"""docstring for PublicationForms"""
	class Meta:
		"""docstring for Meta"""
		model = Publication
		fields = ('image', 'titre', 'texte')

class LoginForm(forms.Form):
	"""docstring for LoginForm"""
	username = forms.CharField(label="Nom d'utilisateur",
								widget=forms.TextInput(attrs={ "class":"form-control" }))
	password = forms.CharField(label="Mot de passe",
								widget=forms.PasswordInput(attrs={ "class":"form-control" }))

class SignUpForm(UserCreationForm):
	"""docstring for SignUpForm"""
	username = forms.CharField(label="Nom d'utilisateur",
								widget=forms.TextInput(attrs={ "class":"form-control" }))
	last_name = forms.CharField(label="Nom",
								widget=forms.TextInput(attrs={ "class":"form-control" }))
	first_name = forms.CharField(label="Prenom",
								widget=forms.TextInput(attrs={ "class":"form-control" }))
	email = forms.EmailField(label="Email",
								widget=forms.EmailInput(attrs={ "class":"form-control" }))
	password1 = forms.CharField(label="Mot de passe",
								widget=forms.PasswordInput(attrs={ "class":"form-control" }))
	password2 = forms.CharField(label="Confirmation mot de passe",
								widget=forms.PasswordInput(attrs={ "class":"form-control" }))
	class Meta:
		"""docstring for Meta"""
		model = User
		fields = ('username','last_name','first_name', 'email', 'password1', 'password2')
		
class UserUpdateForm(forms.ModelForm):
	username = forms.CharField(label="Nom d'utilisateur",
								widget=forms.TextInput(attrs={ "class":"form-control" }))
	last_name = forms.CharField(label="Nom",
								widget=forms.TextInput(attrs={ "class":"form-control" }))
	first_name = forms.CharField(label="Prenom",
								widget=forms.TextInput(attrs={ "class":"form-control" }))
	email = forms.EmailField(label="Email",
							widget=forms.EmailInput(attrs={ "class":"form-control" }))
	
	class Meta:
		"""docstring for Meta"""
		model = User
		fields = ('username','last_name','first_name', 'email')

class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields  = ['image']
		
		
			

