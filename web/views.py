from django.shortcuts import render, redirect
from store.models import Post
from .models import Category, Collection, Create
from .forms import CreateToken


def index(request):
    posts = Post.objects.filter(Active=1)
    context = {'posts': posts}
    return render(request, 'web/index.html', context)


def explore(request, col=None):
    posts = Post.objects.filter(Active=1)
    if col != None:
        posts = posts.filter(collection__name=col)

    context = {'posts': posts}
    return render(request, 'web/explore.html', context)


def create(request):
    if request.method == 'POST':
        forms = CreateToken(request.POST, request.FILES)
        print(forms)
        if forms.is_valid():
            forms.save()
            return redirect('/')

    forms = CreateToken()
    return render(request, 'web/create.html', {'forms': forms})


def items(request, cat):
    posts = Post.objects.filter(Active=1, category__name=cat)
    category = Category.objects.get(name=cat)
    context = {'posts': posts, 'category': category}

    return render(request, 'web/items.html', context)


def search_post(request):
    if request.method == 'GET':
        search = request.GET.get('s')
        posts = Post.objects.filter(content__contains=search)

    context = {'posts': posts}
    return render(request, 'web/explore.html', context)
