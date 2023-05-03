from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.forms import inlineformset_factory
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout

from customers.decorators import unauthorized_user, allowed_role, strong_perm
from customers.filters import OrderFilter
from customers.forms import OrderForm, CreationUserForm, CustomerForm
from customers.models import Product, Customer, Order


@unauthorized_user
def register_user(request):
    form = CreationUserForm()

    if request.method == 'POST':
        form = CreationUserForm(request.POST)

        if form.is_valid():
            user = form.save()
            messages.success(request, f'account created successfully {user.username}')
            return redirect('login')

    context = {'form': form}
    return render(request, 'customers/authentication/register.html', context)


@unauthorized_user
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Username or Password is invalid')

    context = {}
    return render(request, 'customers/authentication/login.html', context)


def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('login')


@login_required(login_url=reverse_lazy('login'))
@strong_perm
def home(request):
    customers = Customer.objects.all()
    orders = Order.objects.all()

    context = {
        'customers': customers,
        'orders': orders,
        'total_orders': orders.count(),
        'orders_delivered': orders.filter(status='Delivered').count(),
        "orders_pending": orders.filter(status='Pending').count(),
    }

    return render(request, 'customers/dashboard.html', context)


@login_required(login_url=reverse_lazy('login'))
@allowed_role(allowed_user=['customer'])
def user_page(request):
    orders = request.user.customer.order_set.all()
    context = {
        'orders': orders,
        'total_orders': orders.count(),
        'orders_delivered': orders.filter(status='Delivered').count(),
        "orders_pending": orders.filter(status='Pending').count(),
    }
    return render(request, 'customers/users/user.html', context)


@login_required(login_url=reverse_lazy('login'))
@allowed_role(allowed_user=['customer'])
def settingsUser(request):
    user = request.user.customer
    form = CustomerForm(instance=user)

    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance=user)

        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'customers/users/settings_profile.html', context)


@login_required(login_url=reverse_lazy('login'))
@allowed_role(allowed_user=['admin'])
def product(request):
    products = Product.objects.all()
    return render(request, 'customers/products.html', {'products': products})


@login_required(login_url=reverse_lazy('login'))
@allowed_role(allowed_user=['admin'])
def customer(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    customer_orders = customer.order_set.all()
    total_orders = customer_orders.count()

    filterset = OrderFilter(request.GET, queryset=customer_orders)
    customer_orders = filterset.qs

    context = {'customer': customer, 'customer_orders': customer_orders, 'total_orders': total_orders,
               'filterset': filterset}
    return render(request, 'customers/customer.html', context)


@login_required(login_url=reverse_lazy('login'))
@allowed_role(allowed_user=['admin'])
def createOrder(request, pk):
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'), extra=2)

    customer = get_object_or_404(Customer, pk=pk)
    formset = OrderFormSet(queryset=Order.objects.none(), instance=customer)
    if request.method == 'POST':
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')

    context = {'formset': formset}
    return render(request, 'customers/forms/form_order.html', context)


@login_required(login_url=reverse_lazy('login'))
@allowed_role(allowed_user=['admin'])
def updateOrder(request, pk):
    order = get_object_or_404(Order, pk=pk)
    context = {}
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')

    context['form'] = form
    return render(request, 'customers/forms/form_order.html', context)


@login_required(login_url=reverse_lazy('login'))
@allowed_role(allowed_user=['admin'])
def deleteOrder(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == "POST":
        order.delete()
        return redirect('/')
    context = {
        'item': order
    }
    return render(request, 'customers/forms/delete_order.html', context)
