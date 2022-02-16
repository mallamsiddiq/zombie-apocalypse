from django.urls import path

from .views import RegisterView,survivor_detail_api,statview,robotsview
from . import views
from rest_framework import permissions

  
urlpatterns = [
   # path('items/', views.home, name='home'),
   # path('items/<int:id>/', views.details, name='item-detail'),
   # path('author_review/<str:slug>/', views.author_review, name='author-review'),
   
   # # path('api/items-api/', ItemView.as_view(),name='all_items_api'),
   path('api/survivors', RegisterView.as_view(), name='list-api'),
   path('api/<str:username>/', survivor_detail_api.as_view(), name='author-review'),
   path('survivorstats/', statview, name='stats'),
   path('robots/', robotsview, name='robots'),



   # path('api/<int:pk>/', item_detail_api.as_view(), name='details'),
   
]
