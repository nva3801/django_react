from django.urls import path
from User.views import user_list, user_create
urlpatterns=[
    path('list/',user_list),
    path('',user_create)
]