from django import forms
from MyApp.models import AddProduct

class Product(forms.ModelForm):
	class Meta:
		model = AddProduct
		fields = '__all__'

