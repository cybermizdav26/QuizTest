from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

User = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("phone",)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ("phone", "email")


class SignUpForm(forms.ModelForm):
    password1 = forms.CharField(max_length=128, widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=128, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("phone", "email", "first_name", "password1", "password2")

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password1

    def save(self, commit=True):
        password1 = self.cleaned_data["password1"]
        user = super().save(commit=False)
        user.set_password(password1)
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    phone = forms.CharField(max_length=13)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)


class UserUpdateProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'image')
