from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm, EntryForm
from .models import Entry, Category
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class IndexView(View):
    template_name = 'finances/index.html'

    def get(self, request):
        try:
            incomes = Entry.objects.filter(agent=request.user,category=Category.objects.get(entries_type='IN'))
        except ObjectDoesNotExist:
            incomes = None
        try:
            expenses = Entry.objects.filter(agent=request.user,category=Category.objects.get(entries_type='EX'))
        except ObjectDoesNotExist:
            expenses = None

        return render(request, 'finances/index.html', {
                    'incomes': incomes,
                    'expenses': expenses,
                })

    def post(self, request):
        form = self.form_class(request.POST)


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


class CreateEntry(CreateView):
    model = Entry
    fields = ['category', 'description', 'amount', 'entry_date']

    def form_valid(self, form):
        entry = form.save(commit=False)
        entry.agent = self.request.user
        entry.save()
        return super(CreateEntry, self).form_valid(form)


class UpdateEntry(UpdateView):
    model = Entry
    fields = ['category', 'description', 'amount', 'entry_date']

    def form_valid(self, form):
        entry = form.save(commit=False)
        entry.agent = self.request.user
        entry.save()
        return super(UpdateEntry, self).form_valid(form)


class DeleteEntry(DeleteView):
    model = Entry
    success_url = reverse_lazy('finances:index')

def login_user(request):
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return render(request, 'finances/index.html')        
            else: 
                return render(request, 'finances/login.html', {'error_message': 'Invalid username or password'})
    
        else:
            return render(request, 'finances/login.html')
        
    
def delete_entry(request, entry_id):
    entry = Entry.objects.get(pk=entry_id)
    entry.delete()
    return render(request, 'finances/index.html')


        
        
