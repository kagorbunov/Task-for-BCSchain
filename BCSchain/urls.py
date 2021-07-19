from django.urls import path

from . import views

urlpatterns = [
    path('', views.table, name='table'),
    path('blocks/<int:OneBlock_height>/', views.OneBlocks, name='OneBlock_height')
]
