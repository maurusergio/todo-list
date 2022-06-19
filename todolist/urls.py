from django.urls import path

from . import views

app_name = 'todolist'

urlpatterns = [
    # ex: /tasks/
    path('', views.IndexView.as_view(), name='index'),
    
    # ex: /tasks/5/
    path('<int:pk/', views.DetailView.as_view(), name='detail'),    

]