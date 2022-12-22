from django.urls import path
from Categories.views import cate_list,cate_create, category
urlpatterns=[
    path('list/',cate_list),
    path('',cate_create),
    path('<int:pk>',category)
]