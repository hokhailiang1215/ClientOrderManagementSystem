from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q
from .models import Client, Order
from .forms import ClientForm, OrderForm
from django.http import HttpResponse
import csv

# ---------------- CLIENT CSV ----------------
@login_required
def export_clients_csv(request):
    # Filter if search query exists
    query = request.GET.get('q', '')
    clients = Client.objects.all()
    if query:
        clients = clients.filter(
            Q(name__icontains=query) | Q(company__icontains=query)
        )

    # Create the HttpResponse object with CSV headers
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="clients.csv"'

    writer = csv.writer(response)
    # Write header row
    writer.writerow(['Name', 'Email', 'Phone', 'Company', 'Created At'])

    # Write data rows
    for client in clients:
        writer.writerow([client.name, client.email, client.phone, client.company, client.created_at])

    return response


# ---------------- ORDER CSV ----------------
@login_required
def export_orders_csv(request):
    # Filter if search query or status exists
    search_query = request.GET.get('search', '')
    status_filter = request.GET.get('status', '')
    orders = Order.objects.select_related('client').all()

    if search_query:
        orders = orders.filter(client__name__icontains=search_query)
    if status_filter:
        orders = orders.filter(status=status_filter)

    # Create the HttpResponse object with CSV headers
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="orders.csv"'

    writer = csv.writer(response)
    # Write header row
    writer.writerow(['Title', 'Description', 'Client', 'Amount', 'Status', 'Created At'])

    # Write data rows
    for order in orders:
        writer.writerow([
            order.title,
            order.description,
            order.client.name,
            order.amount,
            order.status,
            order.created_at,
        ])

    return response

# ------------------ DASHBOARD ------------------
@login_required
def dashboard(request):
    total_clients = Client.objects.count()
    total_orders = Order.objects.count()
    pending_orders = Order.objects.filter(status='Pending').count()
    in_progress_orders = Order.objects.filter(status='In Progress').count()
    completed_orders = Order.objects.filter(status='Completed').count()

    context = {
        'total_clients': total_clients,
        'total_orders': total_orders,
        'pending_orders': pending_orders,
        'in_progress_orders': in_progress_orders,
        'completed_orders': completed_orders,
    }
    return render(request, 'core/dashboard.html', context)


# ------------------ CLIENT VIEWS ------------------
@method_decorator(login_required, name='dispatch')
class ClientListView(ListView):
    model = Client
    template_name = 'core/client_list.html'
    context_object_name = 'page_obj'  # pass paginated object
    paginate_by = 10  # 10 clients per page

    def get_queryset(self):
        queryset = Client.objects.all()
        search_query = self.request.GET.get('q')
        if search_query:
            queryset = queryset.filter(
                Q(name__icontains=search_query) | Q(company__icontains=search_query)
            )
        return queryset.order_by('name')  # optional: order alphabetically

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        return context


@method_decorator(login_required, name='dispatch')
class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    template_name = 'core/client_form.html'
    success_url = reverse_lazy('client-list')


@method_decorator(login_required, name='dispatch')
class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    template_name = 'core/client_form.html'
    success_url = reverse_lazy('client-list')


@method_decorator(login_required, name='dispatch')
class ClientDeleteView(DeleteView):
    model = Client
    template_name = 'core/client_confirm_delete.html'
    success_url = reverse_lazy('client-list')


# ------------------ ORDER VIEWS ------------------
@method_decorator(login_required, name='dispatch')
class OrderListView(ListView):
    model = Order
    template_name = 'core/order_list.html'
    context_object_name = 'page_obj'  # paginated object
    paginate_by = 10  # 10 orders per page

    def get_queryset(self):
        queryset = Order.objects.select_related('client').all()
        
        # Filters from GET parameters
        search_query = self.request.GET.get('search')
        status_filter = self.request.GET.get('status')

        if search_query:
            queryset = queryset.filter(client__name__icontains=search_query)
        if status_filter:
            queryset = queryset.filter(status=status_filter)

        return queryset.order_by('-created_at')  # newest first

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = self.request.GET.get('search', '')
        context['status'] = self.request.GET.get('status', '')
        context['clients'] = Client.objects.all()
        return context


@method_decorator(login_required, name='dispatch')
class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'core/order_form.html'
    success_url = reverse_lazy('order-list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class OrderUpdateView(UpdateView):
    model = Order
    form_class = OrderForm
    template_name = 'core/order_form.html'
    success_url = reverse_lazy('order-list')


@method_decorator(login_required, name='dispatch')
class OrderDeleteView(DeleteView):
    model = Order
    template_name = 'core/order_confirm_delete.html'
    success_url = reverse_lazy('order-list')
