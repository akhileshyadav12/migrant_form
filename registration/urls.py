from django.urls import path

from . import views

app_name = 'registration'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    #path('<int:question_id>/vote/', views.vote, name='vote'),
    path('register',views.PersonCreateView.as_view(),name='register'),
    path('data',views.data,name="data")


]
