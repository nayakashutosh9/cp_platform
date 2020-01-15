from django import forms
from django.contrib.auth.models import User
from cp_app.models import UserProfileInfo,Problem

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('first_name','last_name','username','email','password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('profile_pic',)
class SearchForm(forms.Form):
    tag = forms.CharField(required=False,widget=forms.TextInput(attrs={'autocomplete': 'off'}) )
    def clean(self):
        cleaned_data = super(SearchForm, self).clean()
        # do your custom validations / transformations here
        # and some more
        return cleaned_data
