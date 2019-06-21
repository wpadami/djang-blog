from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Post

class BlogIndexView(generic.ListView):
    model = Post
    #paginate_by = 12
    template_name = 'blog/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

def detail(request, cat_slug, slug):

    post = get_object_or_404(Post, slug=slug)
    contextos =  {'post': post, 'now': timezone.now()}
    return render(request, 'blog/detail.html',contextos)