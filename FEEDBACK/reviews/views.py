from typing import Any
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from .forms import ReviewForm
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from .models import Review


class ReviewView(FormView):
    form_class = ReviewForm
    template_name = "reviews/review.html"
    success_url = "/thank-you"
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

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
    
    
class SingleReviewView(DetailView):
    template_name = "reviews/single_review.html"
    model = Review