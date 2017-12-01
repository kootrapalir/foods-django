from django.core.exceptions import ValidationError

def validate_even(value):
    if value % 2 != 0:
        raise ValidationError(
            ('%(value)s is not an even number'),
            params={'value': value},
        )


#sample of good way of making validation
def clean_email(value):
    email = value
    if ".edu" in email:
        raise ValidationError(".edu emial ownt work")

CATEGORIES = ['Mandir', 'Aashram', 'Both']
def validate_category(value):
    cat = value.capitalize()
    if not value in CATEGORIES and not cat in CATEGORIES:
        raise ValidationError("not in category")