from django.shortcuts import render, redirect, get_object_or_404
from shop.models import Category, Product, Comment
from shop.forms import CategoryForm, ProductForm, CommentForm

def home(request):
    return render(request, 'shop/home.html', {'title':'Главная страница'})

def category(request):
    categories = Category.objects.all()
    context = {
        'title': 'Categories',
        'categories':categories
    }
    return render(request, 'shop/category_list.html', context=context)

def product(request):
    products = Product.objects.all()
    context = {
        'title': 'Product',
        'products':products
    }
    return render(request, 'shop/product_list.html', context=context)

def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('shop:category_list')  
    else:
        form = CategoryForm()  

    context = {
        'form': form,
        'title': 'Create Category'
    }
    return render(request, 'shop/create_category.html', context=context)


def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug) 
    products = category.products_category.all()
     
    context = {
        'category': category,
        'products': products,
        'title': category.title  
    }
    return render(request, 'shop/category_detail.html', context)


def update_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('shop:category_detail', slug=category.slug)
    else:
        form = CategoryForm(instance=category)

    context = {
        'form': form,
        'title': 'Update Category'
    }
    return render(request, 'shop/update_category.html', context)

def delete_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    if request.method == 'POST':
        category.delete()
        return redirect('shop:category_list')





def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('shop:product_list')  
    else:
        form = ProductForm()  

    context = {
        'form': form,
        'title': 'Create product'
    }
    return render(request, 'shop/create_product.html', context=context)

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug) 
    comments = product.product_comment.all()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.product = product
            comment.save()
            return redirect('shop:product_detail', slug=product.slug)
    else:
        form = CommentForm()       
    context = {
        'product': product,
        'title': product.name,
        'comments': comments,
        'form': form,  
    }
    return render(request, 'shop/product_detail.html', context)


def update_product(request, slug):
    product = get_object_or_404(Product, slug=slug)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('shop:product_detail', slug=product.slug)
    else:
        form = ProductForm(instance=product)

    context = {
        'form': form,
        'title': 'Update Product'
    }
    return render(request, 'shop/update_product.html', context)

def delete_product(request, slug):
    product = get_object_or_404(Product, slug=slug)
    if request.method == 'POST':
        product.delete()
        return redirect('shop:product_list')


def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user == comment.author:
        product_slug = comment.product.slug
        comment.delete()
    return redirect('shop:product_detail', slug=product_slug)  
   

def update_comment(request, product_slug, comment_id):
    comment = get_object_or_404(Comment, id=comment_id, author=request.user)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('shop:product_detail', slug=product_slug)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'shop/update_comment.html', {'form': form, 'product_slug': product_slug, 'comment': comment})