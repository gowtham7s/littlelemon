from django.contrib import admin 
from django.urls import path 
# from .views import sayHello 
from . import views
  
urlpatterns = [ 
    # path('', sayHello, name='sayHello'), 
    path('', views.index, name='index'),
    #add following lines to urlpatterns list 
    path('menu/', views.MenuItemsView.as_view()),  # ✅ correct class name
    path('menu/<int:pk>', views.SingleMenuView.as_view()),
]