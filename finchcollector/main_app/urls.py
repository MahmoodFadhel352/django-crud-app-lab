from django.urls import path
from . import views # Import views to connect routes to view functions

urlpatterns = [
    # Routes will be added here
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('finchs/', views.finch_index, name='finch-index'),
    path('finchs/<int:finch_id>/', views.finch_detail, name='finch-detail'),
    path('finchs/create/', views.FinchCreate.as_view(), name='finch-create'),
    path('finchs/<int:pk>/update/', views.FinchUpdate.as_view(), name='finch-update'),
    path('finchs/<int:pk>/delete/', views.FinchDelete.as_view(), name='finch-delete'),
]