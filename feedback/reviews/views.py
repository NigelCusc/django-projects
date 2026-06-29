from django.shortcuts import redirect, render
from reviews.models import Review
from .forms import ReviewForm
from django.views import View

# Two kind of requests: GET and POST
# GET request is used to retrieve data from the server
# POST request is used to send data to the server
def review(request):
    form = ReviewForm()
    if (request.method == 'POST'):
        form = ReviewForm(request.POST)

        if form.is_valid():
            # review = Review(user_name=form.cleaned_data['user_name'], review_text=form.cleaned_data['review_text'], rating=form.cleaned_data['rating'])
            form.save() # Saves the form data to the database. Since we are using a ModelForm, the data is saved to the database.
            return redirect('/thank-you/')
    else:
        form = ReviewForm()
    return render(request, 'reviews/review.html', {
        'form': form
    })

# Using Class Based Views
class ReviewView(View):
    def get(self, request):
        form = ReviewForm()
        return render(request, 'reviews/review.html', {
            'form': form
        })
    def post(self, request):
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/thank-you/')
        return render(request, 'reviews/review.html', {
            'form': form
        })

def thank_you(request):
    return render(request, 'reviews/thank_you.html')