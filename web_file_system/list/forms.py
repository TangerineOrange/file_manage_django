from django import forms
 
class AddForm(forms.Form):
    name = forms.CharField(label='name', max_length=100)
    path = forms.CharField(label='path', max_length=100)