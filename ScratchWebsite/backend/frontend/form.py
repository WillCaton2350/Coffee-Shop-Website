from django import forms
from .models import review_Models

class ReviewForm(forms.ModelForm):
    class Meta:
        model = review_Models
        fields = "__all__"