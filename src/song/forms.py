from django import forms
from .models import Song,Try


GENDER_CHOICES = [('Male','Male'), ('Female','Female'), ('Others','Others')]


class SongForm(forms.ModelForm):
	sid 	= forms.IntegerField(label="",widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'sid'}))
	sname 	= forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'sname'}))
	singer 	= forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'singer'}))
	file    = forms.FileField(label="",widget=forms.FileInput(attrs={'class':'form-control'}))
	cost 	= forms.IntegerField(label="",widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'cost'}))
	desc 	= forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'desc'}))


	def clean_singer(self,*args,**kwargs):
		singer = self.cleaned_data.get("singer")
		if len(singer)>20 :
			raise forms.ValidationError("Singer length is more")
		else:	
			return singer

	def clean_sid(self):
		sid = str(self.cleaned_data.get("sid"))
		if len(sid)>5:
			raise forms.ValidationError("sID IS GREATER THAN 5")
		return sid	

	def clean_cost(self):
		cost = self.cleaned_data.get("cost")
		if cost>500:
			raise forms.ValidationError("The cost is greater than 500")
		return cost
		
	class Meta:
		model = Song
		fields = ['sid','sname','singer','cost','desc','file']			

				
class TryForm(forms.ModelForm):
	gender = forms.CharField(label='Gender', widget=forms.RadioSelect(choices=GENDER_CHOICES, attrs={'class':'custom-control-inline'}))
	date   = forms.DateField(label="Date",widget=forms.TextInput(attrs={'placeholder':'Pick Date','class':'form-control','id':'datepicker','autocomplete':'off'}))
	image  = forms.ImageField(label="Image",widget=forms.FileInput(attrs={'class':'form-control'}))
	class Meta:
		model = Try
		fields = "__all__"