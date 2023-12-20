from typing import Any
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from .forms import ReviewForm
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from .models import Review


class ReviewView(View):
    def get(self, request):
        form = ReviewForm()
        return render(request, 'reviews/review.html', {
            "form": form
    })

    def post(self, request):
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/thank-you")

class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"
    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['message'] = 'This works!'
        return context

class ReviewsListView(TemplateView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "reviews"

    def get_queryset(self):
        base_query = super().get_queryset()
        data = base_query.filter(rating__gt=4)
        return data
    
    
class SingleReviewView(ListView):
    template_name = "reviews/single_review.html"

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        review_id = kwargs["id"]
        selected_review = Review.objects.get(pk=review_id)
        context['review'] = selected_review
        return context