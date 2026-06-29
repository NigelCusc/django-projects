from django.shortcuts import redirect, render
from reviews.models import Review
from .forms import ReviewForm
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView, CreateView

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

# Using Specific Class Based Views
class ReviewFormView(FormView):
    form_class = ReviewForm
    template_name = 'reviews/review.html'
    success_url = '/thank-you/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class ReviewCreateView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'reviews/review.html'
    success_url = '/thank-you/'

class ThankYouView(TemplateView):
    template_name = 'reviews/thank_you.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'This works!'
        return context

class ReviewListView(ListView):
    template_name = 'reviews/review_list.html'
    model = Review
    context_object_name = 'reviews' # This is the name of the context variable in the template.

    # This is the query set for the list view.
    def get_queryset(self):
        base_query = super().get_queryset()
        return base_query.order_by('-id')

class SingleReviewView(DetailView):
    template_name = 'reviews/single_review.html'
    model = Review