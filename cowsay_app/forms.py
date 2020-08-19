from django import forms


class AddTextForm(forms.Form):
    text = forms.CharField(widget=forms.TextInput)
