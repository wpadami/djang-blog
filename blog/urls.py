from django.urls import path

from . import views

app_name = "blog"
urlpatterns = [
    path('', views.BlogIndexView.as_view(), name='blog-index'),
    path('<slug:cat_slug>/<slug:slug>/', views.DetailedView.as_view(), name='blog-detail'),
    path('<slug:cat_slug>/', views.CategoryListView.as_view(), name='cat-index'),
]