from django import forms


class Cricketrun(forms.Form):
 	hit = forms.IntegerField(min_value=1, max_value=6,  widget=forms.NumberInput(attrs={'class' : 'form-control' , 'placeholder' : 'Enter'}))


class Usernameform(forms.Form):
 	username = forms.CharField(min_length=4, max_length=15,  widget=forms.TextInput(attrs={'class' : 'form-control' , 'placeholder' : 'Enter Username'}))
 	