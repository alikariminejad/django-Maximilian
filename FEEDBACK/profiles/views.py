from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from .forms import ProfileForm

def store_file(file):
    with open("temp/image.png", "wb+") as dest:
        for chunk in file.chunks():
            dest.write(chunk)


class CreateProfile(View):
    def get(self, request):
        form = ProfileForm()
        return render(request, "profiles/create_profile.html", {
            "form": form
        })

    def post(self, request):
        submiited_form = ProfileForm(request.POST, request.FILES)
        if submiited_form.is_valid():
            store_file(request.FILES["image"])
            return HttpResponseRedirect("/profiles")
        return render(request, "profiles/create_profile.html", {
            "form": submiited_form
        })