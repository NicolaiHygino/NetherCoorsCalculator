from django import forms 


class CoordForm(forms.Form):
	x = forms.CharField()
	y = forms.CharField()
