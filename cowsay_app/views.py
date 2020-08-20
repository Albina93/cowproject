from django.shortcuts import render, HttpResponseRedirect, reverse
from .models import Text_Result
from .forms import AddTextForm
import subprocess

# Create your views here.


def index(request):
    cowsaid = ""
    if request.method == "POST":
        form = AddTextForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            text = data.get("text")
            Text_Result.objects.create(text=text)
            cowsaid = subprocess.check_output(
                ["cowsay", text], text=True)

    form = AddTextForm()
    return render(request, "index.html", {"form": form, "cowsaid": cowsaid})


def recent(request):
    cow_text = Text_Result.objects.all().order_by('-id')[:10]
    return render(request, "recent.html", {"cow_text": cow_text})
