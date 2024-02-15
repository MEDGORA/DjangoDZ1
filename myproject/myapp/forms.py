from django import forms

class ProductForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Наименование'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'placeholder': 'Описание'}))
    price = forms.DecimalField(max_digits=8, decimal_places=2, widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder': 'Цена'}))
    digits = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder': 'Количество'}))
    image = forms.ImageField()