from . import views
from django.urls import path

urlpatterns = [    
    path('asset-list', views.assetList, name='asset-list'),
    path('asset-create', views.assetCreate, name='asset-create'),
    path('asset-update/<int:id>', views.assetUpdate, name='asset-update'),
    path('asset-delete/<int:id>', views.assetDelete, name='asset-delete'),
]