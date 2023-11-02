from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView


# Create your views here.
def hello_world(request):
    if request.method == "POST":
        # POST일때 어떤 값을 처리할지 적어줌
        temp = request.POST.get('email')
        return render(request, "accountapp/hello_world.html",
                      context={"temp": temp})

    temp = "techit"

    return render(request, "accountapp/hello_world.html",
                  context={"temp": temp})

class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy("accountapp:hello_world")
    template_name = "accountapp/create.html"