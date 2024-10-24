from django.shortcuts import redirect, render, get_object_or_404
from django.http import Http404

from catalogue.models import Artist
from catalogue.forms import ArtistForm

# Create your views here.
def index(request):
	artists = Artist.objects.all()
	
	return render(request, 'artist/index.html', {
		'artists' : artists,
	})

def show(request, artist_id):
	try:
		artist = Artist.objects.get(id=artist_id)
	except Artist.DoesNotExist:
		raise Http404('Artist inexistant');
		
	return render(request, 'artist/show.html', {
		'artist' : artist,
	})

def create(request): 
	form = ArtistForm(request.POST or None)
	
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			
			return redirect('catalogue:artist-index')

	return render(request, 'artist/create.html', {
		'form' : form,
	})

def edit(request, artist_id): 
	# fetch the object related to passed id
	artist = Artist.objects.get(id=artist_id)

	# pass the object as instance in form
	form = ArtistForm(request.POST or None, instance = artist)
	
	if request.method == 'POST':	#TODO http_override doesn't work
		# save the data from the form and
		# redirect to detail_view
		if form.is_valid():
			form.save()
			
			return render(request, "artist/show.html", {
				'artist' : artist,
			})

	return render(request, 'artist/edit.html', {
		'form' : form,
		'artist' : artist,
	})

def delete(request, artist_id): 
    print('ok')
    artist = get_object_or_404(Artist, id = artist_id)
    print(request.method)
    if request.method =="POST":
        artist.delete()

        return redirect('catalogue:artist-index')

    return render(request, 'artist/show.html', {
		'artist' : artist,
	})