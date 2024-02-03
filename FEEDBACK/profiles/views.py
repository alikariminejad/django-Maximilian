from django.shortcuts import render
from django.views import View

class CreateProfile(View):
    def get(self, request):
        return render(request, "profiles/create_profile.html")

    def post(self, request):
        pass