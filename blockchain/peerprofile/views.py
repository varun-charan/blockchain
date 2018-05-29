from django.http import HttpResponse	

# Create your views here.
def profile(request):
	return (HttpResponse("<h1>Profile Page</h1>"))