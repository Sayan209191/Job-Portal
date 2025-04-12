from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, LikeDislike
from .forms import ArticleForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

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

@login_required
def edit_blog(request, blog_id):
    blog = get_object_or_404(Article, id=blog_id)

    if request.user != blog.author:
        return redirect('blog_detail', blog_id=blog_id)

    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=blog)
        if form.is_valid():
            updated_blog = form.save(commit=False)
            updated_blog.isUpadated = True
            updated_blog.updated_at = timezone.now()
            updated_blog.save()
            return redirect('blog_detail', blog_id=blog_id)
    else:
        form = ArticleForm(instance=blog)

    return render(request, 'blog/editblog.html', {'form': form})
@login_required
def like_article(request, blog_id):
    article = get_object_or_404(Article, id=blog_id)
    existing_like_dislike = LikeDislike.objects.filter(article=article, user=request.user).first()

    if existing_like_dislike:
        if existing_like_dislike.choice == LikeDislike.LIKE:
            return redirect('blog_detail', blog_id=article.id)
        else:
            # User previously disliked, change to like
            existing_like_dislike.choice = LikeDislike.LIKE
            existing_like_dislike.save()

            # Update like and dislike counts
            article.like_count += 1
            article.dislike_count -= 1
            article.save()
    else:
        # User hasn't interacted yet, create a LikeDislike record
        LikeDislike.objects.create(article=article, user=request.user, choice=LikeDislike.LIKE)

        # Increment the like count
        article.like_count += 1
        article.save()

    # Redirect back to the article detail page (or you can change this as needed)
    return redirect('blog_detail', blog_id=article.id)
@login_required
def dislike_article(request, blog_id):
    article = get_object_or_404(Article, id=blog_id)
    existing_like_dislike = LikeDislike.objects.filter(article=article, user=request.user).first()

    if existing_like_dislike:
        if existing_like_dislike.choice == LikeDislike.DISLIKE:
            return redirect('blog_detail', blog_id=article.id)
        else:
            # User previously liked, change to dislike
            existing_like_dislike.choice = LikeDislike.DISLIKE
            existing_like_dislike.save()

            # Update like and dislike counts
            article.dislike_count += 1
            article.like_count -= 1
            article.save()
    else:
        # User hasn't interacted yet, create a LikeDislike record
        LikeDislike.objects.create(article=article, user=request.user, choice=LikeDislike.DISLIKE)

        # Increment the dislike count
        article.dislike_count += 1
        article.save()

    # Redirect back to the article detail page (or you can change this as needed)
    return redirect('blog_detail', blog_id=article.id)