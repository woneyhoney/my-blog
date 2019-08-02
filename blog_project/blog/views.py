from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Blog 
from .forms import BlogPost

def home(request):
    blogs = Blog.objects 
    # queryset = .objects로 모델로부터 전달 받은 객체 목록 
    # method
    blog_list = Blog.objects.all() # 블로그 모든 글들을 대상으로
    paginator = Paginator(blog_list, 3) # 블로그 객체 3개를 한 페이지로 자르기
    page = request.GET.get('page')
    # request된 페이지가 뭔지를 알아내고 (request페이지를 변수에 담아내고)
    posts = paginator.get_page(page)
    # request된 페이지를 얻어온 뒤 return 해 준다
    return render(request, 'home.html', {'blogs':blogs, 'posts':posts})

    # 쿼리셋과 메소드의 형식
    # 모델.쿼리셋(objects).메소드

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk = blog_id)
    # 이용자가 원한 몇 번 블로그 객체 
    return render(request, 'detail.html', {'blog':blog_detail})

# new.html을 띄워주는 함수
def new(request):
    return render(request, 'new.html')

# 입력받은 내용을 데이터베이스에 넣어주는 함수
def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save() # queryset method 중 하나 
    # <-> 객체.delete()
    return redirect('/blog/'+str(blog.id)) # render 함수와 차이! 
    # redirect는 인자를 URL로 받음

def blogpost(request):
    # 1. 입력된 내용을 처리하는 기능 -> POST
    if request.method == 'POST':
        form = BlogPost(request.POST)
        if form.is_valid():
            post = form.save(commit=False) # 모델 객체를 반환하되 저장 x
            post.pub_date = timezone.now()
            post.save()
            return redirect('home')
    # 2. 빈 페이지를 띄우주는 기능 -> GET
    else:
        form = BlogPost()
        return render(request, 'new.html', {'form':form})

def search(request):
    if request.method == 'POST':
        search_word = request.POST['search_word']
        blog_list = Blog.objects.filter(
            Q(title__icontains=search_word) | Q(body__icontains=search_word) # Q 객체를 사용해서 검색
        ).distinct() # 중복 제거
        return render(request, 'search.html', {'blog_list':blog_list, 'search_word':search_word})
    return render(request, 'home.html')