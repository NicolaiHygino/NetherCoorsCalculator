from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('coordcalc/', include('coordcalculator.urls')),
    path('admin/', admin.site.urls),
]
