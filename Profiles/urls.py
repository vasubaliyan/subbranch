from django.urls import path,include
from.import views

urlpatterns=[
    
    path("sellerprofile/",views.SellerProfileAPI.as_view()),
    path("sellerprofile/<int:pk>/",views.SellerProfileAPI.as_view()),
]
