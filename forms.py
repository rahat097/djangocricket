from django import forms


class Cricketrun(forms.Form):
 	hit = forms.IntegerField(min_value=1, max_value=6,  widget=forms.NumberInput(attrs={'class' : 'form-control' , 'placeholder' : 'Enter'}))
 	