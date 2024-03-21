"""
URL configuration for config project.

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
from django.urls import path
from main.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', root),
    path('about/', about),
    path('products/', products),
    path('compressors/', compressors),
    path('fittings/', fittings),
    path('gaskets/', gaskets),
    path('flanges/', flanges),
    path('valves2/', valves2),
    path('pipes/', pipes),
    path('instrumentation/', instrumentation),
    path('electricals/', electricals),
    path('valves/', valves),
    path('checkout/', checkout),
    path('contacto/', contacto),
    path('attachment/', attachment),
    path('news/', news),
    path('client/', client),
    path('cart/', cart),
    path('privacy-policy/', privacy_policy),
    path('terms-and-conditions/', terms_and_conditions),
    path('user-registration/', user_registration),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
