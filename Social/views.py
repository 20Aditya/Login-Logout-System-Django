from django.shortcuts import render, render_to_response, reverse
from django.contrib.auth import authenticate, login, logout
from django.views import generic
from .forms import UserForm, LoginForm
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm
from django.template.context_processors import csrf
from django.views.decorators.csrf import requires_csrf_token
from .models import UserProfile


app_name = 'Social'


def index(request):
    return render(request, 'Social\welcome_page.html', {'index': index})


def new_account(request):
    return render(request, 'Social/registration.html', {'new_account': new_account})


class UserFormView(generic.View):
    form_class = UserForm
    template_name = 'Social/base.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            user.set_password(password)
            user.save()

            return HttpResponseRedirect(reverse('Social:login'))

        return render(request, self.template_name, {'form': form})


class newloginView(generic.View):
    form_class = LoginForm
    template_name = 'Social/login.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('Social:loggedin'))
        else:
            return render(request, 'Social/invalid_login.html')



@login_required()
def loggedin(request):
    return render_to_response('Social/loggedin.html', {'name': request.user.username})


def invalid_login(request):
    return render_to_response('Social/invalid_login.html')


def user_logout(request):
    logout(request)
    return render_to_response('Social/loggingout.html', {'us': request.user.username})

@login_required()
@requires_csrf_token
class EditProfileView(generic.View):
    form_class = UserProfileForm
    template_name = 'Social/profile.html'
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            likes_cheese = form.cleaned_data['likes_cheese']
            favorite_ham_name = form.cleaned_data['favorite_ham_name']
            user.save()

            return HttpResponseRedirect(reverse('Social:loggedin'))

        return render(request, self.template_name, {'form': form})












