from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import generic
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm, EntryForm


class IndexView(generic.ListView):
    template_name = 'finances/index.html'

    def get_queryset(self):
        return []


class UserFormView(View):
    form_class = UserForm
    template_name = 'finances/registration_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return render(request, 'finances/index.html')

        return render(request, self.template_name, {"form": form})


class EntryFormView(View):
    form_class = EntryForm
    template_name = 'finances/create_entry.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            entry = form.save(commit=False)
            entry.agent = request.user
            entry.save()
            return render(request, 'finances/index.html')

        return render(request, self.template_name, {"form": form})

    def get_queryset(self):
        return []