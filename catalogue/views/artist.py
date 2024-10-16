from django.shortcuts import (render, HttpResponseRedirect)
from django.http import Http404

from catalogue.models import Artist
from catalogue.forms import Artistorm

# Create your views here.
def index(request):
	artists = Artist.objects.all()
	
	return render(request, 'artist/index.html', {
		'artists':artists,
	})

def show(request, artist_id):
	try:
		artist = Artist.objects.get(id=artist_id)
	except Artist.DoesNotExist:
		raise Http404('Artist inexistant');
		
	return render(request, 'artist/show.html', {
		'artist':artist,
	})

def edit(request, artist_id):
	 # dictionary for initial data with 
    # field names as keys
    context = {}

    # fetch the object related to passed id
    artist = Artist.objects.get(id=artist_id)

    # pass the object as instance in form
    form = ArtistForm(request.POST or None, instance = artist)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/"+id)

    # add form dictionary to context
    context["form"] = form

    return render(request, "edit.html", context)

def update(request, artist_id):
	try:
		artist = Artist.objects.get(id=artist_id)
	except Artist.DoesNotExist:
		raise Http404('Artist inexistant');

	return render(request, 'artist/show.html', {
		'artist':artist,
	})

