from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    DeleteView,
    TemplateView,
)
from loan.forms import LoanForm, UpdateLeanForm
from services.moni.moni_client import MoniClient
from utils.validators import is_admin_user
from .models import Loan
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect
from django.contrib.auth import logout


def custom_logout(request):
    logout(request)
    return redirect("landing_page")


class LandingPageView(TemplateView):
    template_name = "loan/landing_page.html"


class AdminFuncValiadotor:
    def test_func(self):
        return is_admin_user(self.request.user)


class LoanCreateView(CreateView):
    model = Loan
    template_name = "loan/loan_create.html"
    form_class = LoanForm
    ordering = ["id"]
    success_url = reverse_lazy("landing_page")

    gender_choices_es = {
        "Male": "Masculino",
        "Female": "Femenino",
        "Other": "Otro",
    }

    def form_valid(self, form):
        moni_client = MoniClient()
        if not moni_client.check_pre_score(form.instance.dni):
            form.add_error("dni", "El dni no esta aprobado para el prestamo")
            return self.form_invalid(form)

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["gender_choices_es"] = self.gender_choices_es
        return context


class LoanListView(AdminFuncValiadotor, UserPassesTestMixin, ListView):
    model = Loan
    template_name = "loan/loan_list.html"
    context_object_name = "loans"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        gender_choices_es = {"M": "Masculino", "F": "Femenino", "O": "Otro"}
        context["gender_choices_es"] = gender_choices_es
        return context


class LoanUpdateView(AdminFuncValiadotor, UserPassesTestMixin, UpdateView):
    model = Loan
    template_name = "loan/loan_update.html"
    form_class = UpdateLeanForm
    success_url = reverse_lazy("loan_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        gender_choices_es = {"Male": "Masculino", "Female": "Femenino", "Other": "Otro"}
        context["gender_choices_es"] = gender_choices_es

        return context


class LoanDeleteView(AdminFuncValiadotor, UserPassesTestMixin, DeleteView):
    model = Loan
    template_name = "loan/loan_delete.html"
    success_url = reverse_lazy("loan_list")
