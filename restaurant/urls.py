from django.contrib import admin 
from django.urls import path , include
# from .views import sayHello 
from . import views
from restaurant import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [ 
    # path('', sayHello, name='sayHello'), 
    path('', views.index, name='index'),
    #add following lines to urlpatterns list 
    path('menu/', views.MenuItemsView.as_view()),  # ✅ correct class name
    path('menu/<int:pk>', views.SingleMenuView.as_view()),
    path('menu-items/', views.MenuItemsView.as_view()),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
    # path('api/',include('littlelemon.urls')),
    path('secured/', views.securedview, name='securedview'),  # ✅ secured view
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('message/', views.messageView, name='message'),
]