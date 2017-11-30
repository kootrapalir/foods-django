#to take data from user

from django import forms

from .models import RestaurantLocation

from .validators import validate_category

class RestaurantCreateForm(forms.Form):
    name =          forms.CharField()
    location =      forms.CharField(required=False)
    category =      forms.CharField(required=False)

    #USING FORM VALIDATAION
    #this is called when forms.is_valid() is called in views
    def clean_name(self):
        name = self.cleaned_data.get("name")
        if name == "Hello":
            raise forms.ValidationError("not valid name")
        return name

class RestaurantLocationCreateForm(forms.ModelForm):
    # email = forms.EmailField()

    #done from models itself
    # category = forms.CharField(required=False, validators=[validate_category])

    class Meta:
        model = RestaurantLocation
        fields = [
            "name",
            "location",
            "category"
        ]

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if name == "Hello":
            raise forms.ValidationError("not valid name")
        return name

    #sample of simple way of making validation
    # def clean_email(self):
    #     email = self.cleaned_data.get("email")
    #     if ".edu" in email:
    #         raise forms.ValidationError(".edu emial ownt work")
    #     return email
