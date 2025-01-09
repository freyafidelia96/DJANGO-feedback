from reviews.models import Review
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView, FormView, CreateView

from .forms import ReviewForm
from .models import Review
# Create your views here.


class ReviewView(CreateView):
    template_name = "reviews/review.html"
    form_class = ReviewForm
    success_url = "/thank-you"
    
    

class ThankYouView(TemplateView):
    template_name = "reviews/thanks.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["message"] = "This works!"
        return context
    
    
class ReviewListView(ListView):
    template_name = "reviews/reviews_list.html"
    model = Review
    context_object_name = "reviews"
    
    

class ReviewDetailView(DetailView):
    template_name = "reviews/single_review.html"
    model = Review
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_review = self.object
        request = self.request
        favorite_id = request.session.get("favorite_review")
        context["is_favorite"] = favorite_id == str(loaded_review.id)
        return context

    
    
class AddFavoriteView(View):
    def post(self, request):
        review_id = request.POST['review_id']
        request.session["favorite_review"] = review_id
        return HttpResponseRedirect("/review-detail/" + review_id)