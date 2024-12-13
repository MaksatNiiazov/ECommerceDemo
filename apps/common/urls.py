from django.urls import path

from apps.common.views import DashboardView

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),

]