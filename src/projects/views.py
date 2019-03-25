from django.shortcuts import render,get_object_or_404,redirect,reverse
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger 
from django.db.models import Count ,Q
from .models import Post,Comment,Author
from .forms import CommentForm,PostForm


def get_author(user):
    qs = Author.objects.filter(user=user)
    if qs.exists():
        return qs[0]
    return None


def get_category_count():
    queryset = Post.objects.values('categories__title').annotate(Count('categories__title'))
    return queryset

def projets(request):
    category_count = get_category_count()
    most_recent = Post.objects.order_by('-timestamp')[:4]
    project_list = Post.objects.all()
    paginator = Paginator(project_list,5)
    page_req_var = 'page'
    page = request.GET.get(page_req_var)
    try:
        paginator_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginator_queryset = paginator.page(1)
    except EmptyPage:
        paginator_queryset = paginator.page(paginator.num_pages)

    context = {
        'most_recent':most_recent,
        'category_count':category_count,
        'queryset':paginator_queryset,
        'page_req_var':page_req_var
    }
    
    return render(request,'projets.html',context)


def project_detail(request,id):
    category_count = get_category_count()
    most_recent = Post.objects.order_by('-timestamp')[:3]
    post = get_object_or_404(Post,id=id)
    ps = Post.objects.all()
    form = CommentForm(request.POST or None)
    if request.method =='POST':
        form.instance.user = request.user
        form.instance.post = post 
        form.save()
        return redirect(reverse("project-detail",kwargs={
            'id':post.pk
        }))

    context = {
        'ps':ps,
        'form':form,
        'most_recent':most_recent,
        'post':post,
        'category_count':category_count
    }
    return render(request,'project-detail.html',context)

def create_post(request):
    title='Create'
    form = PostForm(request.POST or None ,request.FILES or None)
    author = get_author(request.user)
    if request.method=='POST':
        if form.is_valid:
            form.instance.author =author
            form.save()
            return redirect(reverse("post_detail",kwargs={
                'id':form.instance.id
            }))

    context = {
        'title':title,
        'form':form
    }
    return render(request,'create_post.html',context)

def update_post(request,id):
    title='Update'
    post = get_object_or_404(Post,id=id)
    form = PostForm(request.POST or None ,request.FILES or None,instance=post)
    author = get_author(request.user)
    if request.method=='POST':
        if form.is_valid:
            form.instance.author =author
            form.save()
            return redirect(reverse("post_detail",kwargs={
                'id':form.instance.id
            }))

    context = {
        'title':title,
        'form':form
    }
    return render(request,'create_post.html',context)
    

def delete_post(request,id):
    post=get_object_or_404(Post,id=id)
    post.delete()

    return redirect(reverse("project"))
    