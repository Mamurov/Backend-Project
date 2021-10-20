from .models import *
from django.shortcuts import render
from .models import Video
from .forms import VideoForm
from django.shortcuts import render
from django.core.paginator import Paginator


def index(request):
    pass

""" Song"""
def song(request):
    paginator = Paginator(Song.objects.all(), 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {"page_obj": page_obj}
    return render(request, "", context)  # Шаблон


def showvideo(request):
    firstvideo = Video.objects.last()
    videofile = firstvideo.file.url
    form = VideoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
    context = {'file_url': videofile, 'form': form}
    return render(request, '', context)  # Шаблон


class PostListView(Paginator):
    model = Post
    paginate_by = 5
    ordering = ['id']
    template_name = ''  # Шаблон
    context_object_name = 'posts'

