"""
URL configuration for fancy_cars project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from garage.views import (CarListView, 
                          CarDetailView,
                          CarCreateView,
                          CarUpdateView,
                          CarDeleteView,
                          CarListViewByMake,
                          CarListViewByColor)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', CarListView.as_view(), name="car-list"),
    path('allcars/<int:pk>/', CarDetailView.as_view(), name="car-detail"),
    path("allcars/create/", CarCreateView.as_view(), name='car-create'),
    path("allcars/update/<int:pk>/", CarUpdateView.as_view(), name='car-update'),
    path("allcars/delete/<int:pk>/", CarDeleteView.as_view(), name='car-delete'),
    path("allcars/<make>/",CarListViewByMake.as_view(), name = 'car_make'),
    path('allcars/c/<color>/', CarListViewByColor.as_view(), name="car_color"),
]  #make is the key and can 
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
