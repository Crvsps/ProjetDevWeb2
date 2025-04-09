from django.urls import path
from .views import CreateAccount, LoginPage, LogoutPage

urlpatterns = [
    path('register/', CreateAccount.as_view()),
    path('login/', LoginPage.as_view()),
    path('logout/', LogoutPage.as_view()),
]