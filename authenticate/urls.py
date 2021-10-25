from django.urls import path
from .views import Login, Logout


urlpatterns = [
    path('logout/', Logout.as_view()),
    path('login/', Login.as_view()),
]
