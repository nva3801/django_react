from django.urls import path
from CategoryList.views import cate_list1,categorylist, catelist_create 
urlpatterns=[
    path('list/',cate_list1),
    path('',catelist_create),
    path('<int:pk>',categorylist)
]