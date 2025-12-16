"""
URL configuration for erp_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]


#"refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc2NTk2NTYwMSwiaWF0IjoxNzY1ODc5MjAxLCJqdGkiOiIzMjc4NTgxOTg3MTY0OWZlODVhZWMwYzA2YzBlOTJiOSIsInVzZXJfaWQiOiIxIn0.twBCubc-cvpKgXvRY2qnYHCaLXBteLiTznUL_f54igM",
    #"access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzY1ODc5NTAxLCJpYXQiOjE3NjU4NzkyMDEsImp0aSI6IjY3NDFiYWQyY2YwYTRmMDViNDU2YjlmNGRhN2FjNmQ3IiwidXNlcl9pZCI6IjEifQ.0KQpL37niHbnlBzhuSzU1iwwxWmNqun_NpHmwLCzNFg"