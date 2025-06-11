from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from .models import Product
from .forms import ProductForm
import csv
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.
def home(request):
    from django.db.models import Sum
    query = request.GET.get('q', '').strip()

    # Initial base queryset
    base_qs = Product.objects.filter(is_active=True, quantity__gt=0)

    # If search query exists, filter it early
    if query:
        base_qs = base_qs.filter(name__icontains=query)

    # Now compute stats *after filtering*
    total_products = base_qs.count()
    total_quantity = base_qs.aggregate(Sum('quantity'))['quantity__sum'] or 0
    total_value = sum([p.quantity * float(p.price) for p in base_qs])

    return render(request, 'glassapp/index.html', {
        'products': base_qs,
        'total_products': total_products,
        'total_quantity': total_quantity,
        'total_value': total_value,
        'query': query,
    })


def product_list(request):
    query = request.GET.get('q', '')
    sort = request.GET.get('sort', 'name')
    order = request.GET.get('order', 'asc')
    products = Product.objects.filter(is_active=True)
    if query:
        products = products.filter(name__icontains=query)
    if sort in ['name', 'quantity', 'price']:
        if order == 'desc':
            sort = f'-{sort}'
        products = products.order_by(sort)
    return render(request, 'glassapp/product_list.html', {
        'products': products,
        'query': query,
        'sort': sort.lstrip('-'),
        'order': order,
    })

def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'glassapp/product_form.html', {'form': form})

def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk, is_active=True)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'glassapp/product_form.html', {'form': form, 'edit': True})

def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk, is_active=True)
    if request.method == 'POST':
        product.is_active = False
        product.save()
        return redirect('product_list')
    return render(request, 'glassapp/product_confirm_delete.html', {'product': product})

def product_import(request):
    if request.method == 'POST' and request.FILES.get('csv_file'):
        csv_file = request.FILES['csv_file']
        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'Please upload a CSV file.')
            return render(request, 'glassapp/product_import.html')
        decoded_file = csv_file.read().decode('utf-8').splitlines()
        reader = csv.DictReader(decoded_file)
        imported, updated = 0, 0
        for row in reader:
            name = row.get('name', '').strip()
            description = row.get('description', '').strip()
            try:
                quantity = int(row.get('quantity', 0))
                price = float(row.get('price', 0))
            except (ValueError, TypeError):
                continue  # skip rows with invalid data
            product, created = Product.objects.get_or_create(
                name=name,
                defaults={
                    'description': description,
                    'quantity': quantity,
                    'price': price,
                }
            )
            if not created:
                # Update quantity and price if changed
                updated_flag = False
                if product.quantity != quantity:
                    product.quantity = quantity
                    updated_flag = True
                if product.price != price:
                    product.price = price
                    updated_flag = True
                if product.description != description:
                    product.description = description
                    updated_flag = True
                if updated_flag:
                    product.save()
                    updated += 1
            else:
                imported += 1
        messages.success(request, f'Products imported: {imported}, updated: {updated}.')
        return redirect('product_list')
    return render(request, 'glassapp/product_import.html')

def product_export(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="products.csv"'
    writer = csv.writer(response)
    writer.writerow(['name', 'description', 'quantity', 'price'])
    for product in Product.objects.filter(is_active=True):
        writer.writerow([product.name, product.description, product.quantity, product.price])
    return response

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    can_retrieve = not product.is_active
    if request.method == 'POST' and can_retrieve:
        product.is_active = True
        product.save()
        messages.success(request, f'Product "{product.name}" has been restored.')
        return redirect('product_list')
    return render(request, 'glassapp/product_detail.html', {'product': product, 'can_retrieve': can_retrieve})

def soft_deleted_products(request):
    products = Product.objects.filter(is_active=False)
    return render(request, 'glassapp/soft_deleted_products.html', {'products': products})