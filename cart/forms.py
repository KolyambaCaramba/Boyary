from django import forms


PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]



class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

class CartAddProductForm(forms.Form):
        quantity = forms.IntegerField(min_value=1, max_value=10)
        update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

        def clean_quantity(self):
            quantity = self.cleaned_data['quantity']
            if quantity > 10:
                raise forms.ValidationError("The quantity should be less than or equal to 10.")
            return quantity
    