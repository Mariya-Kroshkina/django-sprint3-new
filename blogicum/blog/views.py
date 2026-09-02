from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .models import Category, Post


POSTS_NUMBER_ON_INDEX = 5


def posts_filter(queryset):
    """Применяет стандартные фильтры для опубликованных постов."""
    return queryset.filter(
        pub_date__lte=timezone.now(),
        is_published=True,
        category__is_published=True
    )


def index(request):
    return render(
        request,
        'blog/index.html',
        {
            'posts': posts_filter(
                Post.objects.select_related(
                    'category', 'location', 'author'
                )
            )[:POSTS_NUMBER_ON_INDEX]
        }
    )


def post_detail(request, post_id):
    return render(
        request,
        'blog/detail.html',
        {
            'post': get_object_or_404(posts_filter(
                Post.objects.select_related('category', 'location', 'author')
            ),
                pk=post_id
            )
        }
    )


def category_posts(request, category_slug):
    category = get_object_or_404(
        Category.objects.filter(is_published=True),
        slug=category_slug
    )

    return render(
        request,
        'blog/category.html',
        {
            'category': category,
            'posts': posts_filter(
                category.posts_category.select_related(
                    'category', 'location', 'author'
                )
            )
        }
    )
