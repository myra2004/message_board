from django.urls import path
from .views import HomePageView
from posts import views


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('citizen_kane/', views.citizen_kane),
    path('casablanca/', views.casablanca),
    # path('maltese_falcon/', views.maltese_falcon),
    path('psycho/', views.psycho),
]

