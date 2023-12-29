from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.forms import TextInput

from kitchen.models import Dish, Cook


class DishForm(forms.ModelForm):
    cookers = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Dish
        fields = "__all__"


class CookCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Cook
        fields = UserCreationForm.Meta.fields + (
            "years_of_experience",
            "first_name",
            "last_name",
        )
        widgets = {
            "years_of_experience": TextInput(attrs={"placeholder": "Years of experience"},),
            "first_name": TextInput(attrs={"placeholder": "First name"},),
            "last_name": TextInput(attrs={"placeholder": "Last name"}, ),
            "username": TextInput(attrs={"placeholder": "Username"}, ),

        }

    def clean_license_number(self):  # this logic is optional, but possible
        return validate_years_of_experience(self.cleaned_data["years_of_experience"])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, field in self.fields.items():
            if key == "password1" or key == "password2":
                continue
            field.label = ""

class CookExperienceUpdateForm(forms.ModelForm):
    class Meta:
        model = Cook
        fields = ["years_of_experience"]

    def clean_license_number(self):
        return validate_years_of_experience(self.cleaned_data["years_of_experience"])


def validate_years_of_experience(
    years_of_experience,
):  # regex validation is also possible here
    if years_of_experience > 100:
        raise ValidationError("Years of experience should be real")
    if years_of_experience.isdigit():
        raise ValidationError("Years of experience should be integer")

    return years_of_experience


class DishTypeSearchForm(forms.Form):
    name = forms.CharField(max_length=50,
                           label="",
                           widget=forms.TextInput(
                               attrs={"placeholder": "sort by name"}))


class DishSearchForm(forms.Form):
    model = forms.CharField(max_length=50,
                            label="",
                            widget=forms.TextInput(
                                attrs={"placeholder": "sort by name"}))


class CookSearchForm(forms.Form):
    username = forms.CharField(max_length=50,
                               label="",
                               widget=forms.TextInput(
                                   attrs={"placeholder": "sort by username"}))
