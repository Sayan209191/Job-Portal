from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import ArticleForm
from django.contrib.auth.decorators import login_required


def blog_list(request):
    blogs = Article.objects.order_by('-created_at')
    return render(request, 'blog/bloglist.html', {'blogs': blogs})


def blog_detail(request, blog_id):
    blog = get_object_or_404(Article, id=blog_id)
    return render(request, 'blog/blogdetail.html', {'blog': blog})


@login_required
def create_blog(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            return redirect('blog_list')
    else:
        form = ArticleForm()
    return render(request, 'blog/create_blog.html', {'form': form})