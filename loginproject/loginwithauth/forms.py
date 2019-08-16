from django import forms

class LoginForm(forms.Form):
    username = forms.CharField()
    email = forms.CharField()
    pws = forms.CharField(widget=forms.PasswordInput)
    psw_confirm = forms.CharField(widget=forms.PasswordInput)


