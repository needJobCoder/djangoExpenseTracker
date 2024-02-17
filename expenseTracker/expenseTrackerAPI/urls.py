from django.contrib import admin
from django.urls import path
from .views import createUser, createPurchase
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('createUser/', createUser),
    path('createPurchase/', createPurchase)
]
