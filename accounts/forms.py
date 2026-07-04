from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import SECURITY_QUESTIONS


class RegisterForm(UserCreationForm):

    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            "placeholder": "Enter email",
        })
    )

    security_question = forms.ChoiceField(
        choices=SECURITY_QUESTIONS,
        required=True,
        label="Security Question",
    )

    security_answer = forms.CharField(
        required=True,
        label="Your Answer",
        widget=forms.TextInput(attrs={
            "placeholder": "Answer used to recover your password later",
        })
    )

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password1",
            "password2",
            "security_question",
            "security_answer",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["username"].widget.attrs.update({
            "placeholder": "Choose a username",
        })
        self.fields["password1"].widget.attrs.update({
            "placeholder": "Create a password",
        })
        self.fields["password2"].widget.attrs.update({
            "placeholder": "Confirm password",
        })

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]

        if commit:
            user.save()

        return user
