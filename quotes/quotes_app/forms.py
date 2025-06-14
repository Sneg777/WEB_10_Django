from django import forms

from .models import Quote


class QuoteForm(forms.ModelForm):
    quote = forms.CharField(
        max_length=255,
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
            }
        )
    )
    author = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        )
    )

    class Meta:
        model = Quote
        fields = ["quote", "author"]
