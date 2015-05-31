from django.shortcuts import render_to_response
from GG_Products.models import Category

# Create your views here.
def menu(request):
	categories = Category.objects.filter(cate_parent_id__isnull=True)
	return render_to_response("menu.html", {"categories": categories})

def home(request):
	return render_to_response("home.html")

