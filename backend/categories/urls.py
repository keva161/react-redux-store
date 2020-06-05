from django.urls import path
from .views import CategoryView

urlpatterns = [
    path('', CategoryView.as_view()),
    path('<slug>', CategoryView.as_view()),
]