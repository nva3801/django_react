from django.urls import path
from CategoryItems.views import cateitem_list,cateitem_create, categoryitem
urlpatterns=[
    path('list/',cateitem_list),
    path('',cateitem_create),
    path('<int:pk>',categoryitem)
]