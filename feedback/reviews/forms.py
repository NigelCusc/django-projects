from django import forms
from .models import Review

# class ReviewForm(forms.Form):
#     username = forms.CharField(label='Your name', min_length=2, max_length=100, error_messages={
#         'required': 'Your name must be at least 2 characters long.',
#         'min_length': 'Your name must be at least 2 characters long.',
#         'max_length': 'Your name must be less than 100 characters long.'
#     })
#     review = forms.CharField(label='Your review', widget=forms.Textarea, min_length=10, max_length=200, error_messages={
#         'required': 'Your review must be at least 10 characters long.',
#         'min_length': 'Your review must be at least 10 characters long.',
#         'max_length': 'Your review must be less than 200 characters long.'
#     })
#     rating = forms.IntegerField(label="Your Rating", min_value=1, max_value=5)


#  Generate form from model
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
        # exclude = ['owner_comment']
        labels = {
            'user_name': 'Your Name',
            'review_text': 'Your Review',
            'rating': 'Your Rating'
        }
        error_messages = {
            'user_name': {
                'required': 'Your name must be at least 2 characters long.',
                'min_length': 'Your name must be at least 2 characters long.',
                'max_length': 'Your name must be less than 100 characters long.'
            },
            'review_text': {
                'required': 'Your review must be at least 10 characters long.',
                'min_length': 'Your review must be at least 10 characters long.',
                'max_length': 'Your review must be less than 200 characters long.'
            },
            'rating': {
                'required': 'You must select a rating.',
                'min_value': 'Your rating must be at least 1.',
                'max_value': 'Your rating must be less than 6.'
            }
        }
        widgets = {
            'review_text': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }