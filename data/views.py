from django.shortcuts import render,redirect,HttpResponse
from .forms import SaveDataForm
# Create your views here.
def saving(request):
    if request.method == "POST":
        form = SaveDataForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()  # This here will save the necessary data to the database
            return HttpResponse("save")
        else:
            print(form.errors)  # To show you what field(s) are causing the form not to submit
