from django.urls import path
from .views import ComplistALLView,CompDetalesView,CompCreateView,CompDeleteView,CompUpdateView
urlpatterns=[
    path('get_all/',ComplistALLView.as_view()),
    path("get_by_index/<int:pk",CompDetalesView.as_view()),
    path('create/',CompCreateView.as_view()),
    path("update/<int:pk>/",CompUpdateView.as_view()),
    path('delete/<int:pk>/',CompDeleteView.as_view()),

]