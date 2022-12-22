from django.urls import path
from ProductImages.views import productimg_list,productimg_create, productimg
urlpatterns=[
    path('list/',productimg_list),
    path('',productimg_create),
    path('<int:pk>',productimg)
]