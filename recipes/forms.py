from .models import Reviews
from django import forms


class ReviewDetail(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ('author', 'comment',)
