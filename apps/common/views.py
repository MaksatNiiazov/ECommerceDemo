from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


def dashboard_callback(request, context):

    context.update({
        'total_users': 120,
        'total_orders': 45,
        'total_revenue': 15000,
        'best_selling_products': [
            {'name': 'Product 1', 'sales': 25},
            {'name': 'Product 2', 'sales': 20},
            {'name': 'Product 3', 'sales': 18},
        ],
        'recent_orders': [
            {'order_id': 101, 'customer': 'John Doe', 'total': 300, 'status': 'Completed'},
            {'order_id': 102, 'customer': 'Jane Smith', 'total': 450, 'status': 'Pending'},
        ],
    })
    return context



class DashboardView(TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
