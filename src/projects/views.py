from django.shortcuts import render,get_object_or_404,redirect,reverse
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger 
from django.db.models import Count ,Q
from .models import Post,Comment,Author
from .forms import CommentForm

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