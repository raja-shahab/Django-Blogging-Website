from django.shortcuts import redirect, render, get_object_or_404
from blog.models import Blog
from blogging_platform.forms import BlogForm

def blog_list(request):
    list = Blog.objects.all()
    return render(request, 'home.html', {'list':list})

def blog_detail(request, pk):
    blog = Blog.objects.get(pk = pk)

    context = {
        'blog' : blog
    }
    return render(request, 'blog.html', context)

def edit_blog(request ,pk):
    blog = get_object_or_404(Blog, pk = pk)

    if request.method == 'POST':
        form = BlogForm(request.POST, instance=blog)

        if form.is_valid():
            form.save()
            return redirect('product_list')

    else:
        form = BlogForm(instance=blog)

    context = {
        'form' : form
    }
    return render(request, 'edit.html', context)

def delete_blog(request, pk):
    blog = get_object_or_404(Blog, pk = pk)

    if request.method == 'POST':
        blog.delete()
        return redirect('blog_list')

    return render(request, 'delete.html', {'blog': blog})

# Another way without using forms.py

''' 
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Product

# Create a new product manually
def create_product(request):
    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        image = request.FILES.get('image')

        # Validate and save the product manually
        if name and description and image:
            product = Product(name=name, description=description, image=image)
            product.save()
            return redirect('product_list')
        else:
            return HttpResponse("Invalid data", status=400)
    return render(request, 'myapp/product_form.html')

# Update an existing product manually
def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        image = request.FILES.get('image')

        # Validate and update the product manually
        if name and description and image:
            product.name = name
            product.description = description
            product.image = image
            product.save()
            return redirect('product_detail', pk=product.pk)
        else:
            return HttpResponse("Invalid data", status=400)
    return render(request, 'myapp/product_form.html', {'product': product})

# Other views (product_list, product_detail, delete_product) remain the same

'''