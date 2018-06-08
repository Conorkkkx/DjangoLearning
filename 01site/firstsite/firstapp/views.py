from django.shortcuts import render, HttpResponse, redirect
from firstapp.models import People, Article, Comment
from django.template import Context, Template
from firstapp.form import CommentForm

def index(request):
    requestGET = request.GET.get('tag')
    if requestGET:
        article_list = Article.objects.filter(tag=requestGET)
    else:
        article_list = Article.objects.all()
    context = {}
    context['article_list'] = article_list
    index_page = render(request, 'index.html', context)
    return index_page

def detail(request,page_num):
    if request.method == 'GET':
        form = CommentForm
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['comment']
            comment = form.cleaned_data['comment']
            c = Comment(name=name, comment=comment)
            c.save()
            return redirect(to='detail')
    context = {}
    a = Article.objects.get(id=page_num)
    best_comment = Comment.objects.filter(best_comment=True, belong_to=a)
    if best_comment:
        context['best_comment'] = best_comment[0]
    article = Article.objects.get(id=page_num)
    context['article'] = article
    context['form'] = form
    return render(request,'detail.html',context)
