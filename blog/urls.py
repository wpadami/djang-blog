from django.urls import path

from . import views

app_name = "blog"
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<slug:cat_slug>/<slug:slug>/', views.DetailedView.as_view(), name='detail'),

]