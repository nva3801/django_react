from django.urls import path
from TourCodes.views import tourcode_list,tourcode_create, tourCode
urlpatterns=[
    path('list/',tourcode_list),
    path('',tourcode_create),
    path('<int:pk>',tourCode)
]