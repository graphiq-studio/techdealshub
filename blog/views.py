from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator
from .models import BlogPost


def blog_list(request):
    """Blog posts list view."""
    posts = BlogPost.objects.filter(is_published=True).order_by('-published_at')
    
    # Pagination
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)

    context = {'posts': posts}
    return render(request, 'blog/blog_list.html', context)


def blog_detail(request, slug):
    """Blog post detail view."""
    post = get_object_or_404(BlogPost, slug=slug, is_published=True)
    
    # Increment views
    post.views_count += 1
    post.save(update_fields=['views_count'])
    
    # Get related posts
    related_posts = BlogPost.objects.filter(
        is_published=True
    ).exclude(id=post.id).order_by('-published_at')[:3]

    context = {
        'post': post,
        'related_posts': related_posts,
    }
    return render(request, 'blog/blog_detail.html', context)
