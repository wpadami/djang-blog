from django.urls import path

from . import views

app_name = "blog"
urlpatterns = [
    path('', views.BlogIndexView.as_view(), name='blog-index'),
    path('<slug:cat_slug>/<slug:slug>/', views.detail, name='blog-detail'),

]