from django import forms
 
class AddForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
    b = forms.IntegerField()