from django.urls import path
from CheckOut.views import checkout_list,checkout_create
urlpatterns=[
    path('list/',checkout_list),
    path('',checkout_create)
]