from django import forms
from .models import User
import re



class UserCreationForm(forms.ModelForm):
    error_messages = {
        'password_mismatch': "The two password fields didn't match.",
        'password_invalid': "The password content does not have a capital character or the length is less than 8.",
        'name_not_capitalized': "First name should start with a capital letter.",
        'surname_not_capitalized': "Last_name name should start with a capital letter."
    }
    password1 = forms.CharField(label=("Password"), widget=forms.PasswordInput)
    password2 = forms.CharField(label=("Password confirmation"), widget=forms.PasswordInput)
    photo = forms.ImageField(label=("Photo"), required=False)

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name")

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def clean_password1(self):
        password1 = self.cleaned_data.get("password1")
        if len(password1) < 8 or not (re.search("[A-Z]", password1) and re.search("\d", password1)):
            raise forms.ValidationError(
                self.error_messages['password_invalid'],
                code='password_invalid',
            )
        return password1

    def clean_first_name(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get("first_name")

        if first_name and not first_name[0].isupper():
            raise forms.ValidationError(
                self.error_messages['name_not_capitalized'],
                code='name_not_capitalized',
            )
        return first_name
    
    def clean_last_name(self):
        cleaned_data = super().clean()
        last_name = cleaned_data.get("last_name")

        if last_name and not last_name[0].isupper():
            raise forms.ValidationError(
                self.error_messages['surname_not_capitalized'],
                code='surname_not_capitalized',
            )
        return last_name
    
    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if self.cleaned_data.get("photo"): 
            user.photo = self.cleaned_data["photo"]
        if commit:
            user.save()
        return user