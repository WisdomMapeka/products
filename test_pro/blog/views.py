from django.shortcuts import render, get_object_or_404
from . models import Products, Categories

# Create your views here.
def index(request):
	categories = Categories.objects.all()
	products = Products.objects.all()
	if request.method=="POST":
		if 'category' in request.POST:
		    categ = request.POST['category']

		if 'product' in request.POST:
		    product = request.POST['product']

		if 'price' in request.POST:
		    price = request.POST['price']

		if 'description' in request.POST:
		    description = request.POST['description']

		ca = Categories.objects.get(id=categ)
		Products.objects.create(category=ca, product_name=product, price=price, description=description)
		print("saved")
   
	return render(request, 'blog/index.html', {"categories":categories, "products":products})



def details(request, id):
	product = get_object_or_404(Products, id=id)
	return render(request, 'blog/details.html', {"product":product})