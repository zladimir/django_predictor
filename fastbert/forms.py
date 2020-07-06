from django import forms

class NameForm(forms.Form):
	your_review = forms.CharField(label='Your review',  widget=forms.Textarea)