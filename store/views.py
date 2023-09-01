from django.shortcuts import render, redirect
from .models import Post, Author, BidDetail
from .forms import BidForm


def details(request, num):
    post = Post.objects.get(pk=num)
    if request.method == 'POST':
        forms = BidForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('/')
    forms = BidForm()
    return render(request, 'store/details.html', {'post': post, 'forms': forms})


def author(request, auth):
    profile = Author.objects.get(username__username=auth)
    posts = Post.objects.filter(Active=1, Artist__username=auth)
    context = {'profile': profile, 'posts': posts}
    return render(request, 'store/author.html', context)
