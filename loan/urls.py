from django.urls import path
from loan.views import (
    LoanDeleteView,
    LoanListView,
    LoanUpdateView,
    LandingPageView,
    custom_logout,
    LoanCreateView,
)
from django.contrib.auth import views as auth_views


urlpatterns = [
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="login.html", success_url="loan_list"
        ),
        name="login",
    ),
    path("new/", LoanCreateView.as_view(), name="new-loan"),
    path("logout/", custom_logout, name="logout"),
    path("landing/", LandingPageView.as_view(), name="landing_page"),
    path("loans/", LoanListView.as_view(), name="loan_list"),
    path("loan/<int:pk>/", LoanUpdateView.as_view(), name="loan_update"),
    path("loan/<int:pk>/delete/", LoanDeleteView.as_view(), name="loan_delete"),
]
