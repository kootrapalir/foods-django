from django import forms

from restaurants.models import RestaurantLocation

from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
            'restaurant',
            'name',
            'contents',
            'excludes',
            'public'
        ]
    def __init__(self, user=None, *args, **kwargs):
        # print(kwargs.pop('instance'))
        super(ItemForm, self).__init__(*args, **kwargs)
        #to get items from only 1 user who added restaurants
        self.fields['restaurant'].queryset = RestaurantLocation.objects.filter(owner=user)
