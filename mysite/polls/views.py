from django.http import Http404
from .models import Album
from django.shortcuts import render


def index(request):
    all_albums = Album.objects.all()
    context = {'all_albums': all_albums}
    return render(request, 'polls/index.html', context)


def detail(request, album_id):
    try:
        album = Album.objects.get(id=album_id)
    except Album.DoesNotExist:
        raise Http404("Album does not exist")
    return render(request, 'polls/detail.html', {'album': album})
# Create your views here.
# html = ''
    # for album in all_albums:
    #    url = '/polls/' + str(album.id) + '/'
    #    html += '<a href="' + url + '">' + album.album_tittle + '</a><br>'
