from .views import Login, Register, Logout, Account
from django.urls import path



urlpatterns = [
    path('register/', Register.as_view(), name = "register_page"),
    path('login/', Login.as_view(), name = "login_page"),
    path('logout/', Logout.as_view(), name = "logout_page"),
    path('my_account/', Account.as_view(), name = "my_account_page"),
] 