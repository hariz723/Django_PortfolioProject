from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('reg',views.reg,name="register"),
    path('login',views.login_page,name="login"),
    path('logout',views.logout_page,name="logout"),
    path('collecions',views.collections,name="collections"),
    path('collecions/<str:name>',views.collectionsview,name="collections"),
    path('collecions/<str:cname>/<str:pname>',views.product_details,name="product_details"),
]
