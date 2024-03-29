from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Post, Category

class BlogIndexView(generic.ListView):
    model = Post
    #paginate_by = 12
    template_name = 'blog/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class DetailedView(generic.DetailView):
    model = Post
    template_name = "blog/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class CategoryListView(generic.ListView):
    model = Category
    template_name = "blog/cat_index.html"

    def get_context_data(self, **kwargs):
        category  = get_object_or_404(Category, cat_slug=self.kwargs.get('cat_slug'))
        context = super().get_context_data(**kwargs)
        context.update({
            'post_list': Post.objects.order_by('-created_on').filter(category_id=category.id),
        })
        return context
