#to take data from user

from django import forms

from .models import RestaurantLocation

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
            print("error detected")
        return name

class RestaurantLocationCreateForm(forms.ModelForm):
    class Meta:
        model = RestaurantLocation
        fields = [
            "name",
            "location",
            "category"
        ]