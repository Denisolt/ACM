from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .forms import UserForm
from .forms import UploadFileForm
from .models import Event, Post

#from somewhere import handle_uploaded_file

# Create your views here.

def index(request):
    events = Event.objects.filter().order_by('start')
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:3]
    return render(request, 'blog/index.html', {'events': events,'posts': posts})

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def events(request):
    return render(request, 'blog/Events.html')

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('/completed')
    else:
        form = UserForm()
    return render(request, 'blog/signup.html', {'form': form})

def completed(request):
    return render(request, 'blog/Completed.html')

#def competition(request):
#    return render(request, 'blog/competition.html')


#def competition(request):
#    if request.method == 'POST':
#        form = UploadFileForm(request.POST, request.FILES)
#        if form.is_valid():
#            #handle_uploaded_file(request.FILES['file'])
#            post = form.save(commit=False)
#            post.author = request.user
#            post.published_date = timezone.now()
#            post.save()
#            return redirect('/completed')
#    else:
#        form = UploadFileForm()
#    return render(request, 'blog/competition.html', {'form': form})


def competition(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('/completed')
    else:
        form = UserForm()
    return render(request, 'blog/competition.html', {'form': form})


