from django import forms
from .models import Accounts
from django.contrib.auth.models import User


class AccountForm(forms.ModelForm):
	# full_name = forms.CharField(label="Full Name",widget=forms.TextInput(attrs={'placeholder':'name'}))
	username  = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control ','placeholder':'username'}))
	email  = forms.EmailField(label="",widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'email'}))
	password  = forms.CharField(label="",widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'password'}))
	conf_password = forms.CharField(label="",widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'confirm password'}))
	
	def clean(self):
		cleaned_data = super(AccountForm, self).clean()
		username = cleaned_data.get('username')
		email = cleaned_data.get('email')
		conf_password = cleaned_data.get('conf_password')
		password = cleaned_data.get('password')

		if len(password)<7:
			raise forms.ValidationError("Password must be 8 character")	

		if password and conf_password:
			if password != conf_password:
				raise forms.ValidationError("The two password fields must match.")	
		return cleaned_data
	class Meta:
		model = Accounts
		fields = "__all__"	

		
class LoginForm(forms.Form):
	username = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'username'}))
	password = forms.CharField(label="",widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'password'}))

	def clean(self):
		pas = self.cleaned_data.get('password')
		if len(str(pas))>10:
			raise ValidationError("Length is more")	
		return pas				
