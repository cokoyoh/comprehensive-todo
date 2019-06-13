from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('mark-completed/<int:id>', views.mark_as_completed),
]
