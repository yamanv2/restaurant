from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard),
    path('menu/', views.menu),
    path('order/', views.order, name="order_page"),
    path('recipe_requirement/', views.recipe_requirement),
    # path('product/<int:id>/', views.product_detail),
    # path('cart/', views.cart),
    path("manageOrder/", views.manageOrder, name='manage_order'),
    path("updateOrder/<str:pk>/", views.updateOrder, name='updateOrder'),
    path("deleteOrder/<str:pk>/", views.deleteOrder, name='deleteOrder'),
    path('signup/', views.signupPage, name="SignUp"),
    path('login/', views.loginPage, name="Login"),
    path('logout/', views.logoutUser, name="LogOut"),

]