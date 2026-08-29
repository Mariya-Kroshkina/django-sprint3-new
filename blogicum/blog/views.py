from django.shortcuts import render, get_object_or_404
from .models import Category, Post
from django.utils import timezone


POSTS_NUMBER_ON_INDEX = 5


def index(request):
    template_name = 'blog/index.html'
    post_list = Post.objects.filter(
        pub_date__lte=timezone.now(),
        is_published=True,
        category__is_published=True
    ).select_related(
        'category', 'location', 'author'
    )[:POSTS_NUMBER_ON_INDEX]
    context = {'post_list': post_list}
    return render(request, template_name, context)


def post_detail(request, id):
    template_name = 'blog/detail.html'
    detail_post = get_object_or_404(
        Post.objects.select_related('category', 'location', 'author'),
        is_published=True,
        pub_date__lte=timezone.now(),
        category__is_published=True,
        pk=id
    )

    context = {'post': detail_post}
    return render(request, template_name, context)


def category_posts(request, category_slug):
    template_name = 'blog/category.html'
    category = get_object_or_404(
        Category.objects.filter(is_published=True),
        slug=category_slug
    )

    post_list = category.posts.filter(
        is_published=True,
        pub_date__lte=timezone.now()
    ).select_related('category', 'location', 'author')

    context = {
        'category': category,
        'post_list': post_list
    }
    return render(request, template_name, context)
