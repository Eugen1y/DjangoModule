"""
User Application Views
======================

"""

from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, CreateView

from user.forms import UserSignUpForm


class UserSignUpView(CreateView):
    """User sign up view implementation"""

    template_name = "registration/signup.html"
    form_class = UserSignUpForm
    success_url = reverse_lazy("login")


class UserLoginView(LoginView):
    """User login view implementation"""

    def get_success_url(self):
        """Return an URL to redirect to"""

        return self.request.GET.get("next") or reverse_lazy("product-list")


class UserLogoutView(View):
    """User logout view implementation"""

    def get(self, *args, **kwargs):
        """Handle GET request"""

        logout(self.request)

        redirect_url = reverse_lazy("home")
        return HttpResponseRedirect(redirect_url)


class UserProfileView(LoginRequiredMixin, TemplateView):
    """"User profile view implementation"""

    template_name = "user/profile.html"
