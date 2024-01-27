from django.urls import path
from . views import *

urlpatterns = [
    path('list', BlogView.as_view(),name='list'),
    path('<int:pk>', BlogView.as_view(), name='blog-view'),
    path('blog/update/<int:pk>', BlogUpdateView.as_view(), name='blog-update'),   
]